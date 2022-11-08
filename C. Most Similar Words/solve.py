letters = "abcdefghijklmnopqrstuvwxyz"
m = {}
for i in range(1,27):
	m[letters[i-1]] = i


def cost(s1,s2):
	t = 0
	for i,j in zip(s1,s2):
		t+=abs(m[i]-m[j])
	return t


for _ in range(int(input())):
	n,sl = map(int, input().split())
	s = []
	for i in range(n):
		s.append(input())


	min_cost = 1000
	for n,i in enumerate(s):
		for j in s[n+1:]:
			# print(i,j,cost(i,j))
			min_cost = min(min_cost,cost(i,j))

	print(min_cost)

