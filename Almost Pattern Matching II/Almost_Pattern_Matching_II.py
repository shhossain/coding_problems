# import time

# tests = 1200000 * 'ab'

memo = {}
def humming_distance(s1, s2):
    if (s1, s2) in memo:
        return memo[(s1, s2)]
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    memo[(s1, s2)] = dist
    return dist
    


runs = int(input())
# runs = 1
memo2 = {}
for i in range(runs):
    s, pattern, k = input().split()
    # s, pattern, k = tests, 'abababab', 1
    if (s, pattern, k) in memo2:
        print(memo2[(s, pattern, k)])
        continue

    k = int(k)
    count = 0
    pat_len = len(pattern)
    for i in range(len(s) - pat_len + 1):
        if humming_distance(s[i:i+pat_len], pattern) <= k:
            count += 1
    memo2[(s, pattern, k)] = count
    print(count)
    count = 0


