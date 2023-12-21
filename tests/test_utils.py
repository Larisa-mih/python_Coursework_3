from config import TEST_OPERATIONS_PATH, TEST_OPERATIONS_SORTED_PATH, TEST_OPERATIONS_FILTERED_PATH
from src.utils import (number_format, data_format, get_data, get_sorted_list,
                       get_filtered_data, formate_operations_for_output)
import json

def test_number_format():
    assert number_format("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert number_format("Счет 35383033474447895560") == "Счет **5560"


def test_data_format():
    assert data_format("2018-06-30") == "30.06.2018"


def test_get_data():
    assert get_data(TEST_OPERATIONS_PATH) == [1, 2, 3]


def test_get_sorted_list():
    with open(TEST_OPERATIONS_SORTED_PATH) as file:
        data = json.load(file)
    assert get_sorted_list(data) == [{"date": "2020-07-03"},
                                     {"date": "2019-08-26"},
                                     {"date": "2019-07-03"},
                                     {"date": "2018-03-23"}]


def test_get_filtered_data():
    with open(TEST_OPERATIONS_FILTERED_PATH, encoding="UTF-8") as file:
        data = json.load(file)
    assert get_filtered_data(data) == [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
          "amount": "31957.58",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
      }]


def test_formate_operations_for_output():
    data_1 = {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
              "amount": "31957.58",
              "currency": {
                "name": "руб.",
                "code": "RUB"
              }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
    }
    assert formate_operations_for_output(data_1) == ('\n26.08.2019 Перевод организации\n'
                                                     'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                                                     '31957.58 руб.')
    data_2 = {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
              "amount": "48223.05",
              "currency": {
                "name": "руб.",
                "code": "RUB"
              }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
          }
    assert formate_operations_for_output(data_2) == ('\n23.03.2018 Открытие вклада\n'
                                                     'Anonymous -> Счет **2431\n'
                                                     '48223.05 руб.')
