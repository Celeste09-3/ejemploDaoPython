import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=master;"
    "UID=sa;"
    "PWD=StrongP@ssword123;"
    "TrustServerCertificate=yes;"
)
print("✅ Conexión exitosa a SQL Server")
conn.close()