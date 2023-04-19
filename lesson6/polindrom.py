words = ("человек", "шалаш", "работа", "заказ", "день", "мадам")
print(*filter(lambda x: x == x[::-1], words))
