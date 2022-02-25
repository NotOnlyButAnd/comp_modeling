import random


# function 1 (n = 11)
def f_1(cur_x):
    return 10 * cur_x / 11


# function 2 (n = 11)
def f_2(cur_x):
    return 10 * (cur_x - 20) / -9 + 20


# Task 1 #
n = 11

# точка пересечения f_1 и f_2 [x, y]
inter_point = [20.9, 19]
print(f"f_1 intersect f_2: [{inter_point[0]}, {inter_point[1]}]")

# точка пересечения f_1 и x
f_1_x = round(f_1(0), 3)
print(f"f_1 intersect x = 0: [{f_1_x}, 0]")

# точка пересечения f_2 и x
f_2_x = round(f_2(0), 3)
print(f"f_2 intersect x = 0: [{f_2_x}, 0]")

# следовательно прямоугольник будет иметь размеры (a - по x, b - по y)
a, b = 21, 19

#####
# строим графики и прямоугольник
#####

print("Input amount N of random points: ")
N = int(input())

# создаем рандомные точки в пределах прямоугольника
rand_x = []
rand_y = []
# round(random.random(), 3)
for i in range(N):
    rand_x.append(round(random.random() * 10 + 1, 3))
