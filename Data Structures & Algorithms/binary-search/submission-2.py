class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = r - (r-l)//2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            if nums[m] < target:
                l = m + 1
        return -1

