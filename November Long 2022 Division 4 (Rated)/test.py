


modulo = 10**9 + 7
MAX = 2 * 10**5
facts = [0] * (MAX + 1)
facts[0] = 1
facts[1] = 1
s = 1
for i in range(2, MAX + 1):
    s = ((s % modulo) * (i % modulo)) % modulo
    facts[i] = s
    



