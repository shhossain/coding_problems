for _ in range(int(input())):
	x,y,x = map(int,input().split())
	min_idx = min(x,y,z)
	print(["ALICE","BOB","CHARLIE"][min_idx])
	