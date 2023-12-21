from config import OPERATIONS_PATH
from src.utils import get_data, get_filtered_data, get_sorted_list, formate_operations_for_output


def main():
    all_operations = get_data(OPERATIONS_PATH)
    filtered_operations = get_filtered_data(all_operations)
    sorted_operations = get_sorted_list(filtered_operations)
    last_five_operations = sorted_operations[:5]
    for operation in last_five_operations:
        print(formate_operations_for_output(operation))


if __name__ == "__main__":
    main()
