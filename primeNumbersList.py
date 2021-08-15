def isPrime(num):
    for factor in range(2, num//2 + 1): 
        if num % factor == 0:
            return str(num) + " is not prime"
    return str(num) + " is prime"

def prime_nums_list(l): 
    list = []
    for i in l:
        list.append(isPrime(i))
    return list

print(prime_nums_list([50, 45, 47, 13, 2, 4, 8]))