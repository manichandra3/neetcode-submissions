from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        # 1. Renamed to two_sum
        def two_sum(array, target):
            l, r = 0, len(array) - 1
            pairs = [] # 4. Store all valid pairs, don't just return the first one
            
            while l < r:
                curr_sum = array[l] + array[r]
                
                if curr_sum == target:
                    pairs.append([array[l], array[r]])
                    # Move both pointers to look for MORE pairs
                    l += 1
                    r -= 1
                    
                    # 5. Skip duplicates for the left pointer
                    while l < r and array[l] == array[l - 1]:
                        l += 1
                        
                elif curr_sum > target:
                    r -= 1
                else: # curr_sum < target
                    l += 1
                    
            return pairs # Return the list of all found pairs

        for i in range(len(nums)):
            # 5. Skip duplicates for the fixed number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            curr = nums[i]
            # 2. Pass the correct target (-curr)
            valid_pairs = two_sum(nums[i+1:], -curr)
            
            # 3. Combine the fixed number with each found pair
            for pair in valid_pairs:
                ans.append([curr, pair[0], pair[1]])
                
        return ans