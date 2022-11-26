from math import gcd

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	val = 0
	for i in a:
		val = gcd(val,i)

	print(a[-1]//val)