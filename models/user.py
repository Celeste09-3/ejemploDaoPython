class User:
    def __init__(self, user_id: int | None, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User({self.user_id}, '{self.name}', '{self.email}')"
class Cliente:
    def __init__(self, id_cliente: int | None, nombre: str, correo_electronico: str):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo_electronico = correo_electronico

    def __repr__(self):
        return f"Cliente({self.id_cliente}, '{self.nombre}', '{self.correo_electronico}')"
