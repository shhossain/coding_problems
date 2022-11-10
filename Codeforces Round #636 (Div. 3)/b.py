for _ in range(int(input())):
    n = int(input())

    if n/2%2 != 0:
        print("NO")
        continue

    a = [] 
    b = []
    v = 0
    v2 = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            a.append(i)
            v +=i
        else:
            b.append(i)
            v2+=i


    b[-1] += (v-v2)
    
        

    print("YES")
    print(*a,*b)
    

