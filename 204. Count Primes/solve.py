class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        primes = [1] * n

        primes[0] = 0
        primes[1] = 0
        primes[2] = 1
        
        m = 2
        i = 2
        ct = 0
        for i in range(n):
            if primes[i] == 1:
                ct+=1

                for j in range(i*i,n,i):
                    primes[j] = 0
        return ct


    




print(Solution().countPrimes(40))

