n = input()
cards = list(map(int, input().split()))
sereja = 0
dima = 0
for i in range(int(n)):
    if i % 2 == 0:
        max_num = max(cards[0], cards[-1])
        sereja += max_num
        cards.remove(max_num)
    else:
        max_num = max(cards[0], cards[-1])
        dima += max_num
        cards.remove(max_num)
print(sereja, dima)
