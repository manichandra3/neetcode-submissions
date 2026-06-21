class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        def findm(array,l,r):
            m = (l+r)//2
            if l==r:
                return array[l]
            if array[l]<array[r]:
                return array[l]
            if array[m]>array[r]:
                return findm(array,m+1,r)
            if array[m]<array[r]:
                return findm(array,l,m)
        return findm(nums,0,len(nums)-1)
