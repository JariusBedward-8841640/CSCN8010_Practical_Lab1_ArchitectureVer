import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

class DataExtraction:
    def __init__(self):
        load_dotenv()
        self.db_url = os.getenv("DATABASE_URL")
        self.engine = create_engine(self.db_url)


    def connect(self, query: str) -> pd.DataFrame:

        return pd.read_sql(query, self.engine)

