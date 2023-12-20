import json
from utils import number_format, date_format

with open("C:/Users/Лариса/PycharmProjects/python_Coursework_3/src/operations.json", encoding='utf-8') as file:
    data_dict = json.load(file)
date_list = []
for data in data_dict:
    if "from" not in data:
        continue
    elif data["state"] == "EXECUTED":
        date_list.append(data["date"][0:10])
    sorted_list = sorted(date_list, reverse=True)[0:5]

for i in range(5):
     for data in data_dict:
         if "date" not in data or "from" not in data:
             continue
         elif data["date"][0:10] == sorted_list[i]:
             date_name = data["date"][0:10]
             description_name = data["description"]
             from_name = data["from"]
             to_name = data["to"]
             amount = data["operationAmount"]["amount"]
             currency = data["operationAmount"]["currency"]["name"]

             print(f"{date_format(date_name)} {description_name}\n"
                   f"{number_format(from_name)} -> {number_format(to_name)}\n"
                   f"{amount} {currency}\n"
                   f"")