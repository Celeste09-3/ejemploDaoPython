from models.user import Cliente
from dao.factory import get_dao_from_config

def main():
    dao = get_dao_from_config("config.json")
    

    print("Usuarios almacenados:")
    for u in dao.get_all_users():
        print(u)

if __name__ == "__main__":
    main()
