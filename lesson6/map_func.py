num = [i for i in range(15)]
even_odd = list(map(lambda x: "четное" if x % 2 == 0 else "нечетное", num))
result = {}
for i in num:
    result[i] = even_odd[i]
print(result)
