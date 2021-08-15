def factorial(num):
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    return factorial

def factorial_list(l):
    list = []
    for i in l:
        list.append(factorial(i))
    return list

print(factorial_list(range(6)))