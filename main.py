from models.user import Cliente
from dao.factory import get_dao_from_config

def main():
    dao = get_dao_from_config("config.json")
<<<<<<< HEAD
    
=======

    dao.add_user(User(None, "Juan perez", "juan@example.com"))
    dao.add_user(User(None, "maria Martinez", "maria@example.com"))
    dao.add_user(User(None, "alejandra Lopez", "alejandra@example.com"))
   
>>>>>>> e5af6c8370166f64643b32dbc65876391b5c7dc7

    print("Usuarios almacenados:")
    for u in dao.get_all_users():
        print(u)

if __name__ == "__main__":
    main()
