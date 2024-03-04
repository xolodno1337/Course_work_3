import json
from datetime import datetime


def load_operation(file):
    """Преобразовывает формат JSON в словарь."""
    with open(file, 'r', encoding='utf-8') as f:
        operation = json.load(f)
        return operation


def operation_filter(*operations):
    """Функция фильтрует по выполненным операциям(EXECUTED)."""
    executed_operations = []
    for operation in operations:
        if operation.get('state') == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations


def sort_operation(*operations):
    """Функция сортирует операции по дате."""
    return sorted(operations, key=lambda x: x['date'], reverse=True)


def format_date(date_str):
    """Функция переводит в необходимый формат даты."""
    dt = datetime.fromisoformat(date_str)
    return dt.strftime('%d.%m.%Y')


def format_operation(operation):
    """Функция выводит на экран выполненные операции в формате <дата перевода> <описание перевода>."""
    print(format_date(operation['date']), operation['description'])


def mask_account_number(operations, key):
    """Функция маскировки"""
    mask_account = operations.get(key, 'Открытие вклада')
    if 'Счет' in mask_account:
        check, number = mask_account.split()
        return check + ' **' + number[-4:]
    elif mask_account == 'Открытие вклада':
        return 'Открытие вклада'
    else:
        account = mask_account.split()
        number = account[-1]
        mask_number = number[:4] + ' ' + number[4:6] + '**' + ' **** ' + number[-4:]
        account.pop()
        return ' '.join(account) + ' ' + mask_number
