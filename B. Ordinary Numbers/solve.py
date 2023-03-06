for _ in range(int(input())):
	n = int(input());nl = len(str(n))
	print((n//(int("1"*nl))) + (9 * (nl-1)))
	
