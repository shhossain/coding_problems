modulo = 10**9 + 7
MAX = 10**6
facts = [0] * (MAX + 1)
facts[0] = 1
facts[1] = 1
s = 1
for i in range(2, MAX + 1):
    s = ((s % modulo) * (i % modulo)) % modulo
    facts[i] = s


for _ in range(int(input())):
	n = input()
	a = list(map(int, input().split()))
	asum = 0
	for i in a:
		asum += facts[i]

	print(asum % modulo)
