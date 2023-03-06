row, col = map(int, input().split())
x, y = map(int, input().split())
p, q = map(int, input().split())
n = int(input())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))


# row
x1, y1 = x+p, y+q
x2, y2 = x+p, y-q

x3, y3 = x-p, y+q
x4, y4 = x-p, y-q

# col
x5, y5 = x+q, y+p
x6, y6 = x+q, y-p

x7, y7 = x-q, y+p
x8, y8 = x-q, y-p

moves = [(x1, y1), (x2, y2), (x3, y3), (x4, y4),
         (x5, y5), (x6, y6), (x7, y7), (x8, y8)]

moves = set(moves)

# check for coliision and if in ab
ct = 0
for i, j in moves:
	if i > row or j > col or i < 1 or j < 1:
		continue
	if (i, j) in ab:
		continue
	ct += 1

print(ct)
