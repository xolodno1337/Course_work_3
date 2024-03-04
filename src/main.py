from pathlib import Path
from src.func import load_operation, operation_filter, sort_operation, format_operation, mask_account_number
BASE_DIR = Path(__file__).resolve().parent.parent
OPERATION_PATH = BASE_DIR.joinpath('operations.json')


def main():
    operations = load_operation(OPERATION_PATH)
    executed_operation = operation_filter(*operations)
    sorted_operation = sort_operation(*executed_operation)
    last_operation = sorted_operation[:5]
    for i in last_operation:
        format_operation(i)
        to = mask_account_number(i, 'to')
        from_ = mask_account_number(i, 'from')
        print(f'{to} -> {from_}')
        print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])


if __name__ == '__main__':
    main()

