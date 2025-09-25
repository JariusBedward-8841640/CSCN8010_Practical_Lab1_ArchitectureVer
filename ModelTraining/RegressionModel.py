import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class RegressionModel:
    def __init__(self, df_std, axis_cols):
        self.df_std = df_std
        self.axis_cols = axis_cols
        self.models = {}
        self.residuals = {}

    def fit_models(self):

        for axis in self.axis_cols:
            x = self.df_std[["time_min"]].values
            y=self.df_std[axis].values

            model = LinearRegression().fit(x,y)
            y_pred = model.predict(x)

            self.models[axis] = model
            self.residuals[axis] = y_pred - y

            print(f"{axis}: slope = {model.coef_[0]:.5f}, intercept = {model.intercept_:.5f}")
        return self.models, self.residuals

    def plot_regression(self, step=30):

        for axis in self.axis_cols:
            x = self.df_std[["time_min"]].values
            y=self.df_std[axis].values
            y_pred = self.models[axis].predict(x)

            df_plot = self.df_std.iloc[::step]

            plt.figure(figsize=(8,4))
            plt.scatter(df_plot["time_min"], df_plot[axis], alpha=0.5, label="Observed (z-scores")
            plt.plot(self.df_std["time_min"], y_pred, color="red", label = "Regression Line")
            plt.title(f"Regression {axis}")
            plt.xlabel("Time (Mins)")
            plt.ylabel(f"{axis} (z-scores)")
            plt.legend()
            plt.show()

