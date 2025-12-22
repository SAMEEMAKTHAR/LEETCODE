class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            b=str(i)
            b.split()
            if len(list(b))%2==0:
                a+=1
        return a