def analyze(number):
    for i in number:
        value = i.isdigit()
        if value is True:
            print(f"Вы ввели положительное целое число: {i}")
        elif value is False:
            try:
                y = float(i)
                if y % 1 != 0:
                    if y < 0:
                        print(f"Вы ввели отрицательное дробное число: {y}")
                    else:
                        print(f"Вы ввели положительное дробное число: {y}")
                elif y % 1 == 0:
                    if y < 0:
                        print(f"Вы ввели отрицательное целое число: {i}")
            except ValueError:
                print(f"Вы ввели не корректное число: {i}")


numbers = ["-6.7", "-5", "5.4r", "-.777"]
analyze(numbers)
