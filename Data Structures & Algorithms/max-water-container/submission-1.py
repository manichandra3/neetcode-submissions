class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        curr_max=max_area = 0
        while l<r:
            curr_max = min(heights[r],heights[l])*(r-l)
            max_area=max(curr_max,max_area)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1 
        return max_area
