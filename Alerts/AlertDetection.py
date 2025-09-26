import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class AlertDetection:
    def __init__(self, df_synth, models, axis_cols, residuals_synth=None):
        self.df_synth = df_synth
        self.models = models
        self.axis_cols = axis_cols
        self.residuals_synth = residuals_synth or {}
        self.thresholds = {}
        self.alerts_df = None

    def compute_residuals(self):
        for axis in self.axis_cols:
            y_pred = self.models[axis].predict(self.df_synth[["time_min"]].values)
            self.residuals_synth[axis] = self.df_synth[axis] - y_pred
        return self.residuals_synth

    def define_thresholds(self, T_seconds=5):

        for axis in self.axis_cols:
            res = self.residuals_synth[axis]
            minC = np.percentile(res,80)
            maxC = np.percentile(res,90)
            self.thresholds[axis] = {"MinC": minC, "MaxC": maxC, "T": T_seconds}
        return self.thresholds


    def detect_alerts(self):

        alerts = []


        def find_periods(mask, T_seconds):
            periods = []
            start_idx = None
            for i, val in enumerate(mask):
                if val and start_idx is None:
                    start_idx=i
                elif not val and start_idx is not None:
                    duration = self.df_synth["time_min"].iloc[i-1] - self.df_synth["time_min"].iloc[start_idx]
                    if duration >= T_seconds:
                        periods.append((self.df_synth["Time"].iloc[start_idx], self.df_synth["Time"].iloc[i-1]))
                    start_idx = None
                return periods
        for axis in self.axis_cols:
            res = self.residuals_synth[axis]
            MinC = self.thresholds[axis]["MinC"]
            MaxC = self.thresholds[axis]["MaxC"]
            T = self.thresholds[axis]["T"]

            above_min = res > MinC
            above_max = res > MaxC

            alerts += [(axis, "ALERT", s, e) for s, e in find_periods(above_min, T)]
            alerts += [(axis, "ERROR", s, e) for s, e in find_periods(above_max, T)]

        self.alerts_df = pd.DataFrame(alerts, columns=["Alert", "Type", "Start Time", "End Time"])
        return self.alerts_df

    def plot_with_alerts(self, df_train):

        for axis in self.axis_cols:
            x_test = self.df_synth["time_min"] /  60
            y_pred = self.models[axis].predict(self.df_synth[["time_min"]].values)

            plt.figure(figsize=(12, 5))
            plt.scatter(x_test, self.df_synth[axis], alpha=0.5, label="Observed (Synthetic)")
            plt.plot(x_test, y_pred, color="red", linewidth=2, label="Regression Line")

            used_labels = set()
            ymin, ymax = self.df_synth[axis].min() - 0.5, self.df_synth[axis].max() + 0.5

            for _, row in self.alerts_df[self.alerts_df["Axis"] == axis].iterrows():
                start = (row["Start Time"] - df_train["Time"].min()).total_seconds() / 3600
                end = (row["End Time"] - df_train["Time"].min()).total_seconds() / 3600
                duration_min = (row["End Time"] - row["Start Time"]).total_seconds() / 60

                color = "orange" if row["Type"] == "ERROR" else "yellow"
                label = row["Type"] if row["Type"] not in used_labels else None
                plt.axvspan(start, end, ymin=0.0, ymax=0.5, color=color, alpha=0.3, label=label)
                used_labels.add(row["Type"])

                plt.text((start + end) / 2, ymax, f"{int(duration_min)} min",
                         color="black", ha="center", va="bottom", fontsize=8, rotation=90)

            plt.ylim(ymin, ymax)
            plt.title(f"Regression with Alerts/Errors - {axis}")
            plt.xlabel("Time (Hours)")
            plt.ylabel(f"{axis} (z-score)")
            plt.legend()
            plt.show()

