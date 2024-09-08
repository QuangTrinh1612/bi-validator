import pandas as pd
from sys import path

path.append("C:\\Program Files\\Microsoft.NET\\ADOMD.NET\\160")

from pyadomd import Pyadomd

workspaceName = ''
datasetName = ''

connection_str= f"Provider=MSOLAP;Data Source=powerbi://api.powerbi.com/v1.0/myorg/{workspaceName};Initial Catalog={datasetName};"

dax_query = "EVALUATE 'DIM - REGION'"

con = Pyadomd(connection_str)
con.open()
result = con.cursor().execute(dax_query)
df = pd.DataFrame(result.fetchone())
print(df)
con.close()