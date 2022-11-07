for _ in range(int(input())):
    a,b = map(int, input().split())
    if (a*2) > (b*5):
        print("Chocolate")
    elif (a*2) < (b*5):
        print("Candy")
    else:
        print("Either")