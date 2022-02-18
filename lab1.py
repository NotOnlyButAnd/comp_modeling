import math
import matplotlib.pyplot as plt

# сумма квадратов эл-тов списка
def square_sum(arr):
    summ = 0
    for elem in arr:
        summ += elem * elem
    return summ


# сумма кубов эл-тов списка
def cubic_sum(arr):
    summ = 0
    for elem in arr:
        summ += elem * elem * elem
    return summ


# сумма четвертых степеней эл-тов списка
def fourth_degree_sum(arr):
    summ = 0
    for elem in arr:
        summ += elem * elem * elem * elem
    return summ


# сумма произведений эл-тов 2-х списков (одинаковой длины)
def mul_lists_sum(arr1, arr2):
    summ = 0
    for i in range(len(arr1)):
        summ += arr1[i] * arr2[i]
    return summ


# сумма произведений эл-тов 2-х списков, причем первый в квадрате
def mul_lists_sum_2(arr1, arr2):
    summ = 0
    for i in range(len(arr1)):
        summ += arr1[i] * arr1[i] * arr2[i]
    return summ


# определитель матрицы 2х2
def det_2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


# определитель матрицы 3х3
def det_3(matrix):
    main_diag = matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] + matrix[0][2] * \
                matrix[1][0] * matrix[2][1]
    sec_diag = matrix[0][2] * matrix[1][1] * matrix[2][0] + matrix[0][0] * matrix[1][2] * matrix[2][1] + matrix[0][1] * \
               matrix[1][0] * matrix[2][2]
    return main_diag - sec_diag


# меньше нуля? -> "-", болльше нуля? -> "+" // для красивого вывода //
def is_below_zero(number):
    if number >= 0.0:
        return "+"
    else:
        return "-"


# метод крамера для 2х2
def kramer_2_2(my_slae):
    t_matrix = [[my_slae[0][0], my_slae[0][1]],
                [my_slae[1][0], my_slae[1][1]]]
    det = det_2(t_matrix)
    t_matrix = [[my_slae[0][2], my_slae[0][1]],
                [my_slae[1][2], my_slae[1][1]]]
    det_first = det_2(t_matrix)
    t_matrix = [[my_slae[0][0], my_slae[0][2]],
                [my_slae[1][0], my_slae[1][2]]]
    det_sec = det_2(t_matrix)
    # It's working!
    # print(f"det: {det}, det_first: {det_first}, det_sec: {det_sec}\n")
    a = det_first / det
    b = det_sec / det
    return a, b


# метод крамера для 3х3
def kramer_3_3(my_slae):
    t_matrix = [[my_slae[0][0], my_slae[0][1], my_slae[0][2]],
                [my_slae[1][0], my_slae[1][1],  my_slae[1][2]],
                [my_slae[2][0], my_slae[2][1],  my_slae[2][2]]]
    det = det_3(t_matrix)
    t_matrix = [[my_slae[0][3], my_slae[0][1], my_slae[0][2]],
                [my_slae[1][3], my_slae[1][1],  my_slae[1][2]],
                [my_slae[2][3], my_slae[2][1],  my_slae[2][2]]]
    det_first = det_3(t_matrix)
    t_matrix = [[my_slae[0][0], my_slae[0][3], my_slae[0][2]],
                [my_slae[1][0], my_slae[1][3],  my_slae[1][2]],
                [my_slae[2][0], my_slae[2][3],  my_slae[2][2]]]
    det_sec = det_3(t_matrix)
    t_matrix = [[my_slae[0][0], my_slae[0][1], my_slae[0][3]],
                [my_slae[1][0], my_slae[1][1],  my_slae[1][3]],
                [my_slae[2][0], my_slae[2][1],  my_slae[2][3]]]
    det_third = det_3(t_matrix)
    # It's working!
    # print(f"det: {det}, det_first: {det_first},\n det_sec: {det_sec}, det_third: {det_third}\n")
    a = det_first / det
    b = det_sec / det
    c = det_third / det
    return a, b, c


# красивый вывод linear
def print_lin(my_list):
    print(f"linear func: y = {my_list[0]}*x {is_below_zero(my_list[1])} {abs(my_list[1])}\n")


