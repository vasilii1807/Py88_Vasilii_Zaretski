names = ("Petr", "Vasya", "Anton", "Vlad", "Masha", "Alexey", "Danila", "Max", "Olya", "Yan", "Yra")

print(*filter(lambda x: len(x) > 4, names))
print(*filter(lambda x: len(x) <= 3, names))
