class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre=[0]*len(nums)
        post=[0]*len(nums)
        res=[0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
            else:
                pre[i] = pre[i-1]*nums[i-1]
        for i in range(len(nums)):
            r=len(nums)-i-1
            if i == 0:
                post[r] = 1
            else:
                post[r] = post[r+1]*nums[r+1]
        for i in range(len(nums)):
            res[i] = pre[i]*post[i]
        return res  