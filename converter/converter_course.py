DATA = [
    {
        'currency': 'RUB',
        'course': 1,
    },
    {
        'currency': 'USD',
        'course': 60.2179,
    },
    {
        'currency': 'EUR',
        'course': 61.5416
    },
    {
        'currency': 'CNY',
        'course': 84.4637,
    },
]


def run(from_currency, to_currency, value):
    for item in DATA:
        if item.get('currency').lower() == from_currency:
            from_course = item.get('course')
        if item.get('currency').lower() == to_currency:
            to_course = item.get('course')
    return (value * from_course) / to_course