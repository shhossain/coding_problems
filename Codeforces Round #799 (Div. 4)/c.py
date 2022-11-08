from collections import defaultdict


for _ in range(int(input())):
	a = input()

	board = {}

	for i in range(8):
		for j in range(8):
			board[f"{i},{j}"] = 0

	board = defaultdict(lambda:-1,board)

	b = []
	for i in range(8):
		s = input()
		for j in range(8):
			if s[j] =="#":
				b.append((i,j))
				board[f"{i},{j}"] = 1

	pos = (0,0)
	for i,j in b:
		p1 = f"{i-1},{j+1}"
		p2 = f"{i+1},{j-1}"
		p3 = f"{i-1},{j-1}"
		p4 = f"{i+1},{j+1}"

		if board[p1] == 1 and board[p2] == 1 and board[p3] == 1 and board[p4]:
			pos = (i+1,j+1)
			break

	print(pos[0],pos[1])