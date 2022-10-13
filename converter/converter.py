import prompt

CM_IN_M = 100

OPTION_CM_TO_M = 1
OPTION_M_TO_CM = 2


def convert():
    option = prompt.integer("Выберите вариант конвертирования: \n 1. см -> м\n 2. м -> см\n")

    number = prompt.real("Введите число: ")

    if option == OPTION_CM_TO_M:
        result = number / CM_IN_M 
        print(number, 'см', '=', result, 'м')

    elif option == OPTION_M_TO_CM:
        result = number * CM_IN_M
        print(number, 'м', '=', result, 'cм')

    else:
        raise 'Неизвестный тип'
