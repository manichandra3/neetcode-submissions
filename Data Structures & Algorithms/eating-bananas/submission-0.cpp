class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // piles
        // piles[i] in ith pile
        // h time to eat all bananas in pile
        // choose a pile and eat k banana from that pile
        // return k such that you can eat all the bananas within h hours.
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());
        sort(piles.begin(), piles.end());
        int res = r;
        while(l<=r) {
            int k = l+(r-l)/2;
            long long totalTime=0;
            for(int i = 0; i < piles.size(); i++){
                totalTime += (piles[i]+k-1)/k;
            }
            // satisfies
            if(totalTime<=h){
                res = k;
                r = k - 1;
            } else {
                l = k + 1;
            }
        }
        return res;
    }
};
