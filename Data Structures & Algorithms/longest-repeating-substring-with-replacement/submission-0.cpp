class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> count(26, 0);  
        int maxFreq = 0;           
        int l = 0;                 
        
        int res = 0;               // Result to store the max length of valid window

        for (int r = 0; r < s.size(); r++) {
            count[s[r] - 'A']++;
            maxFreq = max(maxFreq, count[s[r] - 'A']);  // Update max frequency in the window

            // Check if the current window can be made valid with at most k replacements
            if ((r - l + 1) - maxFreq > k) {
                // Move the left pointer if we need more than k replacements
                count[s[l] - 'A']--;
                l++;
            }

            // Update result as the max length of the window
            res = max(res, r - l + 1);
        }

        return res;
    }
};
