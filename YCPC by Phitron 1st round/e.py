while 1:
	try:
		st = input()

		s,e=0,len(st)-1
		op = 0
		while s <= e:
			if st[s] != st[e]:
				op+=1
			s+=1
			e-=1
		print(op)
	except EOFError:
		break