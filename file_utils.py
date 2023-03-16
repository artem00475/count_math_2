from func_utils import *


# Вывод таблицы с итерациями в файл
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


# Вывод результата в файл
def print_to_file(table, x, count, fx):
    name = input("Введите имя файла: ")
    f = open(name, 'w')
    print_table_to_file(table, f)
    f.write("Корень: %.5f\n" % x)
    f.write("Число итераций:" + str(count + 1) + '\n')
    f.write("Значение функции: %.5f\n" % fx)
    f.close()


# Считывание исходных данных из файла
def get_data_from_file(eq):
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
        if len(inp) != 2:
            raise ValueError
        begin = float(inp[0])
        end = float(inp[1])
        der = derivative(eq)
        k = 0
        index = begin
        prev = func(eq, begin)
        while index < end + 0.1:
            if prev * func(eq, index) < 0:
                k += 1
                prev = func(eq, index)
            index += 0.1
        if k == 0:
            print("На данном интервале нет корней.")
            return False, accuracy, begin, end
        elif k > 1:
            print("На интервале", k, "корней.")
        return True, accuracy, begin, end
    except ValueError:
        print("Некорректные данные")
        return False, 0, 0, 0
