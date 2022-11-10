DATA = [
    {
        'type': 'cm',
        'key': 1,
        'pow': -2,
    },
    {
        'type': 'km',
        'key': 2,
        'pow': 3,
    },
    {
        'type': 'dm',
        'key': 3,
        'pow': -1,
    },
    {
        'type': 'm',
        'key': 4,
        'pow': 0,
    },
    {
        'type': 'mm',
        'key': 5,
        'pow': -3,
    }
]


def run(option1, option2, number):
    for item in DATA:
        if item.get('key') == option1:
            pow1 = item.get('pow')
    for item in DATA:
        if item.get('key') == option2:
            pow2 = item.get('pow')
    return number * 10**-(pow2-pow1)
