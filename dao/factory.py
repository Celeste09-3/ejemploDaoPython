import json
import pandas as pd
from dao.user_dao_mysql import UserDAOMySQL
from dao.user_dao_txt import UserDAOTxt
from dao.user_dao_xml import UserDAOXML
from dao.user_dao_sqlserver import UserDAOSQLServer

def get_dao_from_config(config_path="config.json"):
    with open(config_path, "r") as f:
        config = json.load(f)

    dao_type = config["dao_type"].lower()

    if dao_type == "mysql":
        mysql_conf = config["mysql"]
        return UserDAOMySQL(
            host=mysql_conf["host"],
            user=mysql_conf["user"],
            password=mysql_conf["password"],
            database=mysql_conf["database"]
        )

    elif dao_type == "txt":
        return UserDAOTxt(config["txt"]["filepath"])

    elif dao_type == "xml":
        return UserDAOXML(config["xml"]["filepath"])

    elif dao_type == "sqlserver":
        sql_conf = config["sqlserver"]
        dao = UserDAOSQLServer(
            server=sql_conf["server"],
            database=sql_conf["database"],
            username=sql_conf["username"],
            password=sql_conf["password"],
            driver=sql_conf.get("driver", "ODBC Driver 17 for SQL Server")
        )

        # Exportar automáticamente a Excel
        clientes = dao.get_all_users()
        df = pd.DataFrame([{
            "IdCliente": c.id_cliente,
            "Nombre": c.nombre,
            "CorreoElectronico": c.correo_electronico
        } for c in clientes])
        df.to_excel("clientes.xlsx", index=False)
        print("✅ Archivo 'clientes.xlsx' generado automáticamente desde factory.py")

        return dao

    else:
        raise ValueError(f"Tipo de DAO desconocido: {dao_type}")

