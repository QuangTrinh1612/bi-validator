import pandas as pd
from sys import path

path.append("C:\\Program Files\\Microsoft.NET\\ADOMD.NET\\160")

from pyadomd import Pyadomd

model_name = '7933c335-cbab-4901-8727-2f2fbf355ef8'
port_number = 'localhost:59122'

connection_str = f"Provider=MSOLAP;Data Source={port_number};Catalog={model_name};"

dax_query = "EVALUATE 'Dim - Department'"

con = Pyadomd(connection_str)
con.open()
result = con.cursor().execute(dax_query)
df = pd.DataFrame(result.fetchone())
print(df)
con.close()