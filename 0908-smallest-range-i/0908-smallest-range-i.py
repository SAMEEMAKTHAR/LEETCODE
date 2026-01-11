class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minn=min(nums)
        maxx=max(nums)
        a=[]
        b=[]
        for i in range(minn,minn+k+1):
            a.append(i)
        key=max(a)
        for i in range(maxx,maxx-(k+1),-1):
            b.append(i)
        print(a)
        print(b)
        for i in a:
            if i in b:
                return 0
        return min(b)-max(a)
        
    
