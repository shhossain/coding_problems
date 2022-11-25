letters = "abcdefghijklmnopqrstuvwxyz"
m = {l: i+1 for i, l in enumerate(letters)}

for _ in range(int(input())):
	n = int(input())
	s = input()
	ans = 0
	for i in s:
		ans = max(ans,m[i])
	print(ans)