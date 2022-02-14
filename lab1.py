import math


# сумма квадратов эл-тов списка
def square_sum(arr):
    summ = 0
    for elem in arr:
        summ += elem * elem
    return summ


# сумма произведений эл-тов 2-х списков (одинаковой длины)
def mul_lists_sum(arr1, arr2):
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * arr2[i]
    return sum


# определитель матрицы 2х2
def det_2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


# определитель матрицы 3х3
def det_3(matrix):
    main_diag = matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] + matrix[0][2] * matrix[1][0] * matrix[2][1]
    sec_diag = matrix[0][3] * matrix[1][2] * matrix[2][0] - matrix[0][0] * matrix[1][2] * matrix[2][1] - matrix[0][1] * matrix[1][0] * matrix[2][3]
    return main_diag - sec_diag


# меньше нуля? -> "-", болльше нуля? -> "+" // для красивого вывода //
def is_below_zero(number):
    if number >= 0.0:
        return "+"
    else:
        return "-"


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
    t_matrix = [[slae[0][0], slae[0][1]],
                [slae[1][0], slae[1][1]]]
    det = det_2(t_matrix)
    t_matrix = [[slae[0][2], slae[0][1]],
                [slae[1][2], slae[1][1]]]
    det_first = det_2(t_matrix)
    t_matrix = [[slae[0][0], slae[0][2]],
                [slae[1][0], slae[1][2]]]
    det_sec = det_2(t_matrix)
    # It's working!
    # print(f"det: {det}, det_first: {det_first}, det_sec: {det_sec}\n")
    a = det_first / det
    b = det_sec / det
    # It's working!
    print(f"linear func: y = {a}*x {is_below_zero(b)} {abs(b)}\n")
    return [a, b]


def power_fun(x_list, y_list):
    # logarithm...
    for i in range(len(x_list)):
        x_list[i] = math.log(x_list[i])
        y_list[i] = math.log(y_list[i])
    print(f"Logarithmed: {x_list}\n {y_list}\n")


# Variant 2
x = [1, 2, 3, 4, 5, 6]
y = [1.0, 1.5, 3.0, 4.5, 7.0, 8.5]

linear_fun(x, y)

power_fun(x, y)

print(f"Logarithmed: {x}\n {y}\n")
