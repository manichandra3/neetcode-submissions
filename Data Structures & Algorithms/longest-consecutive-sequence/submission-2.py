class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        find = defaultdict(int)
        res = 0
        for num in nums:
            if not find[num]:
                left = find[num - 1]
                right = find[num + 1]
                total = left + right + 1
                find[num] = total
                find[num - left] = total
                find[num + right] = total
                res = max(res, total)
        return res