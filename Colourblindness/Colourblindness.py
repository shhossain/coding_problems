def identical(a, b):
    a = a.replace("G", "B")
    b = b.replace("G", "B")
    return a == b


runs = int(input())
for i in range(runs):
    char_len = int(input())
    a = input()
    b = input()
    if identical(a, b):
        print("YES")
    else:
        print("NO")
