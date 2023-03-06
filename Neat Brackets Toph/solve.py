a = input()
ct = 0
b1,b2 = 0,0

for i in a:
	if i == "(":
		ct+=1
		b1+=1
	else:
		if ct > 0:
			ct -= 1
		b2+=1

if b1 != b2:
	ct+=1

print("Yes" if ct == 0 else "No")
