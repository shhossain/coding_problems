mem = {}

def ans(n):
	if n == 0:
		return 1
	if n in mem:
		return mem[n]
	else:
		v = ans(n//2) + ans(n//3)
		mem[n] = v
		return v

print(ans(int(input())))