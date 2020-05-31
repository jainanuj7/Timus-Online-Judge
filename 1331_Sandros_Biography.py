# https://acm.timus.ru/problem.aspx?space=1&num=1786
# Execution time: 0.093s
# Memory used: 208 KB

str = input()
min_cost = 100
for i in range(0, len(str) - 6 + 1):
    cost = 0
    substr = str[i:i+6]

    if substr[0].islower():
        cost = cost + 5
    if substr[0].upper() != 'S':
        cost = cost + 5

    if substr[1].isupper():
        cost = cost + 5
    if substr[1].lower() != 'a':
        cost = cost + 5

    if substr[2].isupper():
        cost = cost + 5
    if substr[2].lower() != 'n':
        cost = cost + 5

    if substr[3].isupper():
        cost = cost + 5
    if substr[3].lower() != 'd':
        cost = cost + 5

    if substr[4].isupper():
        cost = cost + 5
    if substr[4].lower() != 'r':
        cost = cost + 5

    if substr[5].isupper():
        cost = cost + 5
    if substr[5].lower() != 'o':
        cost = cost + 5

    if cost < min_cost:
        min_cost = cost
        
print(min_cost)