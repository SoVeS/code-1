import math

sign = input("Введите знак математической операции: + / - / * / : / ** / ! / sqrt / sin / cos / tg: ")

if sign == "+" or sign == "-" or sign == "*" or sign == ":" or sign == "**":
    marker = 1
    while marker > 0:
        marker = 0
        num1 = input()
        num2 = input()
        for elem in num1:
            if elem != "0" and elem != "1" and elem != "2" and elem != "3" and elem != "4" and elem != "5" and elem != "6" and elem != "7" and elem != "8" and elem != "9" and elem != ".":
                marker += 1
        for elem in num2:
            if elem != "0" and elem != "1" and elem != "2" and elem != "3" and elem != "4" and elem != "5" and elem != "6" and elem != "7" and elem != "8" and elem != "9" and elem != ".":
                marker += 1
        if marker != 0:
            print("Некореектный ввод!")
    num1 = float(num1)
    num2 = float(num2)

elif sign == "!" or sign == "sqrt" or sign == "sin" or sign == "cos" or sign == "tg":
    marker = 1
    while marker > 0:
        marker = 0
        num1 = input()
        for elem in num1:
            if elem != "0" and elem != "1" and elem != "2" and elem != "3" and elem != "4" and elem != "5" and elem != "6" and elem != "7" and elem != "8" and elem != "9" and elem != ".":
                marker += 1
        if marker != 0:
            print("Некореектный ввод!")
    num1 = float(num1)
else:
    print("Неизвестный знак, повторите попытку")

if sign == "+":
    print("Сумма равна:", num1 + num2)

elif sign == "-":
    print("Разность равна:", num1 - num2)

elif sign == "*":
    print("Произведение равно:", num1 * num2)

elif sign == ":":
    if num2 == 0:
        print("Деление на 0!!!")
    else:
       print("Частное равно:", num1 / num2)

elif sign == "**":
    print(num1, "В степени", num2, "Равен:",  num1**num2)

elif sign == "!":
    if num1 % 1 != 0:
        print("Операцию выполнить невозможно!")
    else:
        num1 = int(num1)
        result = 1
        for i in range(1, num1 + 1):
            result *= i
        print("Факториал числа", num1, "Равен:", result)

elif sign == "sqrt":
    print("Квадратный корень числа", num1, "Равен:", math.sqrt(num1))

elif sign == "sin":
    print("Синус Угла", num1, "в радианах равен:", math.sin(num1))

elif sign == "cos":
    print("Косинус Угла", num1, "в радианах равен:", math.cos(num1))

elif sign == "tg":
    if math.cos(num1) == 0:
        print("Невозможно выполнить операцию, косинус вводимого числа равен 0")
    else:
        print("Тангенс Угла", num1, "равен:", math.sin(num1) / math.cos(num1))
