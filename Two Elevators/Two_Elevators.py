runs = int(input())
for _ in range(runs):
    a, b, c = map(int, input().split())
    first_lift_distance = abs(1 - a)
    second_lift_distance = abs(1 - c) + abs(c - b)
    if first_lift_distance < second_lift_distance:
        print(1)
    elif first_lift_distance > second_lift_distance:
        print(2)
    else:
        print(3)
