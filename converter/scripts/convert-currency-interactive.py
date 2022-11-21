import prompt
from converter.currency import run2, DATA2


def input_option2(message, array):
    option = prompt.integer(message)

    while option not in array:
        option = prompt.integer(message)
    return option


def user_input2():
    message = "Выберите валюту, из которой нужно перевести:\n"
    for item in DATA2:
        type = item.get('type')
        key = item.get('key')

        message += f"{key}. {type}\n"

    array = [item.get('key') for item in DATA2]

    option1 = input_option2(message, array)

    message = "Выберите валюту, в которую нужно перевести:\n"
    for item in DATA2:
        type = item.get('type')
        key = item.get('key')

        message += f"{key}. {type}\n"

    option2 = input_option2(message, array)

    number = prompt.real("Введите сумму: ")
    result = run2(option1, option2, number)
    print(result)


def main():
    user_input2()


if __name__ == '__main__':
    main()