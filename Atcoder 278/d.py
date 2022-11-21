def valid(a,b):
	s1 = str(a)
	s2 = str(b)

	if len(s1) == 1:
		s1 += "0"
	if len(s2) == 1:
		s2 += "0"
	
	r1 = s1[0] + s2[0]
	r2 = s1[1] + s2[1]


	if int(r1) <= 23 and int(r2) <= 59:
		return True

	return False





a,b = map(int, input().split())
ab = a * 59 + b

d = 10000
ans = (a,b)
for h in range(24):
	for m in range(60):
		# print(h,m)
		if valid(h,m):
			hm = h * 59 + m
			diff = hm - ab

			if diff < d and diff >= 0:
				d = diff
				ans = (h,m)
			

print(*ans)

				






