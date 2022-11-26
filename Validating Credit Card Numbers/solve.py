from collections import defaultdict
import re


for _ in range(int(input())):
	s = input()

	groups = []
	if "-" in s:
		groups = s.split("-")
	else:
		st=0
		e=4
		while e < len(s) + 1:
			groups.append(s[st:e])

			st+=4
			e+=4

	print(groups)

		



