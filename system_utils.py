# Считывание начальных данных для решения системы
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
        else:
            return a, b


# Вычисление значения функции от двух переменных
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


# Вычисление значения производной по первой переменной
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


# Вычисление значения производной по второй переменной
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


# Проверка сходимости системы
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


# Разрешение уравнения относительно х
def express_x(eq, x):
    a = 1
    for i in range(len(eq) - 1):
        if eq[i] == x:
            if (i < len(eq) - 2 and eq[i + 2] != '^' and eq[i + 1] != 'x_2' and eq[i - 1] != 'x_1' and eq[
                i + 2] != 'x_2' and eq[i - 2] != 'x_1') or i >= len(eq) - 3:
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
