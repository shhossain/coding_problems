def solve(l,r,a):
	x1 = r
	x2 = r%a
	if x2 == 0:
		x2 = r - 1
	else:
		x2 = r - x2 - 1

	if x2 < l:
		x2 = r


	v1 = (x1//a) + (x1%a)
	v2 = (x2//a) + (x2%a)

	return max(v1,v2)

for _ in range(int(input())):
	l,r,a = map(int, input().split())
	print(solve(l,r,a))