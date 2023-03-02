import matplotlib.pyplot as plt
import numpy as np


def show_graph(a, b, num):
    x = np.arange(a, b + 0.01, 0.01)
    if num == 1:
        plt.plot(x, x ** 3 - 0.77 * x ** 2 - 1.251 * x + 0.43)
    elif num == 2:
        plt.plot(x, x ** 2 - x + 4)
    plt.grid(True)
    plt.show()


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
        if func(eq, a) * func(eq, b) > 0:
            print("На данном интервале нет корней. Повторите ввод")
        else:
            return a, b


def equation_to_string(eq):
    s = ''
    for i in range(len(eq)):
        degree = len(eq) - i - 1
        if eq[i] == 0:
            continue
        if abs(eq[i]) != 1:
            s += str(abs(eq[i]))
        if degree > 1:
            s += "x^" + str(degree)
            if eq[i + 1] > 0:
                s += ' + '
            else:
                s += ' - '
        elif degree == 1:
            s += "x"
            if eq[i + 1] >= 0:
                s += ' + '
            else:
                s += ' - '
        else:
            continue
    return s


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


def print_table_to_file(table):
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


def print_to_output(table, x, count, fx):
    print_table(table)
    print("Корень: %.5f" % x)
    print("Число итераций:", count + 1)
    print("Значение функции: %.5f" % fx)


def print_to_file(table, x, count, fx):
    name = input("Введите имя файла: ")
    f = open(name, 'w')
    print_table_to_file(table)
    f.write("Корень: %.5f\n" % x)
    f.write("Число итераций:" + str(count + 1) + '\n')
    f.write("Значение функции: %.5f\n" % fx)
    f.close()


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


def chord_method(eq, num):
    print("Метод хорд")
    table = [["   №   ", "   a   ", "   b   ", "   x   ", "  F(a)  ", "  F(b)  ", "  F(x)  ", "|x_n+1 - x_n|"]]
    accuracy = get_accuracy()
    a, b = get_interval(eq)
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
    table = [["   №   ", "x_(k-1)", " x_k ", "x_(k+1)", "f(x_(k+1))", "|x_k+1 - x_k|"]]
    accuracy = get_accuracy()
    a, b = get_initial_approximation(eq)
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


def derivative(eq):
    d = []
    container = []
    i = 0
    while i < len(eq):
        if str(eq[i]) == '^':
            degree = eq[i-1]
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
            if i < len(eq) - 2 and str(eq[i+1]) == '*':
                d.append('*')
                i += 1
        elif str(eq[i]) == 'x' and i < len(eq) -3 and str(eq[i+2]) != "^" and str(eq[i+1]) != "sin" \
                and str(eq[i+1]) != "cos":
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
    # print(d)


    # for i in range(len(eq) - 1):
    #     degree = len(eq) - 1 - i
    #     d.append(eq[i] * degree)
    return d


def simple_iteration_method(eq, num):
    print("Метод простых итераций")
    table = [["   №   ", " x_k ", "x_(k+1)", "f(x_(k+1))", "|x_k+1 - x_k|"]]
    accuracy = get_accuracy()
    a, b = get_interval(eq)
    a0, b0 = a, b
    der = derivative(eq)
    alpha = -1 / max(abs(func(der, a)), abs(func(der, b)))
    phi = eq.copy()
    phi.append(alpha)
    phi.append('*')
    phi.append('x')
    phi.append('+')
    print(phi)
    if abs(func(der, a)) >= abs(func(der, b)):
        x = a
    else:
        x = b
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


def system_func(eq, x1, x2):
    res = eq[-1]
    for i in range(len(eq) - 2, -1, -1):
        degree = (len(eq) - i + 1) // 3
        index = (len(eq) - i + 1) % 3
        if index == 0:
            res += eq[i]*(x1**degree)
        elif index == 1:
            res += eq[i]*(x2**degree)
        else:
            res += eq[i]*(x1**degree)*(x2**degree)
    res = round(res, 5)
    if abs(res) == 0:
        res = 0
    return res


