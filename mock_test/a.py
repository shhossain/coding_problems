runs = 10
for i in range(runs):
    a = input()
    if a == "0":
        break
    else:
        int_a = int(a) if a else 0
        last = a[len(a) - 1]
        last = int(last) if last else 0

        remaining = a[0:len(a) - 1]
        remaining = int(remaining) if remaining else 0


        cal = (remaining - (last * 5))
        cal = cal % 17 == 0

        if cal:
            print(1)
        else:
            print(0)
