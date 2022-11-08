a,b,c = map(int, input().split())

v1 = a/c
if not v1.is_integer():
	v1 = int(v1)+1
v2 = b/c
if not v2.is_integer():
	v2 = int(v2)+1
print(int(v1*v2))