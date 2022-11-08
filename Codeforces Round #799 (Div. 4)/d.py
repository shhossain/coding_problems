def check_palindrome(s):
	return s == s[::-1]

def add_time(cur_time,add_mins):
	hh,mm = cur_time.split(':')
	hh = int(hh)
	mm = int(mm)
	mm += add_mins
	hh += mm//60
	mm = mm%60
	hh = hh%24
	return str(hh).zfill(2)+':'+str(mm).zfill(2)

def get_times(cur_time,add_min):
	times = []
	while True:
		cur_time = add_time(cur_time,add_min)
		if cur_time in times:
			break
		times.append(cur_time)
	return times

for _ in range(int(input())):
	s,m = input().split()
	m = int(m)
	times = get_times(s,m)
	p = 0
	for i in range(len(times)):
		if check_palindrome(times[i]):
			p += 1
	print(p)










