import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class DataPreparation:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.axis_cols = [col for col in df.columns if col.startswith("Axis #")]
        self.df_std = None
        self.df_norm = None

    def clean_data(self) -> pd.DataFrame:
        self.df.fillna(0, inplace=True)
        self.df = self.df[(self.df[self.axis_cols] != 0).any(axis=1)]
        return self.df


    def normalize(self) -> pd.DataFrame:
        scaler = MinMaxScaler
        self.df_norm = self.df.copy()
        self.df_norm[self.axis_cols] = scaler.fit_transform(self.df[self.axis_cols])
        return self.df_norm

    def standardize(self) -> pd.DataFrame:

       scaler = StandardScaler()
       self.df_std = self.df.copy()
       self.df_std[self.axis_cols] = scaler.fit_transform(self.df[self.axis_cols])
       self.df_std["time_min"] = (self.df_std["Time"] - self.df_std["Time"].min()).dt.total_seconds() / 60
       return self.df_std

