class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ab={}
        for i,num in enumerate(nums):
            dif=target-nums[i]
            if dif in ab:
                return [ab[dif],i]
            ab[num]=i
        return
        