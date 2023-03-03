import matplotlib.pyplot as plt
import numpy as np
from sympy import *


#Отображения графика уравнения
def show_graph(a, b, num):
    x = np.arange(a, b + 0.01, 0.01)
    if num == 1:
        plt.plot(x, x ** 3 - 0.77 * x ** 2 - 1.251 * x + 0.43)
    elif num == 2:
        plt.plot(x, x ** 2 - x + 4)
    elif num == 3:
        plt.plot(x, 20 * np.cos(x) + x ** 2)
    plt.grid(True)
    plt.show()

#Отображения графика системы уравнений
def show_system_graph(num):
    var('x y')
    if num == 1:
        p1 = plot_implicit(Eq(0.1 * x ** 2 + x + 0.2 * y ** 2, 0.3), show=False, line_color='r')
        p2 = plot_implicit(Eq(0.2 * x ** 2 + y + 0.1 * x * y, 0.7), show=False)
    else:
        p1 = plot_implicit(Eq(0.2 * x ** 2 + x + 0.3 * y ** 2, 0.5), show=False, line_color='r')
        p2 = plot_implicit(Eq(0.4 * x ** 2 + y + 0.2 * x * y, 0.5), show=False)
    p2.extend(p1)
    p2.xscale = ''
    p2.show()


#Считывание числа с клавиатуры
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


#Считывание точности с клавиатуры
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


#Считывание интервала для нахождения корня с клавиатуры
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
        if func(eq, a) * func(eq, b) > 0 and func(der, a) * func(der, b/2) > 0:
            print("На данном интервале нет корней. Повторите ввод")
        elif func(der, a) * func(der, b/2) < 0:
            print("На интервале несколько корней")
            return a, b
        else:
            return a, b


#Вычисление значение функции
def func(eq, x):
    s = []
    symb = {'-': 0, '+': 0, '*': 1, '^': 2, 'cos': 3, 'sin': 3}
    for i in eq:
        if i not in symb:
            if i == 'x':
                s.append(x)
            else:
                s.append(i)
        else:
            if i == '-':
                a = s.pop()
                b = s.pop()
                s.append(b - a)
            elif i == '+':
                a = s.pop()
                b = s.pop()
                s.append(b + a)
            elif i == '*':
                a = s.pop()
                b = s.pop()
                s.append(b * a)
            elif i == '^':
                a = s.pop()
                b = s.pop()
                s.append(b ** a)
            elif i == 'cos':
                a = s.pop()
                s.append(np.cos(a))
            elif i == 'sin':
                a = s.pop()
                s.append(np.sin(a))
    return s[0]


def calculate_x_for_chord_method(a, b, fa, fb):
    return (a * fb - b * fa) / (fb - fa)


#Вывод таблицы с итерациями в потока вывода
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


#Вывод таблицы с итерациями в файл
def print_table_to_file(table, f):
    for c in table[0]:
        f.write(c + '    ')
    f.write('\n')
    for row in table[1:]:
        for c in row:
            if c >= 0:
                f.write(' %.5f    ' % c)
            else:
                f.write('%.5f    ' % c)
        f.write('\n')


#Вывод результата в поток вывода
def print_to_output(table, x, count, fx):
    print_table(table)
    print("Корень: %.5f" % x)
    print("Число итераций:", count + 1)
    print("Значение функции: %.5f" % fx)


#Вывод результата в файл
def print_to_file(table, x, count, fx):
    name = input("Введите имя файла: ")
    f = open(name, 'w')
    print_table_to_file(table, f)
    f.write("Корень: %.5f\n" % x)
    f.write("Число итераций:" + str(count + 1) + '\n')
    f.write("Значение функции: %.5f\n" % fx)
    f.close()


#Вывод результата
def print_result(table, x, count, fx):
    while True:
        t = input("Для вывода в консоль введите c, для сохранения в файл введите f: ")
        if t.split()[0] == "f":
            print_to_file(table, x, count, fx)
            break
        elif t.split()[0] == "c":
            print_to_output(table, x, count, fx)
            break
        else:
            print("Повторите ввод")


