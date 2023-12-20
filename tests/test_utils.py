from src.utils import number_format, date_format, get_data, get_sorted_list, get_filtered_data
import json
from config import ROOT_DIR
import os
def test_number_format():
    assert number_format("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert number_format("Счет 35383033474447895560") == "Счет **5560"

def test_date_format():
    assert date_format("2018-06-30") == "30.06.2018"

def test_get_data():
    path = os.path.join(ROOT_DIR, "tests", "test_operation.json")
    assert get_data(path) == [1, 2, 3]

def test_get_sorted_list():
    data = ["2018-03-23", "2019-08-26", "2019-07-03", "2020-07-03"]
    assert get_sorted_list(data) == ["2020-07-03", "2019-08-26", "2019-07-03", "2018-03-23"]

def test_get_filtered_data():
    dictionary = [
        {
            "id": 86608620,
            "state": "EXECUTED",
            "date": "2019-08-16T04:23:41.621065",
            "operationAmount": {
                "amount": "6004.00",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "MasterCard 8826230888662405",
            "to": "Счет 96119739109420349721"
        },
        {
            "id": 232222017,
            "state": "EXECUTED",
            "date": "2018-07-06T22:32:10.495465",
            "operationAmount": {
                "amount": "37160.27",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 4062745111784804",
    "to": "Maestro 8602249654751155"
    },}]
    assert get_filtered_data(dictionary) == ["2019-08-16"]
