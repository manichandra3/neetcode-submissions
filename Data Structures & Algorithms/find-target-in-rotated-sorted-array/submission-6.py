class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def findMin(nums: List[int]) -> int:
            l,r = 0,len(nums)-1
            while l<r:
                if nums[l] < nums[r]:
                    return l
                m = (l+r)//2
                if nums[m] > nums[r]:
                    l = m+1
                if nums[r] > nums[m]:
                    r = m 
            return l
        offset=findMin(nums)
        def vbis(nums,target,offset):
            l,r = 0,len(nums)-1
            while l<=r:
                vm = (l+r)//2
                m = (vm+offset)%len(nums)
                if nums[m]==target:
                    return m
                if nums[m]<target:
                    l = vm+1
                if nums[m]>target:
                    r = vm-1
            return -1
        res = vbis(nums,target,offset)
        return res

