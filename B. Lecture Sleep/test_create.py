import random
import time

# sample testcase
# 6 4
# 1 20 5 2 5 20
# 0 0 0 0 0 0


def create_testcase():
    # n limit 10^5
    n = random.randint(1, 100000)
    k = random.randint(1, n)
    a = []
    sleep = []
    for i in range(n):
        a.append(random.randint(1, 100000))
        sleep.append(random.randint(0, 1))
    return n, k, a, sleep


def run(n, k, a, sleep):
    max_sum = 0
    max_sum_index = 0
    len_a = n
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
    return total


# run 1000 times and test the time
for i in range(1000):
    n, k, a, sleep = create_testcase()
    print("n: ", n, "k: ", k)
    start = time.time()
    run(n, k, a, sleep)
    end = time.time()
    print(end - start)
