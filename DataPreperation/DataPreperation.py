class DataPreperation:
    def __init__(self, data):
        self.data = data
        self.prepared_data = None

    def clean_data(self):
        # TODO: implement data cleaning login (dropping NaN, potentially removing 0's)
        pass

    def transform_data(self):
        # TODO implement scaling/normalization or standardization (MinmaxScaler, StandardScaler)
        pass

    def get_prepared_data(self):
        # TODO: call clean + transform, then return
        pass

