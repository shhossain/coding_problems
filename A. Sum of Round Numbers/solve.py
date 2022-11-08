for _ in range(int(input())):
	num = input()
	num_len = len(num)
	n = int(num)

	ans = []
	re = n
	while re != 0:
		re_len = len(str(re))
		# a = 1000 for 5000
		a = int(f"1"+"".zfill(re_len-1))
		v = re//a # 5//2 = 2
		val = v*a
		re = re - val
		ans.append(val)


	alen = len(ans)
	print(alen)
	for i in ans:
		print(i,end=" ")
	print()