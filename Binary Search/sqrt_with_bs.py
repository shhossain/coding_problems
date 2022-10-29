def sqrtInt(num):
	s = 0
	e = num//2
	ans = -1
	while s <= e:
		mid = (s+e)//2
		v = mid*mid
		if v == num:
			return mid
		elif v > num:
			e = mid - 1
		else:
			ans = mid
			s = mid + 1
	return ans

def cube_root_int(x):
	s = 0
	e = x
	ans = -1
	while s <= e:
		mid = (s+e)//2
		v = (mid*mid*mid)
		if v==x:
			return mid
		elif v > x:
			e = mid - 1
		else:
			ans = mid 
			s = mid + 1
	return ans


def morePrecision(num,p,tempans):
	ans = tempans
	factor = 1

	if (tempans*tempans) == num:
		return tempans

	for i in range(p):
		factor = factor/10

		j = factor
		while 1:
			if (j*j) < num:
				ans = j
			else:
				break
			j+=factor
	return float(str(ans)[:p+2])



i = int(input())
ans = sqrtInt(i)
print(ans)
ans3 = cube_root_int(i)
# print(ans3)
# print(morePrecision(i,5,ans3))
