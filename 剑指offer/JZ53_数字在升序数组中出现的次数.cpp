class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param nums int整型vector
     * @param k int整型
     * @return int整型
     */
    int binary_search(vector<int>& nums, float num){
        int l = 0;
        int h = nums.size()-1;

        int mid = 0;
        while (l<=h){
            mid = (l+h)/2;
            if (nums[mid] < num){
                l = mid + 1;
            }
            else if (nums[mid] > num){
                h = mid - 1;
            }
        }
        return l;
    }

    int GetNumberOfK(vector<int>& nums, int k) {
        // write code here
        int length = binary_search(nums,k+0.5) - binary_search(nums,k-0.5);
        return length;
    }
};
