#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, float>> cars;
        
        // Calculate time to reach the target for each car and pair with its position
        for(int i = 0; i < n; i++) {
            float time = (float)(target - position[i]) / speed[i];
            cars.push_back({position[i], time});
        }
        
        // Sort cars based on their position
        sort(cars.rbegin(), cars.rend());  // Sort in descending order by position
        
        int res = 0;
        float lastTime = 0;
        
        // Calculate the number of fleets
        for(int i = 0; i < n; i++) {
            if(cars[i].second > lastTime) {
                lastTime = cars[i].second;
                res++;
            }
        }
        
        return res;
    }
};
