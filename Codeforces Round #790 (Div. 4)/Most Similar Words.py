def diff(word1,word2):
	d = 0
	for w1,w2 in zip(word1,word2):
		d += abs(ord(w1) - ord(w2))
	return d


for _ in range(int(input())):
	n,m = map(int, input().split())

	words = []
	for i in range(n):
		words.append(input())


	d = 10000
	for i in range(n):
		for j in range(i+1,n):
			d = min(d, diff(words[i],words[j]))
	print(d)