#Считывание исходных данных из файла
def get_data_from_file(a, eq):
    file = None
    while True:
        name = input("Введите имя файла: ")
        try:
            file = open(name)
            break
        except FileNotFoundError:
            print("Файл не найден")
    try:
        accuracy = float(file.readline())
        if accuracy <= 0 or accuracy >= 1:
            raise ValueError
        inp = file.readline().split()
        if a == 2:
            if len(inp) != 2:
                raise ValueError
            begin = float(inp[0])
            end = float(inp[1])
            der = derivative(eq)
            if func(eq, begin) * func(eq, end) > 0 and func(der, begin) * func(der, end/2) > 0:
                print("На данном интервале нет корней. Повторите ввод")
                return False, accuracy, begin, end
            elif func(der, begin) * func(der, end/2) < 0:
                print("На интервале несколько корней")
            return True, accuracy, begin, end
        if a == 1:
            begin = float(file.readline())
            b1 = begin - 0.5
            b2 = begin + 0.5
            while True:
                if func(eq, begin) * func(eq, b1) < 0:
                    return True, accuracy, begin, b1
                elif func(eq, begin) * func(eq, b2) < 0:
                    return True, accuracy, begin, b2
                else:
                    b1 -= 0.5
                    b2 += 0.5
    except ValueError:
        print("Некорректные данные")
        return False, 0, 0, 0


def chord_method(eq, num):
    print("Метод хорд")
    print("Откуда ввести данные? (k - клавиатура, f - файл)")
    type = ''
    while True:
        type = input()
        if type in ['f', 'k']:
            break
        else:
            print("Повторите ввод")
    table = [["   №   ", "   a   ", "   b   ", "   x   ", "  F(a)  ", "  F(b)  ", "  F(x)  ", "|x_n+1 - x_n|"]]
    if type == 'k':
        accuracy = get_accuracy()
        a, b = get_interval(eq)
        check = True
    else:
        check, accuracy, a, b = get_data_from_file(2, eq)
    if check:
        a0, b0 = a, b
        fa = func(eq, a)
        fb = func(eq, b)
        x = calculate_x_for_chord_method(a, b, fa, fb)
        fx = func(eq, x)
        deviation = min(abs(x - a), abs(x - b))
        table.append([0, a, b, x, fa, fb, fx, deviation])
        count = 0
        while accuracy < abs(fx) or accuracy < deviation:
            count += 1
            if fx * fa > 0:
                a = x
                fa = fx
            else:
                b = x
                fb = fx
            x = calculate_x_for_chord_method(a, b, fa, fb)
            fx = func(eq, x)
            deviation = min(abs(x - a), abs(x - b))
            table.append([count, a, b, x, fa, fb, fx, deviation])
        print_result(table, table[-1][3], count, fx)
        show_graph(a0 - 1, b0 + 1, num)


#Считывание начального приближения из консоли
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


def calculate_x_for_secant_method(a, b, fa, fb):
    return b - fb * (b - a) / (fb - fa)


def secant_method(eq, num):
    print("Метод секущих")
    print("Откуда ввести данные? (k - клавиатура, f - файл)")
    type = ''
    while True:
        type = input()
        if type in ['f', 'k']:
            break
        else:
            print("Повторите ввод")
    table = [["   №   ", "x_(k-1)", " x_k ", "x_(k+1)", "f(x_(k+1))", "|x_k+1 - x_k|"]]
    if type == 'k':
        accuracy = get_accuracy()
        a, b = get_initial_approximation(eq)
        check = True
    else:
        check, accuracy, a, b = get_data_from_file(1, eq)
    if check:
        a0, b0 = a, b
        fa = func(eq, a)
        fb = func(eq, b)
        x = calculate_x_for_secant_method(a, b, fa, fb)
        fx = func(eq, x)
        deviation = abs(x - b)
        count = 0
        table.append([count, a, b, x, fx, deviation])
        while accuracy < abs(fx) or accuracy < deviation:
            count += 1
            a = b
            b = x
            fa = fb
            fb = fx
            x = calculate_x_for_chord_method(a, b, fa, fb)
            fx = func(eq, x)
            deviation = abs(x - b)
            table.append([count, a, b, x, fx, deviation])
        print_result(table, table[-1][3], count, fx)
        show_graph(a0 - 1, b0 + 1, num)


