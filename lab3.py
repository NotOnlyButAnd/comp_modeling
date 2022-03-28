# Метод квадратов
# Вход: num - исходное число, n - кол-во повторений
# Выход: random_numbers - массив сгенерированных
def squares_method(num, n):
    # Массив полученных чисел
    random_numbers = []
    capacity = len(str(num))  # Разрядность числа

    for i in range(n):
        num_2 = str(num ** 2)

        # Незначащие нули в начале, если необходимо
        while len(num_2) != capacity * 2:
            num_2 = "0" + num_2

        # Берем только n средних разрядов
        new_num = num_2[int(capacity - int(capacity/2)):int(capacity + int(capacity/2))]

        # Добавляем полученное случайное число, в массив
        random_numbers.append(float("0." + new_num))

        num = int(new_num)

    return random_numbers

def main():
    # Метод квадратов, исходные данные и вызов
    n = 8   # Количество повторений
    num = 7153  # Исходное число
    print(f"Square's method: {squares_method(num, n)}")

    # num = 1357 # Исходное число
    # print(method_square(str(num), n))

    # num = 3729  # Исходное число
    # core = 5167 # Ядро
    # print(method_compasion(str(num), core, n))

    # multiplier = 1357 # Множитель
    # divider = 5689 # Делитель

    # методы, представляющие модификации перечисленных методов


if __name__ == '__main__':
    main()
    
