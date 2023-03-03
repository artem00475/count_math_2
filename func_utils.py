import numpy as np


# Вычисление значение функции
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


# Вычисление производной функции
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
