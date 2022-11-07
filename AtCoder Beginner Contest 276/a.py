a = input()
idx = -1
for n, i in enumerate(a):
    if i == "a":
        idx = n + 1
print(idx)
