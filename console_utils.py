from func_utils import *


# Считывание числа с клавиатуры
def enter_value(b, c):
    a = 0
    while a < b or a > c:
        try:
            a = int(input())
            if a < b or a > c:
                raise ValueError
        except ValueError:
            print("Повторите ввод")
    return a


# Считывание точности с клавиатуры
def get_accuracy():
    print("Введите желаемую точность в виде десятичной дроби")
    accuracy = False
    while not accuracy:
        try:
            accuracy = float(input())
            if accuracy <= 0 or accuracy >= 1:
                accuracy = False
                raise ValueError
        except ValueError:
            print("Повторите ввод")
    return accuracy


# Считывание интервала для нахождения корня с клавиатуры
def get_interval(eq):
    while True:
        print("Введите левую границу интервала")
        flaga = False
        a = 0
        while not flaga:
            try:
                a = float(input())
                flaga = True
            except ValueError:
                print("Повторите ввод")
        print("Введите правую границу интервала")
        flagb = False
        b = 0
        while not flagb:
            try:
                b = float(input())
                flagb = True
            except ValueError:
                print("Повторите ввод")
        der = derivative(eq)
        if func(eq, a) * func(eq, b) > 0 and func(der, a) * func(der, b / 2) > 0:
            print("На данном интервале нет корней. Повторите ввод")
        elif func(der, a) * func(der, b / 2) < 0:
            print("На интервале может содержаться несколько корней")
            return a, b
        else:
            return a, b


# Вывод таблицы с итерациями в потока вывода
def print_table(table):
    for c in table[0]:
        print(c, end='    ')
    print()
    for row in table[1:]:
        for c in row:
            if c >= 0:
                print(' %.5f' % c, end='    ')
            else:
                print('%.5f' % c, end='    ')
        print()


# Вывод результата в поток вывода
def print_to_output(table, x, count, fx):
    print_table(table)
    print("Корень: %.5f" % x)
    print("Число итераций:", count + 1)
    print("Значение функции: %.5f" % fx)


# Считывание начального приближения из консоли
def get_initial_approximation(eq):
    print("Введите начальное приближение корня")
    flaga = False
    a = 0
    while not flaga:
        try:
            a = float(input())
            flaga = True
        except ValueError:
            print("Повторите ввод")
    b1 = a - 0.5
    b2 = a + 0.5
    while True:
        if func(eq, a) * func(eq, b1) < 0:
            return a, b1
        elif func(eq, a) * func(eq, b2) < 0:
            return a, b2
        else:
            b1 -= 0.5
            b2 += 0.5
