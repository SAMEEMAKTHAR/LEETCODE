class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans=[]
        a=Counter(arr)
        for i,j in a.items():
            if i==j:
                ans.append(i)
        if ans:
            return max(ans)
        return -1
        
            

        