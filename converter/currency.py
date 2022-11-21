DATA2 = [
    {
        'type': 'RUB',
        'key': 1,
        'exchange_rate': 1,
    },
    {
        'type': 'USD',
        'key': 2,
        'exchange_rate': 60.2179,
    },
    {
        'type': 'EUR',
        'key': 3,
        'exchange_rate': 61.5416,
    },
    {
        'type': 'CNY',
        'key': 4,
        'exchange_rate': 8.44637,
    }
]


def run2(option1, option2, number):
    for item in DATA2:
        if item.get('key') == option1:
            exchange_rate1 = item.get('exchange_rate')
    for item in DATA2:
        if item.get('key') == option2:
            exchange_rate2 = item.get('exchange_rate')
    return number * exchange_rate1 / exchange_rate2 