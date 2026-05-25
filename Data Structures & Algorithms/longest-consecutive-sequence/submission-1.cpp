class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;

        for (int n : numSet) {
            // if n doesn't have any left neighbours.
            if (numSet.find(n - 1) == numSet.end()) {
                int length = 1;
                // iter until n has no right neighbour in the set.
                while (numSet.find(n + length) != numSet.end()) {
                    length++;
                }
                longest = max(length, longest);
            }
        }
        return longest;
    }
};
