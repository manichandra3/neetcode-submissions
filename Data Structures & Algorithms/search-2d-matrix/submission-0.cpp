class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int ROWS = matrix.size();
        int COLS = matrix[0].size();
        
        for(int i = 0; i < ROWS; i++){
            int first = matrix[i][0];
            int last = matrix[i][COLS - 1];
            
        
            if(first <= target && target <= last){
                if(binarySearch(matrix[i], 0, COLS - 1, target)){
                    return true;
                }
            }
        }
        return false;
    }
    
private:
    bool binarySearch(vector<int>& arr, int l, int r, int target){
        while(l <= r){
            int m = l + (r - l) / 2; 
            
            if(arr[m] == target){
                return true;
            } else if(arr[m] < target){
                l = m + 1; 
            } else {
                r = m - 1; 
            }
        }
        return false;
    }
};
