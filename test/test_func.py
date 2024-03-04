from pathlib import Path

from src.func import load_operation, operation_filter, mask_account_number

BASE_DIR = Path(__file__).resolve().parent.parent
OPERATION_PATH = BASE_DIR.joinpath('operations.json')


def test_load_operation():
    assert type(load_operation(OPERATION_PATH)) == list


def test_operation_filter():
    operations = load_operation(OPERATION_PATH)
    executed_operations = operation_filter(*operations)
    for operation in executed_operations:
        assert operation.get("state") == "EXECUTED"


def test_mask_account_number():
    operations = load_operation(OPERATION_PATH)
    assert mask_account_number(operations[0], 'from') == 'Maestro 1596 83** **** 5199'
    assert mask_account_number(operations[0], 'to') == 'Счет **9589'
    assert mask_account_number(operations[3], 'Открытие вклада') == 'Открытие вклада'
