from typing import List


words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words_map = {w: i for i, w in enumerate(words)}
memo = {}
def get_diffrences(a, b):
	v = f"{a}{b}"
	if v in memo:
		return memo[v]
	else:
		val = words_map[b] - words_map[a]
		memo[v] = val
		return val


class Solution:
    def oddString(self, words: List[str]) -> str:
        diff = {}
        for w in words:
            d = []
            len_w = len(w)
            for i in range(len_w):
                if i == 0:
                    continue

                v = get_diffrences(w[i-1],w[i])
                d.append(v)
                i+=1
            str_d = str(d)
            if str_d not in diff:
                diff[str_d] = [w]
            else:
                diff[str_d].append(w)

        
        for k,v in diff.items():
            if len(v) == 1:
                return v[0]




