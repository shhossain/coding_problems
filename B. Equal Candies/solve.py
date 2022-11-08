for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	a_min = min(a)

	t = 0

	for i in a:
		t+= (i-a_min)

	print(t)