#Вычисление производной функции
def derivative(eq):
    d = []
    container = []
    i = 0
    while i < len(eq):
        if str(eq[i]) == '^':
            degree = eq[i - 1]
            d.append(degree)
            d += container[:-1]
            d.append(degree - 1)
            d.append('^')
            d.append('*')
            container = []
        elif str(eq[i]) == 'sin':
            d += container
            container = []
            d.append('cos')
        elif str(eq[i]) == 'cos':
            d.append(-1)
            d += container
            container = []
            d.append('sin')
            d.append('*')
            if i < len(eq) - 2 and str(eq[i + 1]) == '*':
                d.append('*')
                i += 1
        elif str(eq[i]) == 'x' and i < len(eq) - 3 and str(eq[i + 2]) != "^" and str(eq[i + 1]) != "sin" \
                and str(eq[i + 1]) != "cos":
            d += container
            container = []
            d.append('x')
            d.append(0)
            d.append('^')
        else:
            container.append(eq[i])
        i += 1
    for i in container:
        if str(i) in ['^', '-', '+', '*']:
            d.append(i)
        else:
            break
    return d


def simple_iteration_method(eq, num):
    print("Метод простых итераций")
    print("Откуда ввести данные? (k - клавиатура, f - файл)")
    type = ''
    while True:
        type = input()
        if type in ['f', 'k']:
            break
        else:
            print("Повторите ввод")
    table = [["   №   ", " x_k ", "x_(k+1)", "f(x_(k+1))", "|x_k+1 - x_k|"]]
    if type == 'k':
        accuracy = get_accuracy()
        a, b = get_interval(eq)
        check = True
    else:
        check, accuracy, a, b = get_data_from_file(2, eq)
    if check:
        a0, b0 = a, b
        der = derivative(eq)
        alpha = -1 / max(abs(func(der, a)), abs(func(der, b)))
        phi = eq.copy()
        phi.append(alpha)
        phi.append('*')
        phi.append('x')
        phi.append('+')
        if abs(func(der, a)) >= abs(func(der, b)):
            x = a
        else:
            x = b
        derphi = derivative(phi[:-4]) + [alpha, '*', 1.0, '+']
        if abs(func(derphi, x)) < 1:
            phix = func(phi, x)
            deviation = abs(x - phix)
            fphi = func(eq, phix)
            count = 0
            table.append([count, x, phix, fphi, deviation])
            while accuracy < abs(fphi) or accuracy < deviation:
                count += 1
                x = phix
                phix = func(phi, x)
                fphi = func(eq, phix)
                deviation = abs(x - phix)
                table.append([count, x, phix, fphi, deviation])
            print_result(table, table[-1][2], count, fphi)
            show_graph(a0 - 1, b0 + 1, num)
        else:
            print("Условие сходимости не выполнено")


#Считывание начальных данных для решения системы
def get_system_start():
    while True:
        print("Введите начальное приближение первого корня")
        flaga = False
        a = 0
        while not flaga:
            try:
                a = float(input())
                flaga = True
            except ValueError:
                print("Повторите ввод")
        print("Введите начальное приближение второго корня")
        flagb = False
        b = 0
        while not flagb:
            try:
                b = float(input())
                flagb = True
            except ValueError:
                print("Повторите ввод")
        if a == b == 0:
            print("Некорректные приближения. Повторите ввод")
        else:
            return a, b


#Вычисление значения функции от двух переменных
def system_func(eq, x1, x2):
    s = []
    symb = ['-', '+', '*', '^']
    for i in eq:
        if i not in symb:
            if i == 'x_1':
                s.append(x1)
            elif i == 'x_2':
                s.append(x2)
            else:
                s.append(i)
        else:
            if i == '-':
                a = s.pop()
                b = s.pop()
                s.append(b - a)
            elif i == '+':
                a = s.pop()
                b = s.pop()
                s.append(b + a)
            elif i == '*':
                a = s.pop()
                b = s.pop()
                s.append(b * a)
            elif i == '^':
                a = s.pop()
                b = s.pop()
                s.append(b ** a)
    return s[0]


