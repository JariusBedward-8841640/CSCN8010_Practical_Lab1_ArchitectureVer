# Connefcts everything
# from importlib.metadata import Prepared

from DataExtractionAnalysis.DataExtraction import DataExtraction
from DataPreperation.DataPreperation import DataPreperation
from ModelTraining.RegressionModel import RegressionModel
from Alerts.AlertDetection import AlertDetection

def main():
    # 1. Extract
    # extractor = DataPreperation("DB_URL")
    # data = extractor.load
    #
    # 2. Prepared
    # prep = DataPreperation(data)
    # prepared_data = prep.get_prepared_data()
    #
    # 3. Train Model
    # model = RegressionModel(preapred_data)
    # model.train()
    #
    # 4. Detect alerts
    # detector = AlertDetection(model.get_residuals(), thresholds={})
    # alerts = detectpr.detect_alerts()
    #
    # 5. Save results
    # (to CSV or DB)
    pass
if __name__ == '__main__':
    main()