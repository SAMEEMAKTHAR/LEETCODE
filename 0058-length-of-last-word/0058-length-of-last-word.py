class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        ans=len(a[-1])
        return ans
        