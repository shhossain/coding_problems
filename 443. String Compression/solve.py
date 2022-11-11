from collections import defaultdict
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        arr = []
        m = defaultdict(int)
        for i in chars:
            m[i]+=1
        
        for k,v in m.items():
            arr.append(k)
            if v > 1:
                v1 = list(str(v))
                arr.extend(v1)
        return arr

a = ["a","a","b","b","c","c","c"]
print(Solution().compress(a))