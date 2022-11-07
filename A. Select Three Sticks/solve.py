for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	s = sorted(a)
	v = 1e19
	for i in range(n-2):
		x,y,z = s[i],s[i+1],s[i+2]
		ans1 = abs(x-x) + abs(x-y) + abs(x-z)
		ans2 = abs(y-x) + abs(y-y) + abs(y-z)
		ans3 = abs(z-x) + abs(z-y) + abs(z-z)
		v = min(v,ans1,ans2,ans3)

	print(v)

