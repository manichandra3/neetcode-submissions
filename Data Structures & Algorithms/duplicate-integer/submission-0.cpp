class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        bool flag = false;
        for(const auto& num : nums) {
            mp[num]++;
            if(mp[num]>1){
                flag = true;
                break;
            }
        }
        return flag;
    }
};
