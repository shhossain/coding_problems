from math import sqrt


def dist(x1, y1, x2, y2):
	return sqrt((x1-x2)**2 + (y1-y2)**2)


for _ in range(int(input())):
	x1, y1, x2, y2 = map(int, input().split())

	p1 = x2, y1
	p2 = x2, y2

	p3 = x1, y1
	p4 = p1

	d1 = dist(*p1, *p2)
	d2 = dist(*p3, *p4)

	d3 = min(d1, d2)

	r = d3 / 2
	v = sqrt(r**2 + r**2)
	print(round(v,10))
