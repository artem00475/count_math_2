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
def get_interval(eq, accur):
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
        exist, a, b = check_interval(eq, a, b, accur)
        if exist:
            return a, b
        print("На данном интервале нет корней. Повторите ввод")


def check_interval(eq, a, b, accur):
    k = 0
    index = a
    prev = func(eq, a)
    intervals = [a]
    while index < b + accur:
        if prev * func(eq, index) < 0:
            k += 1
            intervals.append(index)
            prev = func(eq, index)
        index += accur
    intervals[-1] = b
    if k == 0:
        return False, 0, 0
    elif k > 1:
        print("На интервале", k, "корней.")
        print("Выберите интервал:")
        for i in range(k):
            print(f"{i+1}. [{round(intervals[i], 5)}, {round(intervals[i+1], 5)}]")
        val = enter_value(1, k)
        return True, intervals[val-1], intervals[val]
    else:
        return True, a, b


# Вывод таблицы с итерациями в потока вывода
def print_table(table):
    for c in table[0]:
        print(c, end='    ')
    print()
    for row in table[1:]:
        count = 0
        for c in row:
            if count == 0:
                print(c, end='    ')
                count += 1
            else:
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