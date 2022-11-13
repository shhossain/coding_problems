from collections import defaultdict
from bisect import bisect_left



letters = "abcdefghijklmnopqrstuvwxyz"
lm = {}
ml = {}
for i in range(0,26):
	lm[letters[i]] = i+1
	ml[i+1] = letters[i]




for _ in range(int(input())):
	w = input()
	x = int(input())

	w_len = len(w)

	arr = []
	idx = defaultdict(list)
	for n,i in enumerate(w):
		arr.append(lm[i])
		idx[lm[i]].append(n)


	arr.sort()
	sm = 0
	parr = []
	for i in arr:
		sm+=i
		parr.append(sm)


	if sm <= x:
		print(w)
		continue

	# val = binary_search(parr,x)
	val = bisect_left(parr,x,0,len(parr))

	dx = val
	if val == w_len:
		val -= 1

	if parr[val] == x:
		dx+=1

	ans = arr[:dx]
	

	temp = {}
	for i in range(len(ans)):
		v = idx[ans[i]].pop(0)
		temp[v] = ans[i]
		
	tempk = sorted(temp)
	temp_str = ""
	for i in tempk:
		temp_str += ml[temp[i]]

	print(temp_str)

	