#Вычисление значения производной по первой переменной
def derivative_equation_by_x2(eq):
    d = []
    c = 0
    i = 0
    while i < len(eq) - 4:
        if str(eq[i]) == 'x_2':
            if str(eq[i - 2]) == 'x_1':
                if str(eq[i + 1]) == '*':
                    d.append(eq[i - 3])
                    d.append(eq[i - 2])
                    d.append('*')
                    if c > 0:
                        d.append(eq[i + 2])
            elif str(eq[i - 1]) == 'x_1':
                d.append(eq[i - 1])
                if c > 0:
                    d.append(eq[i + 2])
            elif i < len(eq) - 2 and str(eq[i + 2]) == "^":
                if str(eq[i + 3]) == '*':
                    d.append(eq[i - 1])
                    degree = eq[i + 1]
                    d.append(degree)
                    d.append(eq[i])
                    d.append(degree - 1)
                    d.append('^')
                    d.append('*')
                    d.append('*')
                    if c > 0:
                        d.append(eq[i + 4])
                else:
                    degree = eq[i + 1]
                    d.append(degree)
                    d.append(eq[i])
                    d.append(degree - 1)
                    d.append('^')
                    d.append('*')
                    if c > 0:
                        d.append(eq[i + 3])
            else:
                if str(eq[i + 1]) == "*":
                    d.append(eq[i - 1])
                    if c > 0:
                        d.append(eq[i + 2])
                else:
                    d.append(1.0)
                    if c > 0:
                        d.append(eq[i + 1])
            c += 1
        i += 1
    d.append(eq[-4])
    d.append(eq[-3])
    if eq[-2] == 'x_2':
        d.append(1.0)
        d.append(eq[-1])
    return d


#Вычисление значения производной по второй переменной
def derivative_equation_by_x1(eq):
    d = []
    c = 0
    i = 0
    while i < len(eq) - 4:
        if str(eq[i]) == 'x_1':
            if str(eq[i + 2]) == 'x_2':
                if str(eq[i + 3]) == '*':
                    d.append(eq[i - 1])
                    d.append(eq[i + 2])
                    d.append('*')
                    if c > 0:
                        d.append(eq[i + 4])
            elif str(eq[i + 1]) == 'x_2':
                d.append(eq[i + 1])
                if c > 0:
                    d.append(eq[i + 3])
            elif i < len(eq) - 2 and str(eq[i + 2]) == "^":
                if str(eq[i + 3]) == '*':
                    d.append(eq[i - 1])
                    degree = eq[i + 1]
                    d.append(degree)
                    d.append(eq[i])
                    d.append(degree - 1)
                    d.append('^')
                    d.append('*')
                    d.append('*')
                    if c > 0:
                        d.append(eq[i + 4])
                else:
                    degree = eq[i + 1]
                    d.append(degree)
                    d.append(eq[i])
                    d.append(degree - 1)
                    d.append('^')
                    d.append('*')
                    if c > 0:
                        d.append(eq[i + 3])
            else:
                if str(eq[i + 1]) == "*":
                    d.append(eq[i - 1])
                    if c > 0:
                        d.append(eq[i + 2])
                else:
                    d.append(1.0)
                    if c > 0:
                        d.append(eq[i + 1])
            c += 1
        i += 1
    d.append(eq[-4])
    d.append(eq[-3])
    if eq[-2] == 'x_1':
        d.append(1.0)
        d.append(eq[-1])
    return d


#Проверка сходимости системы
def check_convergence(stm, a, b):
    p1x1 = derivative_equation_by_x1(stm[0])
    p2x1 = derivative_equation_by_x1(stm[1])
    p1x2 = derivative_equation_by_x2(stm[0])
    p2x2 = derivative_equation_by_x2(stm[1])
    a = int(a)
    b = int(b)
    for x in range(min(a, 0), max(a, 0) + 1):
        for y in range(min(b, 0), max(b, 0) + 1):
            if abs(system_func(p1x1, x, y)) + abs(system_func(p1x2, x, y)) > 1:
                return False
            if abs(system_func(p2x1, x, y)) + abs(system_func(p2x2, x, y)) > 1:
                return False
    return True


#Разрешение уравнения относительно х
def express_x(eq, x):
    a = 1
    for i in range(len(eq) - 1):
        if eq[i] == x:
            if (i < len(eq) - 2 and eq[i + 2] != '^' and eq[i + 1] != 'x_2' and eq[i - 1] != 'x_1' and eq[i + 2] != 'x_2' and eq[i - 2] != 'x_1') or i >= len(eq) - 3:
                if eq[i + 1] == "*":
                    a = 1 / eq[i - 1]
                for j in range(i, len(eq)):
                    if eq[j] == '+':
                        a *= -1
                        break
                    elif eq[j] == '-':
                        break
                break
    eq.append(a)
    eq.append('*')
    eq.append(x)
    eq.append('+')
    return eq


