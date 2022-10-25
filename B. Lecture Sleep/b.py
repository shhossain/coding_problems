from time import sleep


a = [1, 5, 1, 9, 6, 11, 3, 1, 7]
s = [0, 1, 0, 0, 1, 0, 1, 0, 0]

# 1 3 5 2 5 4
# 1 1 0 1 0 0

a = [1, 3, 5, 2, 5, 4]
s = [1, 1, 0, 1, 0, 0]


max_sum = 0
current_index = 0
arr = [0] * len(a)
for i in range(len(a)):
    sv = s[i]
    if i % 3 == 0:
        current_index = i
        if sv == 0:
            arr[i] = a[i]
    else:
        if sv == 0:
            arr[current_index] += a[i]

print(arr)
total = max(arr)
print(total)
for i in range(len(s)):
    if s[i] == 1:
        total += a[i]

print(total)