# красивый вывод power
def print_pow(my_list):
    print(f"Power func: y = {my_list[0]} * x ^ {my_list[1]}\n")


# красивый вывод power_2
def print_pow_2(my_list):
    print(f"Power func 2: y = {my_list[0]} * e ^ ({my_list[1]}*x)\n")


# красивый вывод quadratic
def print_quadratic(my_list):
    print(f"Quadratic: y = {is_below_zero(my_list[1])} {abs(my_list[0])}*x^2 {is_below_zero(my_list[1])} {abs(my_list[1])}*x {is_below_zero(my_list[2])} {abs(my_list[2])}\n")


# 1.1. y = ax + b - linear
def linear_fun(x_list, y_list):
    sum_x = sum(x_list)
    sum_y = sum(y_list)
    sum_x_2 = square_sum(x_list)
    sum_x_y = mul_lists_sum(x_list, y_list)
    # It's working!
    # print (f"sum_x: {sum_x}, sum_y: {sum_y}, sum_x_2: {sum_x_2 }, sum_x_y: {sum_x_y}\n")
    slae = [[sum_x_2, sum_x, sum_x_y],
            [sum_x, len(x_list), sum_y]]
    # It's working!
    # print(f"SLAE: {slae}, SLAE[0]: {slae[0]}\n")
    a, b = kramer_2_2(slae)
    # It's working!
    # print(f"linear func: y = {a}*x {is_below_zero(b)} {abs(b)}\n")
    return [a, b]


# 1.2 y = beta * x^a - power
def power_fun(x_list, y_list):
    # logarithm...
    new_x_list = []
    new_y_list = []
    for i in range(len(x_list)):
        new_x_list.append(math.log(x_list[i]))
        new_y_list.append(math.log(y_list[i]))
    # It's working!
    # print(f"Logarithmed: {new_x_list}\n {new_y_list}\n")
    # solving task 1...
    a_b = linear_fun(new_x_list, new_y_list)
    beta = pow(math.e, a_b[1])
    # It's working!
    # print(f"Power func: y = {beta} * x ^ {a_b[0]}\n")
    # returning beta and a
    return [beta, a_b[0]]


# 1.3 y = beta * e^(a*x) - power 2
def power_fun_2(x_list, y_list):
    # logarithm...
    new_y_list = []
    for i in range(len(y_list)):
        new_y_list.append(math.log(y_list[i]))
    # It's working!
    # print(f"Logarithmed: {x_list}\n {new_y_list}\n")
    # solving task 1...
    a_b = linear_fun(x_list, new_y_list)
    beta = pow(math.e, a_b[1])
    # It's working!
    # print(f"Power func: y = {beta} * e ^ ({a_b[0]}*x)\n")
    # returning beta and a
    return [beta, a_b[0]]


# 1.4 y = a*x^2 + bx + c - quadratic
def quadratic_fun(x_list, y_list):
    sum_x_4 = fourth_degree_sum(x_list)
    sum_x_3 = cubic_sum(x_list)
    sum_x_2 = square_sum(x_list)
    sum_x = sum(x_list)
    sum_x_2_y = mul_lists_sum_2(x_list, y_list)
    sum_x_y = mul_lists_sum(x_list, y_list)
    sum_y = sum(y_list)
    # It's working!
    # print(f"All summs: {sum_x_4}, {sum_x_3}, {sum_x_2},\n {sum_x}, {sum_x_2_y}, {sum_x_y},\n {sum_y}")
    slae = [[sum_x_4, sum_x_3, sum_x_2, sum_x_2_y],
            [sum_x_3, sum_x_2, sum_x, sum_x_y],
            [sum_x_2, sum_x, len(x_list), sum_y]]
    # It's working!
    # print(slae)
    a, b, c = kramer_3_3(slae)
    return [a, b, c]


# Variant 2
x = [1, 2, 3, 4, 5, 6]
y = [1.0, 1.5, 3.0, 4.5, 7.0, 8.5]

print_lin(linear_fun(x, y))

print_pow(power_fun(x, y))

print_pow_2(power_fun_2(x, y))

print_quadratic(quadratic_fun(x, y))

# print(f"Non Logarithmed: {x}\n {y}\n")
