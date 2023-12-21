import json
import datetime

def get_data(path):
    """Функция считывания данных из файла json"""
    with open(path, encoding='utf-8') as file:
        data_dict = json.load(file)
        return data_dict

def get_filtered_data(data_dict):
    """Функция фильтрации по "EXECUTED"""
    data_list = []
    for data in data_dict:
        if data == {}:
            continue
        elif data["state"] == "EXECUTED":
            data_list.append(data)
    return data_list


def get_sorted_list(data_list):
    """Функция сортировки данных"""
    sorted_list = sorted(data_list, key=lambda operation: operation["date"], reverse=True)
    return sorted_list

def number_format(name):
    """Функция маскировки счета и карты"""
    if "счет" in name.lower():
        name_list = name.split()
        format_number = name_list[0] + " " + "**" + name_list[-1][-4:]
        return format_number
    else:
        name_list = name.split()
        name_operation = name_list[0:-1]
        format_number = " ".join(name_operation) + " " + name_list[-1][0:4] + " " + name_list[-1][4:6] + "**" + " " + "****" + " " + name_list[-1][-4:]
        return format_number

def data_format(data):
    """Фугкция перевода формата даты"""
    format_data = ".".join(data[0:10].split("-")[::-1])
    return format_data
    """Второй вариант с помощью datetime"""
# datetime.datetime.fromisoformat("2019-08-26T10:50:58.294041")

    """Третий вариант"""
# my_date = "2019-08-26T10:50:58.294041"
# my_date_splitter = my_date.split('T')
# date = my_date_splitter(0)
# date_parts = date.split('-')
# reversed_parts = date_parts[::-1]
# to_return = '.'.join(reversed_parts)

def formate_operations_for_output(data):
    data_name = data_format(data["date"])
    description_name = data["description"]
    if data.get("from"):
        from_name = number_format(data["from"])
        to_name = number_format(data["to"])
    else:
        from_name = "Anonymous"
        to_name = number_format(data["to"])
    amount = data["operationAmount"]["amount"]
    currency = data["operationAmount"]["currency"]["name"]
    info_operation = (f"\n{data_name} {description_name}\n"
                      f"{from_name} -> {to_name}\n"
                      f"{amount} {currency}")
    return info_operation