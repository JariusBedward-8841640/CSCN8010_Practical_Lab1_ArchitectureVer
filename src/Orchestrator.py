# Connefcts everything
# from importlib.metadata import Prepared
import pandas as pd

from DataExtraction.DataExtraction import DataExtraction
from DataPreperation.DataPreperation import DataPreperation
from DataPreperation.SyntheticData import SyntheticData
from ModelTraining.RegressionModel import RegressionModel
from Alerts.AlertDetection import AlertDetection


query = """
SELECT "timestamp", "part_id", "reading"
FROM "catdc_data_feed"
WHERE "state"='RUNNING';
"""
#Extract data
extractor = DataExtraction()
df_long = extractor.load_data(query)

# pivot to wude format
df_train = df_long.pivot_table(index='timestamp', columns='part_id', values='reading', aggfunc='mean')
df_train.columns = [f"Axis #{i}" for i in df_train.columns]
df_train.reset_index(inplace=True)
df_train.rename(columns={"timestamp": "Time"}, inplace=True)

# prepare the data
prep = DataPreperation(df_train)
df_clean = prep.clean_data()
df_norm = prep.normalize()
df_std = prep.standardize()

# Regression
reg = RegressionModel(df_std, prep.axis_cols)
models, residuals = reg.fit_models()
reg.plot_regression()

#Synthetic data

synth = SyntheticData(models, residuals, df_clean, prep.axis_cols)
df_synth = synth.generate()

#Alerts

alerts = AlertDetection(df_synth, models, prep.axis_cols)
residuals_synth = alerts.compute_residuals()
thresholds = alerts.define_thresholds()
alerts_df = alerts.detect_alerts()
alerts.plot_with_alerts(df_clean)

# Save results

thresholds_df = pd.DataFrame.from_dict(thresholds, orient='index')
thresholds.to_csv("data/processed/results_thresholds.csv", index_label="Axis")
alerts_df.to_csv("data/processed/results_detected_events.csv", index=False)
print("Results saved in the data folder successfully!")

