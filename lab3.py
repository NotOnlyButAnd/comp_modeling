import math
import random


# Метод квадратов
# Вход: num - исходное число (INTEGER), n - кол-во повторений (INTEGER)
# Выход: random_numbers - массив сгенерированных (Array of Float)
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
        new_num = num_2[int(capacity - capacity/2):int(capacity + capacity/2)]

        # Добавляем полученное случайное число, в массив
        random_numbers.append(float("0." + new_num))

        num = int(new_num)

    return random_numbers


# Метод произведений
# Вход: num - исходное число (INTEGER), core - ядро (INTEGER), n - кол-во повторений (INTEGER)
# Выход: random_numbers - массив сгенерированных (Array of Float)
def mul_method(num, core, n):
    # Массив полученных чисел
    random_number = []
    capacity = len(str(num))  # Разрядность числа

    for i in range(n):

        num_2 = str(int(num) * core)

        # Незначащие нули в начале, если необходимо
        while len(num_2) != capacity * 2:
            num_2 = "0" + num_2

        # Берем только n средних разрядов
        new_num = num_2[int(capacity - capacity / 2):int(capacity + capacity / 2)]

        # Добавляем полученное случайное число, в массив
        random_number.append(float("0." + new_num))

        num = num_2[-capacity:]

    return random_number


# Мультипликативный конгруэнтный метод
def mul_congruent_method(num, multiplier, divider, n):
    # Массив полученных чисел
    random_number = []
    capacity = len(str(num))  # Разрядность числа

    for i in range(n):
        new_num = num * multiplier % divider  # Берем остаток получаем остаток

        # Добавляем случайное число,
        # равномерно распределённое в интервале (0; 1);
        random_number.append(new_num * pow(10, -capacity))

        num = new_num

    return random_number


def main():
    # Метод квадратов, исходные данные и вызов
    n = 8   # Количество повторений
    num = 7153  # Исходное число
    # num = 1357
    print(f"Square's method: {squares_method(num, n)}")

    # Метод произведений, исходные данные и вызов
    num = 3729  # Исходное число
    core = 5167     # Ядро
    print(f"Mul's method: {mul_method(num, core, n)}")

    # Мультипликативный конгруэнтный метод, исходные данные и вызов
    multiplier = 1357   # Множитель
    divider = 5689  # Делитель

    # методы, представляющие модификации перечисленных методов


if __name__ == '__main__':
    main()
