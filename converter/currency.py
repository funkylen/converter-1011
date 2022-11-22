DATA = [
    {
        'type': 'RUB',
        'key': 1,
        'ratio': 1,
    },
    {
        'type': 'USD',
        'key': 2,
        'ratio': 60.2179,
    },
    {
        'type': 'EUR',
        'key': 3,
        'ratio': 61.5416,
    },
    {
        'type': 'CNY',
        'key': 4,
        'ratio': 8.44637,
    }
]


def run(option1, option2, number):
    for item in DATA:
        if item.get('key') == option1:
            ratio1 = item.get('ratio')
    for item in DATA:
        if item.get('key') == option2:
            ratio2 = item.get('ratio')
    return number*(ratio1/ratio2)
