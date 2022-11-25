from math import log

for _ in range(int(input())):
	n,a,b = map(int, input().split())
	v = int(log(n,2))
	print((a*v)+((b*(v-1))))