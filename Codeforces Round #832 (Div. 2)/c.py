for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	a_sorted = sorted(a)
	if a[0] == a_sorted[0]:
		print("Bob")
	else:
		print("Alice")