def derivative_equation(eq, a):
    res = [0, 0]
    for i in range(len(eq) - 2, -1, -1):
        degree = (len(eq) - i + 1) // 3
        index = (len(eq) - i + 1) % 3
        if index == a:
            res[1-a] += eq[i]*degree
        elif index == 2:
            res[a] += eq[i]*degree
    return res


def check_convergence(stm, a, b):
    p1x1 = derivative_equation(stm[0], 0)
    p2x1 = derivative_equation(stm[1], 0)
    p1x2 = derivative_equation(stm[0], 1)
    p2x2 = derivative_equation(stm[1], 1)
    a = int(a)
    b = int(b)
    for x in range(min(a, 0), max(a, 0)+1):
        for y in range(min(b, 0), max(b, 0)+1):
            if abs(p1x1[0]*y + p1x1[1]*x) + abs(p1x2[0]*y + p1x2[1]*x) > 1:
                return False
            if abs(p2x1[0]*y + p2x1[1]*x) + abs(p2x2[0]*y + p2x2[1]*x) > 1:
                return False
    return True


def system_simple_iteration(stm):
    accuracy = get_accuracy()
    system1 = []
    if stm[0][-2] != 0:
        x = -stm[0][-2]
        stm[0][-2] = 0
        eq = []
        for y in stm[0]:
            eq.append(y / x)
        system1.append(eq)
    if stm[1][-3] != 0:
        x = -stm[1][-3]
        stm[1][-3] = 0
        eq = []
        for y in stm[1]:
            eq.append(y / x)
        system1.append(eq)
    print(system1)
    x1, x2 = get_system_start()
    if check_convergence(system1, x1, x2):
        x_1, x_2 = system_func(system1[0], x1, x2), system_func(system1[1], x1, x2)
        deviation1 = abs(x1 - x_1)
        deviation2 = abs(x2 - x_2)
        count = 1
        while accuracy < deviation1 or accuracy < deviation2:
            print(x_1, x_2)
            count += 1
            x1, x2 = x_1, x_2
            x_1, x_2 = system_func(system1[0], x1, x2), system_func(system1[1], x1, x2)
            deviation1 = abs(x1 - x_1)
            deviation2 = abs(x2 - x_2)
        print(x_1, x_2)
        print(count)
        print(deviation1, deviation2)
    else:
        print("Достаточное условие сходимости не выполняется")


def to_pol_format(st):
    a = st.split()
    res = []
    op = []
    symb = {'-': 0, '+': 0, '*': 1, '^': 2, 'cos': 3, 'sin': 3}
    for s in a:
        if s not in symb:
            if s != "x":
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
    print(res)
    return res


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
            # e = [float(y) for y in f.readline().split()]
            # s = str(x) + '. ' + equation_to_string(e)
            e = f.readline()
            s = str(x) + '. ' + e
            equations.append(to_pol_format(e))
            print(s)
        number = enter_value(1, count)
        equation = equations[number - 1]
        derivative(equation)
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
    systems = [[[0.2, 0.1, 0, 0, 1, -0.3], [0, 0.2, 0.1, 1, 0, -0.7]], [[0, 0, 0, 2, -5, -10], [1, 1, 0, 1, 0, -20]]]
    print("Выберите систему нелинейных уравнений:")
    print("1. 0.1x_1^2 + x_1 + 0.2x_2^2 - 0.3 = 0")
    print("   0.2x_1^2 + x_2 + 0.1x_1x_2 - 0.7 = 0")
    print("2. 0.5x_2^2 + 0.2x_1^2 + x_1x_2 + 2x_2 + x_1 - 5 = 0")
    print("   2x_2^2 + 0.2x_1^2 + 0.7x_1x_2 + x_2 + 0.8x_1 - 7 = 0")
    number = enter_value(1, 2)
    system = systems[number-1]
    system_simple_iteration(system)
