queries = ["t", "i", "m", "i", "p", "s"]
dictionary = ["w", "j", "b", "p", "u", "b", "u", "i", "h", "m"]


def dist(a, b):
    return sum([1 for i in range(len(a)) if a[i] != b[i]])


final_arr = []
added_indexs = set()
for n, q in enumerate(queries):
    for d in dictionary:
        v = dist(q, d)
        if v <= 2:
            if n not in added_indexs:
                final_arr.append(q)
                added_indexs.add(n)


print(final_arr)
