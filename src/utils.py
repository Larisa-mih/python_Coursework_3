import json
import datetime

def get_data(path):
    """Функция считывания данных из файла json"""
    with open(path, encoding='utf-8') as file:
        data_dict = json.load(file)
        return data_dict

def get_filtered_data(data_dict):
    """Функция фильтрации по "EXECUTED"""
    date_list = []
    for data in data_dict:
        if "from" not in data:
            continue
        elif data["state"] == "EXECUTED":
            date_list.append(data["date"][0:10])
    return date_list

def get_sorted_list(date_list):
    """Функция сортировки данных и выбор 5 последних"""
    sorted_list = sorted(date_list, reverse=True)[0:5]
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

def date_format(date):
    """Фугкция перевода формата даты"""
    format_date = ".".join(date.split("-")[::-1])
    return format_date
    """Второй вариант с помощью datetime"""
# datetime.datetime.fromisoformat("2019-08-26T10:50:58.294041")

    """Третий вариант"""
# my_date = "2019-08-26T10:50:58.294041"
# my_date_splitter = my_date.split('T')
# date = my_date_splitter(0)
# date_parts = date.split('-')
# reversed_parts = date_parts[::-1]
# to_return = '.'.join(reversed_parts)