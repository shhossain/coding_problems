def valid(s:str) -> bool:
    # a-z, A-Z, 0-9
    if s.isalnum():
        return True
    return False


def is_palindrome(s:str):
    s1 = 0
    e1 = len(s) - 1
    while s1<e1:
        if not valid(s[s1]):
            s1+=1
            continue
        if not valid(s[e1]):
            e1-=1
            continue
        if s[s1].lower() != s[e1].lower():
            return False
        s1+=1
        e1-=1
    return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return is_palindrome(s)

        


