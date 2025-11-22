class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        b=a[::-1]
        if list(a)==list(b):
            return True
        else:
            return False