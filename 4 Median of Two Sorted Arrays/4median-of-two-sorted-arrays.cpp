class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        int n = nums1.size();
        int m = nums2.size();
        if(n > m) return findMedianSortedArrays(nums2, nums1);
        int l = 0, r = n;
        while(l <= r){
            int partX = (l + r) / 2;
            int partY = (n + m + 1) / 2 - partX;
            int maxLeftX = (partX == 0) ? INT_MIN : nums1[partX - 1];
            int minRightX = (partX == n) ? INT_MAX : nums1[partX];
            int maxLeftY = (partY == 0) ? INT_MIN : nums2[partY - 1];
            int minRightY = (partY == m) ? INT_MAX : nums2[partY];
            if(maxLeftX <= minRightY && maxLeftY <= minRightX){
                if((n + m) % 2 == 0){
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0;
                }else{
                    return max(maxLeftX, maxLeftY);
                }
            }else if(maxLeftX > minRightY){
                r = partX - 1;
            }else{
                l = partX + 1;
            }
        }
        return 0.0;
    }
};