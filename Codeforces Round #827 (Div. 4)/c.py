count = int(input())
for i in range(count):
    r = [0] * 8
    b = [0] * 8
    total = 0
    while 1:
        row = input()
        if '.' in row or 'B' in row or 'R' in row:
            for j in range(8):
                if row[j] == 'R':
                    r[j] += 1
                elif row[j] == 'B':
                    b[j] += 1
            total += 1
        if total == 8:
            break

    red = 0
    blue = 0
    for i in range(8):
        if r[i] == 1:
            red += 1
        elif r[i] == 8:
            red = 8
        if b[i] == 1:
            blue += 1
        elif b[i] == 8:
            blue = 8

    if red == 8:
        print("R")
    elif blue == 8:
        print("B")
