class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int leftPointer = 0;
        int rightPointer = numbers.size()-1;
        vector<int> result(2);
        while(leftPointer < rightPointer) {
            int sum = numbers[leftPointer] + numbers[rightPointer];
            if(sum < target) {
                leftPointer++;
            } else if(sum > target) {
                rightPointer--;
            } else {
                break;
            }
        }
        result[0] = leftPointer+1;
        result[1] = rightPointer+1;
        return result;
    }
};
