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


def chord_method():
    print("Метод хорд")


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
            eq = [float(y) for y in f.readline().split()]
            s = str(x) + '. ' + equation_to_string(eq)
            equations.append(eq)
            print(s)
        equation = equations[enter_value(1, count)-1]
        print("ВЫберите метод:")
        print("1. Метод хорд")
        print("2. Метод секущих")
        print("3. Метод простых итераций")
        method = enter_value(1, 3)
        if method == 1:
            chord_method()
        elif method == 2:
            secant_method()
        else:
            simple_iteration_method()
    except ValueError:
        print("Ошибка в введенном уравнении")
else:
    print("Выберите систему нелинейных уравнений:")
