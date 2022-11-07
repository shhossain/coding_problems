for _ in range(int(input())):
	n = int(input())
	a = input()
	remaining = 10 - n -1
	ans = 6 * (remaining*(remaining+1))//2
	print(ans)