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


def get_interval(e):
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
        if func(e, a)*func(e, b) > 0:
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
            if eq[i+1] > 0:
                s += ' + '
            else:
                s += ' - '
        elif degree == 1:
            s += "x"
            if eq[i+1] >= 0:
                s += ' + '
            else:
                s += ' - '
        else:
            continue
    return s


def func(equation, x):
    s = 0
    for i in range(len(equation)):
        degree = len(equation) - 1 - i
        s += equation[i] * x ** degree
    return s


def calculate_x_for_chord_method(a, b, fa, fb):
    return (a*fb - b*fa)/(fb-fa)


def print_table(table):
    for c in table[0]:
        print(c, end='    ')
    print()
    for row in table[1:]:
        for c in row:
            print('%.5f' % c, end='    ')
        print()


def chord_method(equation):
    print("Метод хорд")
    table = [["   №   ", "   a   ", "   b   ", "   x   ", "  F(a)  ", "  F(b)  ", "  F(x)  ", "|x_n+1 - x_n|"]]
    accuracy = get_accuracy()
    a, b = get_interval(equation)
    print(111)
    fa = func(equation, a)
    fb = func(equation, b)
    x = calculate_x_for_chord_method(a, b, fa, fb)
    fx = func(equation, x)
    deviation = min(abs(x-a), abs(x-b))
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
        fx = func(equation, x)
        deviation = min(abs(x - a), abs(x - b))
        table.append([count, a, b, x, fa, fb, fx, deviation])
    print_table(table)
    print("Корень:", table[-1][3])


def secant_method():
    print("Метод секущих")


def simple_iteration_method():
    print("Метод простых итераций")


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
            e = [float(y) for y in f.readline().split()]
            s = str(x) + '. ' + equation_to_string(e)
            equations.append(e)
            print(s)
        equation = equations[enter_value(1, count)-1]
        print("ВЫберите метод:")
        print("1. Метод хорд")
        print("2. Метод секущих")
        print("3. Метод простых итераций")
        method = enter_value(1, 3)
        if method == 1:
            chord_method(equation)
        elif method == 2:
            secant_method()
        else:
            simple_iteration_method()
    except ValueError:
        print("Ошибка в введенном уравнении")
else:
    print("Выберите систему нелинейных уравнений:")
