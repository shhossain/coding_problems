def spell_check(a):
    t = 0
    m = 0
    r = 0
    i = 0
    u = 0

    for c in a:
        if c == "T":
            t += 1
        elif c == "m":
            m += 1
        elif c == "r":
            r += 1
        elif c == "i":
            i += 1
        elif c == "u":
            u += 1
        else:
            return False

        if t > 1 or m > 1 or r > 1 or i > 1 or u > 1:
            return False
    
    if t == 1 and m == 1 and r == 1 and i == 1 and u == 1:
        return True
    else:
        return False



runs = int(input())
for i in range(runs):
    char_len = int(input())
    char_input = input()
    if spell_check(char_input):
        print("YES")
    else:
        print("NO")
