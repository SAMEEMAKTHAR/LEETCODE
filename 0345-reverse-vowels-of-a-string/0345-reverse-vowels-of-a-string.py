class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        a=["a","A","E","e","I","i","O","o","U","u"]
        left=0
        right=len(s)-1
        while left<right:
            if s[left] in a and s[right] not in a:
                right-=1
            elif s[right] in a and s[left] not in a:
                left+=1
            elif s[left] and s[right] in a:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            else:
                left+=1
                right-=1
        return "".join(s)

        