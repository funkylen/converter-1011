import prompt
from converter.currency import run, DATA
def input_option(message, array):
    option = str(input(message))

    while option not in array:
        option = str(input(message))
    return option


def input_info():

    array = [item.get('type') for item in DATA]

    message = "Выберите валюту, из которой собираетесь переводить средства:\n"
    for item in DATA:
        type = item.get('type')

        message += f"{type}\n"

    option1 = input_option(message, array)

    message = "Выберите валюту, в которую переводите средства :\n"
    for item in DATA:
        type = item.get('type')

        message += f"{type}\n"

    option2 = input_option(message, array)

    number = prompt.real('введите число')
    result = run(option1,option2,number)

    print(result)


def main():

    input_info()
    
if __name__ == '__main__':
    main()
