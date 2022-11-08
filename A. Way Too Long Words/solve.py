for _ in range(int(input())):
	s = input()
	s_len = len(s)
	if s_len > 10:
		print(f"{s[0]}{s_len-2}{s[-1]}")
	else:
		print(s)