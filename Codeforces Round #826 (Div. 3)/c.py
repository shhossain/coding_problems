def binary_search(arr,s,t):
    e = len(arr) - 1
    while s<=e:
        mid = (s+e)//2
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            s = mid + 1
        else:
            e = mid - 1
    return -1




for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    apre = []
    s = 0
    for i in range(n):
        s+=a[i]
        apre.append(s)

    # print(apre)

    mans = n
    for i in range(n):
        val = apre[i]
        m = 2

        v = binary_search(apre,i+1,val*m)

        m+=1
        ans = [v-1]

        flag = True
        if v != -1:
            while v<n:
                v1 = binary_search(apre,v,val*m)
                if v1 == -1:
                    flag = False
                    break

                else:
                    ans.append((v+1)-v1)
                    v = v1 + 1
                    m+=1

            # print(ans)
            if flag:
                a = max(ans)
                mans = min(mans,a)
    if mans == 0:
        mans = 1
    print(mans)


