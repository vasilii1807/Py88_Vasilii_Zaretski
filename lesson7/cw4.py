import json
import csv
with open("data_file.json", "r") as read_file:
    data= json.loads(read_file.read())
    print(data)
    with open("classmates.csv", "w") as write_file:
        writer = csv.writer(write_file, delimiter= ',')
        headers = [' '] + [f'person {i}' for i in range(1, len(data) + 1)]
        writer.writerow(headers)
        _id = ["id"] + [i for i in data]
        writer.writerow(_id)
        _name = ["name"] + [j[0] for i, j in data.items()]
        writer.writerow(_name)
        _age = ["age"] + [j[1] for i, j in data.items()]
        writer.writerow(_age)
        _phone = ["phone"]
        writer.writerow(_phone)
