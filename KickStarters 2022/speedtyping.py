from collections import defaultdict


for x in range(int(input())):
	i = input()
	p = input()

	mi = defaultdict(int)
	mp = defaultdict(int)

	for j in  i:
		mi[j]+=1

	for j in p:
		mp[j]+=1


	flag = True
	ans = 0
	if len(mi) != len(mp):
		flag = False
	else:
		for k in mi:
			if mp[k] != 0:
				ans += mp[k] - mi[k]
			else:
				flag = False
				break

	print(f"Case #{x+1}: ",end="")
	if not flag:
		print("IMPOSSIBLE")
	else:
		print(ans)
