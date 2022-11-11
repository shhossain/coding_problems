def time_diff(t1: tuple, t2: tuple) -> tuple:
	h1, m1 = t1
	h2, m2 = t2

	mins = 0
	if h1 == h2 and m1 > m2:
		mins = (24 - h1 + h2) * 60 + m2 - m1
	elif h1 == h2 and m1 <= m2:
		mins = (h2 - h1) * 60 + m2 - m1
	elif h1 > h2:
		mins = (24 - h1 + h2) * 60 + m2 - m1
	else:
		mins = (h2 - h1) * 60 + m2 - m1

	return mins//60, mins % 60


for _ in range(int(input())):
	n, h, m = map(int, input().split())
	min_diff = (24, 00)
	for i in range(n):
		h2, m2 = tuple(map(int, input().split()))
		min_diff = min(min_diff, time_diff((h, m), (h2, m2)))
	print(min_diff[0], min_diff[1])
