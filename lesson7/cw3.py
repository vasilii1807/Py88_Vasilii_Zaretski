import json
data = {123456: ("Petr", 30), 234567: ("Vasya", 25), 345678: ("Max", 26),
        456789: ("Vlad", 24), 567891: ("Dima", 34), 678912: ("Alexey", 29)}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
