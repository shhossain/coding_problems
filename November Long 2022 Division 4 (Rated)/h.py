def starting(bstr):
    # 00100 start is 100
    f = bstr.find("1")
    if f == -1:
        return "0"
    else:
        return bstr[f:]


def op(s1, s2, size):
    count = 0
    for i in range(size):
        if s1[i] != s2[i]:
            count += 1
    return count//2


def solve(bstr):
    bstr = starting(bstr)

    if bstr == "0":
        return 0

    length = len(bstr)
    start = "1" + "0" * (length - 1)
    end = "1" * length
    sint = int(start, 2)
    eint = int(end, 2)

    bones = bstr.count("1")

    arr = []
    for i in range(sint, eint + 1):
        if i % 3 == 0:
            arr.append(i)

    farr = []
    flag = False
    for i in arr:
        ibin = bin(i)[2:]
        if ibin.count("1") == bones:
            flag = True
            farr.append(ibin)

    if not flag:
        return -1

    m = {}  # binary: operations
    for i in farr:
        m[i] = op(bstr, i, length)

    # sort by operations
    m = dict(sorted(m.items(), key=lambda item: item[1]))

    # return the first operation
    return m[list(m.keys())[0]]


for _ in range(int(input())):
    s = input()
    print(solve(s))
