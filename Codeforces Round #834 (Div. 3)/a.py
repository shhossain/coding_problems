for _ in range(int(input())):
    s = input()

    flag = True
    for i in range(len(s)-1):
        if s[i] == "Y" and s[i+1] != "e":
            flag = False
            break

        elif s[i] == "e" and s[i+1] != "s":
            flag = False
            break

        elif s[i] == "s" and s[i+1] != "Y":
            flag = False
            break

    for i in s:
        if i != "Y" and i != "e" and i != "s":
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
