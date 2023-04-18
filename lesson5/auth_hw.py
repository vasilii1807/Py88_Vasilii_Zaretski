usr_pass = {"Dima":"dima123", "Ivan":"ivan123", "Pavel":"pavel123", "Petr":"petr123", "Denis":"denis123"}

def get_name():
    while True:
        user_name = input("Введите ваше имя: ").title()
        if user_name == 'Exit':
            break
        elif user_name not in usr_pass:
            print(f'Name {user_name} not found. Try again!')
        else:
            break
    return user_name

def get_password():
    user_password = input("Введите ваш пароль: ")
    return user_password

def check_password(user_name,user_password):
    while True:
        if user_password == usr_pass[user_name]:
            print(f"Hey {user_name}")
            break
        else:
            print("Authentication Error. Check name or password! ")
            check_password(get_name(),get_password())
            break

check_password(get_name(),get_password())