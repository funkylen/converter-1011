import prompt

CM_IN_M = 100
MM_IN_CM = 10


def convert():
    data = [
        {
            'from_type': 'cm',
            'to_type': 'm',
            'key': 1,
            'handler': lambda x: x / CM_IN_M,
        },
        {
            'from_type': 'm',
            'to_type': 'cm',
            'key': 2,
            'handler': lambda x: x * CM_IN_M,
        },
        {
            'from_type': 'cm',
            'to_type': 'mm',
            'key': 3,
            'handler': lambda x: x * MM_IN_CM,
        },
        {
            'from_type': 'mm',
            'to_type': 'cm',
            'key': 4,
            'handler': lambda x: x / MM_IN_CM,
        },
    ]

    message = "Выберите вариант конвертирования:\n"
    for item in data:
        key = item.get('key')
        from_type = item.get('from_type')
        to_type = item.get('to_type')

        message += f'{key}. {from_type} -> {to_type}' + "\n"

    option = prompt.integer(message)

    number = prompt.real("Введите число: ")

    for item in data:
        if item.get('key') == option:
            result = item.get('handler')(number)
            from_type = item.get('from_type')
            to_type = item.get('to_type')
            print(number, from_type, '=', result, to_type)
            return

    raise 'Неизвестный тип'
