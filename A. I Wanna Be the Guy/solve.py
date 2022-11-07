n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x,a = a[0],a[1:]
y,b = b[0],b[1:]




c = [0] * n
for i in a:
	c[i-1] = 1
for i in b:
	c[i-1] = 1

win = True
for i in c:
	if i != 1:
		win = False
		break

if win:
	print("I become the guy.")
else:
	print("Oh, my keyboard!")

