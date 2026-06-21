class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # abc
        # lecabee
        # take a window of size s1 inside s2 and move it when ever we donot have a char from s1 in s2
        # lecabee
        # lec->eca->cab=>found
        if len(s1) > len(s2):
            return False
            
        l = 0
        # sorted() returns a list, so we keep sorted_s1 as a list for comparison
        sorted_s1 = sorted(s1) 
        
        while l <= len(s2) - len(s1):
            # Extract the window and sort it
            window = s2[l : l + len(s1)]
            sorted_window = sorted(window)
            
            # Compare the two sorted lists
            if sorted_s1 == sorted_window:
                return True
            
            # Slide the window
            l += 1
            
        return False