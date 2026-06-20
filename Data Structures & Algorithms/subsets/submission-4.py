class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = [([],0)]
        while stack:
            subset, i = stack.pop()
            if i == len(nums):
                res.append((subset))
                continue
            stack.append((subset,i+1))
            stack.append((subset+[nums[i]],i+1))
        return res