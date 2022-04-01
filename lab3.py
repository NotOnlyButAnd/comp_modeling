# Метод квадратов
# Вход: num - исходное число (INTEGER), n - кол-во повторений (INTEGER)
# Выход: random_numbers - массив сгенерированных (Array of Float)
def squares_method(num, n):
    random_numbers = []
    capacity = len(str(num))  # Разрядность числа

    for i in range(n):
        num_2 = str(num ** 2)

        # Незначащие нули в начале, если необходимо
        while len(num_2) != capacity * 2:
            num_2 = "0" + num_2

        # Берем только n средних разрядов
        new_num = num_2[int(capacity - capacity/2):int(capacity + capacity/2)]

        # Добавляем полученное случайное число в массив
        random_numbers.append(float("0." + new_num))

        num = int(new_num)

    return random_numbers


# Метод произведений
# Вход: num - исходное число (INTEGER), core - ядро (INTEGER), n - кол-во повторений (INTEGER)
# Выход: random_numbers - массив сгенерированных (Array of Float)
def mul_method(num, core, n):
    random_number = []
    capacity = len(str(num))  # Разрядность числа

    for i in range(n):

        num_2 = str(int(num) * core)

        # Незначащие нули в начале, если необходимо
        while len(num_2) != capacity * 2:
            num_2 = "0" + num_2

        # Берем только n средних разрядов
        new_num = num_2[int(capacity - capacity / 2):int(capacity + capacity / 2)]

        # Добавляем полученное случайное число в массив
        random_number.append(float("0." + new_num))

        num = num_2[-capacity:]

    return random_number


# Мультипликативный конгруэнтный метод
def mul_congruent_method(num, multiplier, divider, n):
    random_number = []

    for i in range(n):
        new_num = num * multiplier % divider  # Берем остаток

        # Добавляем полученное случайное число в массив
        random_number.append(float("0." + str(new_num)))

        num = new_num

    return random_number


def shacked_cong_method(num, multiplier, divider, n, c):
    random_number = []

    for i in range(n):
        new_num = (num * multiplier + c) % divider  # Получаем остаток

        # Добавляем полученное случайное число в массив
        pull = '0.' + str(new_num)
        random_number.append(round(float(pull), 4))

        num = new_num
    return random_number


def main():
    n = 8  # Количество повторений

    # Метод квадратов, исходные данные и вызов
    num = 7153  # Исходное число
    # num = 1357
    print(f"Square's method: {squares_method(num, n)}")

    # Метод произведений, исходные данные и вызов
    num = 3729  # Исходное число
    core = 5167     # Ядро
    print(f"Mul's method: {mul_method(num, core, n)}")

    # Мультипликативный конгруэнтный метод, исходные данные и вызов
    num = 1357  # Исходное число
    multiplier = 1357   # Множитель
    divider = 5689  # Делитель
    print(f"Mul congruent method: {mul_congruent_method(num, multiplier, divider, n)}")

    # Смешанный конгруэнтный метод, исходные данные и вызов
    num = 1357  # Исходное число
    multiplier = 106  # Множитель
    divider = 6075  # Делитель
    c = 1283  # Аддитивная константа
    print(f"Shacked congruent method: {shacked_cong_method(num, multiplier, divider, n, c)}")


if __name__ == '__main__':
    main()
