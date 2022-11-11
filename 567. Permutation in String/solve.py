from collections import defaultdict

def solve(s1, s2):
    n = len(s2)
    n1 = len(s1)

    # m1 is substring
    m1 = defaultdict(int)
    for i in range(n1):
        m1[s1[i]] = m1.get(s1[i],0) + 1
    m2 = defaultdict(int)
    for i in range(n):
        m2[s2[i]] = m2.get(s2[i],0) + 1

    if m1 == m2:
        return True
    
    s = 0
    e = n1
    while e <= n:
        ts2 = s2[s:e]
        tm2 = defaultdict(int)
        for i in ts2:
            tm2[i]+=1
        if m1 == tm2:
            return True
        s+=1
        e+=1

    return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return solve(s1, s2)


# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

print(solve("ab", "aab"))
print(solve("ab", "ab"))
