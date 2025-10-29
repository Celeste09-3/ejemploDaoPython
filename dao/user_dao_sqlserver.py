import pyodbc
from models.user import Cliente
from dao.user_dao_base import UserDAOBase

class UserDAOSQLServer(UserDAOBase):
    def __init__(self, server, database, username, password, driver):
        self.conn = pyodbc.connect(
            f"DRIVER={{{driver}}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password}"
        )
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            IF NOT EXISTS (
                SELECT * FROM sysobjects WHERE name='Clientes' AND xtype='U'
            )
            CREATE TABLE Clientes (
                IdCliente INT IDENTITY(1,1) PRIMARY KEY,
                Nombre NVARCHAR(100) NOT NULL,
                CorreoElectronico NVARCHAR(100)
            )
        ''')
        self.conn.commit()

    def add_user(self, user: Cliente):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Clientes (Nombre, CorreoElectronico) VALUES (?, ?)",
            (user.nombre, user.correo_electronico)
        )
        self.conn.commit()

    def get_all_users(self) -> list[Cliente]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT IdCliente, Nombre, CorreoElectronico FROM Clientes")
        rows = cursor.fetchall()
        return [Cliente(row.IdCliente, row.Nombre, row.CorreoElectronico) for row in rows]
