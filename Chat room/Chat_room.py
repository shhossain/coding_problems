# ahhellllloou
a = "lheehlolo"


def hello_in(string):
    h = 0
    e = 0
    l = 0
    for i in string:
        if i == 'h':
            h = 1
        elif i == 'e' and h == 1:
            e = 1
        elif i == 'l' and h == 1 and e == 1:
            l += 1
        elif i == 'o' and h == 1 and e == 1 and l > 1:
            return True
    return False


print(hello_in(a))
