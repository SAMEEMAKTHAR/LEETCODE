class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        inputt=re.sub(r"[^a-z0-9]","",s.lower())
        check=inputt[::-1]
        if list(inputt)==list(check):
            return True
        else:
            return False
        
        
       
       