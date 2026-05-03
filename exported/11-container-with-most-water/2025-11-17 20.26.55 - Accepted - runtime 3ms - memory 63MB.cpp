class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int area = 0;

        while(left<right){
            int temp = (right - left) * std::min(height[left], height[right]); // get area
            area = std::max(temp, area); // area 

            if (height[left] > height[right]){
                right--; 
            }

            else if (height[left] < height[right]){
                left++;
            }

            else{
                left++;
                right--;
            }
        }
        return area;
    }
};