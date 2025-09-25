import numpy as np
import pandas as pd

class SyntheticData:
    def __init__(self, models, residuals, df_train, axis_cols):
        self.models = models
        self.residuals = residuals
        self.df_train = df_train
        self.axis_cols = axis_cols
        self.df_synth = None


    def generate(self):
        start_time = self.df_train["Time"].min()
        end_time = self.df_train["Time"].max() + pd.Timedelta(minutes=30)
        time_index = pd.date_range(start=start_time, end=end_time, freq="1min")

        self.df_synth = pd.DataFrame({"Time": time_index})
        self.df_synth["time_min"] = (self.df_synth["Time"] - self.df_train["Time"].min()).dt.total_seconds() / 60

        for axis in self.axis_cols:
            model = self.models[axis]
            y_synth = model.predict(self.df_synth[["time_min"]].values)

            train_res = np.array(self.residuals[axis])
            repeats = int(np.ceil(len(self.df_synth)/ len(train_res)))
            synthetic_residuals = np.tile(train_res, repeats)[:len(self.df_synth)]
            self.df_synth[axis] = y_synth + synthetic_residuals

        return self.df_synth