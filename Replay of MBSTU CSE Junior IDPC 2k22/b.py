

def solve(n, k, arr):
    m = {}
    for i in range(n):
        m[a[i]] = i

    m = sorted(m.items(), key=lambda x: x[0])
    g = 0
    s = 0
    c = None
    for _,idx in m:
    	if c == None:
    		c = idx
    		continue

    	if c < idx:
    		c = idx
    		s+=1
    	else:
    		g+=1
    		c = idx
    		s = 1
    
    if g == 1 and s <= k:
    	return True

    return False



for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if solve(n, k, a):
        print("Yes")
    else:
        print("No")
