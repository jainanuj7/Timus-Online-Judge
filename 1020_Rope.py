# https://acm.timus.ru/problem.aspx?space=1&num=1020
# Execution time: 0.078s
# Memory used: 288 KB

import math
user_input = list(map(float, input().split()))
n = int(user_input[0])
r = user_input[1]

if n==1:
    print(round(2 * math.pi * r, 2))
else:
    first_x, first_y = list(map(float, input().split()))
    prev_x = first_x
    prev_y = first_y
    dist = 0
    for i in range(1,n):
        x, y = list(map(float, input().split()))
        dist = dist + math.sqrt( ((x - prev_x)**2)+(( y - prev_y)**2))
        prev_x = x
        prev_y = y

    dist = dist + math.sqrt( ((x - first_x)**2)+(( y - first_y)**2))
    dist = dist + (2 * math.pi * r)
    print(round(dist,2))