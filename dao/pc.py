import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DAKA09;'  # Ajusta según tu instancia
        'DATABASE=ComercialSimple;'
        'UID=sa;'
        'PWD=*Sugacel0953'
    )
    print("Conexión exitosa!")
except pyodbc.Error as ex:
    print(f"Error al conectar: {ex}")