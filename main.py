from console_utils import *
from file_utils import print_to_file, get_data_from_file
from graph_utils import *
from system_utils import *


def calculate_x_for_chord_method(a, b, fa, fb):
    return (a * fb - b * fa) / (fb - fa)


# Вывод результата
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


# Метод хорд
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
        a, b = get_interval(eq, accuracy)
        check = True
    else:
        check, accuracy, a, b = get_data_from_file(eq)
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
        a, b = get_interval(eq, accuracy)
        check = True
    else:
        check, accuracy, a, b = get_data_from_file(eq)
    if check:
        a0, b0 = a, b
        a, b = get_initial_approximation(eq, a, b, accuracy)
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
        a, b = get_interval(eq, accuracy)
        check = True
    else:
        check, accuracy, a, b = get_data_from_file(eq)
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
        print(func(derphi, a))
        print(func(derphi, b))
        if abs(func(derphi, a)) >= 1 or abs(func(derphi, b)) >= 1:
            print("Условие сходимости не выполнено")
        phix = func(phi, x)
        deviation = abs(x - phix)
        fphi = func(eq, phix)
        count = 0
        table.append([count, x, phix, fphi, deviation])
        while accuracy < abs(fphi) or accuracy < deviation:
            count += 1
            if count == 1001:
                break
            x = phix
            phix = func(phi, x)
            fphi = func(eq, phix)
            deviation = abs(x - phix)
            table.append([count, x, phix, fphi, deviation])
        if count <= 1000:
            print_result(table, table[-1][2], count, fphi)
            show_graph(a0 - 1, b0 + 1, num)
        else:
            print("Превышен лимит итераций")


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


# Преобразование уравнения в обратную польскую запись
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
