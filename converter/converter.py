import prompt

CM_IN_M = 100
MM_IN_CM = 10

OPTION_CM_TO_M = 1
OPTION_M_TO_CM = 2
OPTION_CM_TO_MM = 3


def convert():
    option = prompt.integer(
        "Выберите вариант конвертирования: \n 1. см -> м\n 2. м -> см\n 3. см -> мм\n")

    number = prompt.real("Введите число: ")

    if option == OPTION_CM_TO_M:
        result = number / CM_IN_M
        print(number, 'см', '=', result, 'м')

    elif option == OPTION_M_TO_CM:
        result = number * CM_IN_M
        print(number, 'м', '=', result, 'cм')

    elif option == OPTION_CM_TO_MM:
        result = number * MM_IN_CM
        print(number, 'см', '=', result, 'мм')

    else:
        raise 'Неизвестный тип'
