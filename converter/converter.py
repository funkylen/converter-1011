import prompt



def run():
    data = [
        {
            'type': 'cm',
            'key': 1,
            'pow' : -2,
        },
        {
            'type': 'km',
            'key': 2,
            'pow' : 3,
        },
        {
            'type': 'dm',
            'key': 3,
            'pow' : -1,
        },
        {
            'type': 'm',
            'key': 4,
            'pow' : 0,
        },
        {
            'type': 'mm',
            'key': 5,
            'pow' : -3,
        }
    ]



    message = "Выберите:\n"
    for item in data:
        type = item.get('type')
        key = item.get('key')
        
        message += f"{key}. {type}\n"
    

    option1 = prompt.integer(message)

    message = "Выберите :\n"
    for item in data:
        type = item.get('type')
        key = item.get('key')
        
        message += f"{key}. {type}\n"
    

    option2 = prompt.integer(message)

    number = prompt.real("Введите число: ")

    for item in data:
        if item.get('key') == option1:
            pow1 = item.get('pow')
    for item in data:
        if item.get('key') == option2:
            pow2 = item.get('pow')
    result = convert(number,pow1,pow2)
    print(result)
   

def convert(num,pow1,pow2):
    print(pow1,pow2)
    return num * 10**-(pow2-pow1)
