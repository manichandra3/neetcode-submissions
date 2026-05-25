class Solution {
public:
    int search(vector<int>& nums, int target) {
        int r = 0;
        int l = nums.size()-1;
        binarySearch(nums, target, r, l);
    }

private:
    int binarySearch(vector<int>&nums, int target, int r, int l) {
        if(r>l){
            return -1;
        }
        int m = r + (l-r)/2;

        if (nums[m] == target) {
            return m;
        }
        if (nums[m] > target) {
            return binarySearch(nums, target, r, m - 1);
        }
        return binarySearch(nums, target, m + 1, l);
    }
};
