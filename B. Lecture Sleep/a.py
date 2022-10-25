n,k = map(int, input().split())
a = list(map(int, input().split()))
sleep = list(map(int, input().split()))

max_sum = 0
max_sum_index = 0
len_a = len(a)
for i in range(len_a):
    sv = sleep[i]
    if sv == 0:
        s = sum(a[i:i+k])
        if s > max_sum:
            max_sum = s
            max_sum_index = i
        
for i in range(max_sum_index, max_sum_index+k):
    sleep[i] = 1

total = 0
for i in range(len_a):
    if sleep[i] == 1:
        total += a[i]

print(total)
