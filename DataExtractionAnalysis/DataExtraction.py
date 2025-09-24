class DataExtraction:
    def __init__(self, db_url):
        self.db_url = db_url
        self.connection = None
        self.data = None


    def connect(self):
        #TODO: Implement database connection (using SQLAlchemy)
        pass

    def load_data(self):
        # TODO: implement query to fetch data from db
        pass