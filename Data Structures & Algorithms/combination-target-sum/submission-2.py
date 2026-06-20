class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # array of distinct integers: nums
        # target integer: target
        # repetition with replacement
        # combinations are same if frequency of each chosen numbers is same
        # return unique combinations of nums where the numbers sum up to target
        res = []
        subset = []
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return 
            if i >= len(nums) or total > target:
                return
            subset.append(nums[i])
            dfs(i, total + nums[i])
            subset.pop()
            dfs(i+1, total)
        dfs(0,0)
        return res