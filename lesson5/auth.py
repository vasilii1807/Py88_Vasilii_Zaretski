name_1, name_2, name_3, name_4, name_5 = "Dima", "Ivan", "Pavel", "Petr", "Denis"
names = (name_1, name_2, name_3, name_4, name_5)
name_pass_1, name_pass_2, name_pass_3, name_pass_4, name_pass_5 = "dima123", "ivan123", "pavel123", "petr123", "denis123"
usr_pass = [name_pass_1, name_pass_2, name_pass_3, name_pass_4, name_pass_5]

def get_name():
    while True:
        user_name = input("Введите ваше имя: ").title()
        if user_name == 'Exit':
            break
        elif user_name not in names:
            print(f'Name {user_name} not found. Try again!')
        else:
            break
    return user_name
def get_password():
    user_password = input("Введите ваш пароль: ")
    return user_password

def check_password(user_name,user_password):
    while True:
        if user_password == usr_pass[names.index(user_name)]:
            print(f"Hey {user_name}")
            break
        else:
            print("Authentication Error. Check name or password! ")
            check_password(get_name(),get_password())
            break

check_password(get_name(),get_password())
