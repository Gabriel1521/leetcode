class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param nums int整型vector
     * @return int整型
     */
    int mod = 1000000007;
    int merge_sort(vector<int>& nums, int l, int h, vector<int>& store){
        if (l >= h){
            return 0;
        }

        int mid = (l+h)/2;
        int res = merge_sort(nums, l, mid, store) + merge_sort(nums, mid+1, h, store);
        res %= mod;

        int i = l;
        int j = mid+1;

        for (int k=l;k<=h;k++){
            store[k] = nums[k];
        }

        for (int k=l;k<=h;k++){
            if (i==mid+1){
                nums[k] = store[j];
                j += 1;
            }
            else if (j==h+1 || store[i] <= store[j]){
                nums[k] = store[i];
                i += 1;
            }else{
                nums[k] = store[j];
                j += 1;
                res += mid - i + 1;
            }
        }

        return res%mod;
    }

    int InversePairs(vector<int>& nums) {
        // write code here
        vector<int> store(nums.size(),0);
        int result = merge_sort(nums,0,nums.size()-1,store);
        return result%mod;
    }
};
