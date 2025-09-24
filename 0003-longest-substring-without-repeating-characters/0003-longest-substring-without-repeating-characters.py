class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        dic={}
        value=0
        r=0
        l=0
        while r<len(s):
            if s[r] in dic:
                ans=max(ans,value)
                value=0
                dic.clear()
                l+=1
                r=l
            else:
                dic[s[r]]=True
                value+=1
                r+=1
            ans=max(ans,value)
        return ans


            

        
            


        
        