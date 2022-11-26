from math import log

for _ in range(int(input())):
	n = int(input())
	v = 0
	if n == 0:
		v = 0
	else:
		v = log(n,2)
		if v != int(v):
			v = int(v) + 1
		else:
			v = int(v)

	print(2**v)