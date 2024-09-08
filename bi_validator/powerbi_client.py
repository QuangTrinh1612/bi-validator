from config import WORKSPACE_NAME, DATASET_NAME
from sys import path
import pandas as pd

path.append("C:\\Program Files\\Microsoft.NET\\ADOMD.NET\\160")
from pyadomd import Pyadomd

class PowerBIConnection:
    def __init__(self):
        """Initialize the PowerBIConnection class by loading environment variables."""
        self.workspace_name = WORKSPACE_NAME
        self.dataset_name = DATASET_NAME
        
        if not all([self.workspace_name, self.dataset_name]):
            raise EnvironmentError("Missing environment variables for Power BI connection.")
        
        self.connection = self.connect()
        
    def connect(self):
        conn_str= f"Provider=MSOLAP;Data Source=powerbi://api.powerbi.com/v1.0/myorg/{self.workspace_name};Initial Catalog={self.dataset_name};"
        return Pyadomd(conn_str)

    def get_dax_result(self, dax_query: str) -> pd.DataFrame:
        self.connection.open()
        result = self.connection.cursor().execute(dax_query)
        df = pd.DataFrame(result.fetchall())
        self.connection.close()
        return df
    
# Example usage
if __name__ == "__main__":
    try:
        # Initialize the connection class
        power_bi_conn = PowerBIConnection()
        
        # Example to retrieve DAX results
        df = power_bi_conn.get_dax_result("""
            EVALUATE 'DIM - REGION'
        """)
        
        print(df)

    except Exception as e:
        print(f"Error: {e}")
