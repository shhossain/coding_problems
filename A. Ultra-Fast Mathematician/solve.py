a = list(map(int, input()))
b = list(map(int, input()))

c = ""
for i in range(len(a)):
	v1 = a[i]
	v2 = b[i]
	v = v1 + v2
	if v == 1:
		c+="1"
	else:
		c+="0"

print(c)