def system_simple_iteration(stm):
    print("Метод простых итераций")
    accuracy = get_accuracy()
    system1 = [express_x(stm[0].copy(), 'x_1'), express_x(stm[1].copy(), 'x_2')]
    x1, x2 = get_system_start()
    if check_convergence(system1, x1, x2):
        x_1, x_2 = system_func(system1[0], x1, x2), system_func(system1[1], x1, x2)
        deviation1 = abs(x1 - x_1)
        deviation2 = abs(x2 - x_2)
        count = 1
        while accuracy < deviation1 or accuracy < deviation2:
            count += 1
            x1, x2 = x_1, x_2
            x_1, x_2 = system_func(system1[0], x1, x2), system_func(system1[1], x1, x2)
            deviation1 = abs(x1 - x_1)
            deviation2 = abs(x2 - x_2)
        print("Корни: %.5f ; %.5f" % (x_1, x_2))
        print("Число итераций: ", count)
        print("Погрешности: %.5f ; %.5f" % (deviation1, deviation2))
        if abs(system_func(stm[0], x_1, x_2)) <= accuracy and abs(system_func(stm[1], x_1, x_2)) <= accuracy:
            print("Решение корректно")
        else:
            print("Решение некорректно")
    else:
        print("Достаточное условие сходимости не выполняется")


#Преобразование уравнения в обратную польскую запись
def to_pol_format(st):
    a = st.split()
    res = []
    op = []
    symb = {'-': 0, '+': 0, '*': 1, '^': 2, 'cos': 3, 'sin': 3}
    for s in a:
        if s not in symb:
            if s != "x" and s != "x_1" and s != "x_2":
                res.append(float(s))
            else:
                res.append(s)
        else:
            if len(op) == 0:
                op.append(s)
            else:
                sm = op.pop()
                if symb[s] <= symb[sm]:
                    res.append(sm)
                    while len(op) > 0 and symb[s] <= symb[op[-1]]:
                        sm = op.pop()
                        res.append(sm)
                else:
                    op.append(sm)
                op.append(s)
    while len(op) > 0:
        res.append(op.pop())
    return res


work = True
while work:
    print("Выберите, что хотите решить:")
    print("1. Нелинейное уравнение")
    print("2. Система нелинейных уравнений")
    if enter_value(1, 2) == 1:
        f = open("equations.txt")
        count = int(f.readline())
        print("Выбирите нелинейное уравнение:")
        equations = []
        try:
            for x in range(1, count + 1):
                e = f.readline().replace('\n', '')
                s = str(x) + '. ' + e
                equations.append(to_pol_format(e))
                print(s)
            number = enter_value(1, count)
            equation = equations[number - 1]
            print("ВЫберите метод:")
            print("1. Метод хорд")
            print("2. Метод секущих")
            print("3. Метод простых итераций")
            method = enter_value(1, 3)
            if method == 1:
                chord_method(equation, number)
            elif method == 2:
                secant_method(equation, number)
            else:
                simple_iteration_method(equation, number)
        except ValueError:
            print("Ошибка в введенном уравнении")
    else:
        f = open("systems.txt")
        count = int(f.readline())
        print("Выберите систему нелинейных уравнений:")
        systems = []
        try:
            for x in range(1, count + 1):
                system = []
                e = f.readline().replace('\n', '')
                s = str(x) + '. ' + e + " = 0"
                system.append(to_pol_format(e))
                print(s)
                e = f.readline().replace('\n', '')
                s = '   ' + e + " = 0"
                system.append(to_pol_format(e))
                print(s)
                systems.append(system)
            number = enter_value(1, 2)
            system = systems[number - 1]
            show_system_graph(number)
            system_simple_iteration(system)
        except ValueError:
            print("Ошибка в введенном уравнении")
    while True:
        ans = input("Решить еще одно уравнение? (y/n)\n")
        if ans == 'n':
            work = False
            break
        elif ans == 'y':
            break
