class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        int x;
        int y;
        
        for(int i = 0; i < nums.size(); i++) {
            for(int j = 0; j < nums.size(); j++) {
                if(nums.at(i) + nums.at(j) == target && i != j) {
                    x = i;
                    y = j;
                }
            }
        }
        
        
        return {x, y};
    }
};