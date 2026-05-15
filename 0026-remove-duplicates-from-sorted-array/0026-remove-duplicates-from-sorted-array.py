class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        a=1
        while a<len(nums):
            if nums[a]==nums[a-1]:
                nums.remove(nums[a])
            else:
                a+=1
                k+=1
        return a


        