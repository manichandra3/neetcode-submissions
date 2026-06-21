class Solution:
    def findMin(self, nums: List[int]) -> int:
        p = len(nums) - 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                p = i
                break 
        
        if p == len(nums) - 1:
            return nums[0]
            
        return nums[p + 1]