def gen_primes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    r = []
    for p in range(n + 1):
        if prime[p]:
            r.append(p)
    

    return prime,r

prime_list,primes = gen_primes(200000+1)

for _ in range(int(input())):
    n = int(input())
    for i in primes:
        if not prime_list[n+i]:
            print(i)
            break
