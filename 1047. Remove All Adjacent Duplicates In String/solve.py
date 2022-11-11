class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                s.pop(i)
                s.pop(i)
                i = 0
            else:
                i += 1
        return ''.join(s)


a = "abbaca"
print(Solution().removeDuplicates(a))