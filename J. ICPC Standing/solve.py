


p = False
for i in range(1,int(input())+1):
	a,b,c = map(int, input().split())
	ans = "Yes"
	if p:
		ans = "No"

	if c == 1:
		p = True

	print(f"Case {i}: {ans}")


