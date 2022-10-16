import math

mem = {}
def is_coprime(num1, num2):
    # store factors of num1 and num2 in mem
    if num1 not in mem:
        mem[num1] = get_factors(num1)
    if num2 not in mem:
        mem[num2] = get_factors(num2)

def get_factors(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            mem[num] = i 

    return factors

def get_highest(a):
    highest = -1
    for i in range(len(a)):
        for j in range(i, len(a)):
            if is_coprime(a[i], a[j]):
                highest = max(highest, i + 1 + j + 1)

    return highest


t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(get_highest(a))
