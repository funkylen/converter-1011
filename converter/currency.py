DATA = [ 
    { 
        'type' : 'RUB',
        'currency': 1
    },
    {
        'type' : 'USD',
        'currency': 60.2179
    },
    {
        'type' : 'EUR',
        'currency': 61.5416
    },
    {
        'type' : 'CNY',
        'currency': 8.4637
    }
]



def run(option1,option2,number):
    for item in DATA:
        if item.get('type') == option1:
            currency1 = item.get('currency')
    for item in DATA:
        if item.get('type') == option2:
            currency2 = item.get('currency')
    return number*currency1/currency2