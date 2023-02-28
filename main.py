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
    for x in range(1, count + 1):
        print(x, ". ", f.readline(), sep="")
    equation = enter_value(1, count)
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
else:
    print("Выберите систему нелинейных уравнений:")
