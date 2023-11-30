class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param nums int整型vector
     * @return int整型
     */
    int binary_search(vector<int>& nums, int l, int h){
        while (l < h){
            int m = (l+h)/2;
            if (nums[m] > nums[h])
                l = m+1;
            else if (nums[m] < nums[l])
                h = m;
            else h -= 1;
        }
        return l;

    }


    int minNumberInRotateArray(vector<int>& nums) {
        // write code here
        int idx = binary_search(nums, 0, nums.size()-1);
        return nums[idx];

    }
};
