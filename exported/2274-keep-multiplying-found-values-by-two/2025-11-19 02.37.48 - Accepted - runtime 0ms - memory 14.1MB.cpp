class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        int current = original;


        while (true){
            auto idx = std::find(nums.begin(), nums.end(), current);
            if (idx == nums.end()){
                return current;
            }
            current *= 2;
        }

        return 0;
    }
};