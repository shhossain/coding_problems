def solve(s):
    # slice s in two parts
    s1, s2 = s[:len(s)//2], s[len(s)//2:]

    if s2+s1 == s:
        return True
    else:
        return False


for _ in range(int(input())):
    n = int(input())
    s = input()
    if solve(s):
        print("YES")
    else:
        print("NO")
