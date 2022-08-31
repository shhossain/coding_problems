def get_points(word_list):
    mem = {}
    for n, i in enumerate(word_list):
        for j in i:
            if j not in mem:
                mem[j] = [n]
            else:
                mem[j].append(n)

    p1 = 0
    p2 = 0
    p3 = 0
    for v in mem.values():
        for i in v:
            if len(v) == 2:
                if i == 0:
                    p1 += 1
                elif i == 1:
                    p2 += 1
                elif i == 2:
                    p3 += 1
            elif len(v) == 1:
                if i == 0:
                    p1 += 3
                elif i == 1:
                    p2 += 3
                elif i == 2:
                    p3 += 3
    return p1, p2, p3


runs = int(input())
for i in range(runs):
    list_len = int(input())
    word_list = []
    for j in range(3):
        word_list.append(input().split())

    p1, p2, p3 = get_points(word_list)
    print(f"{p1} {p2} {p3}")
