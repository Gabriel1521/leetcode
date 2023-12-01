class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param array int整型vector
     * @return int整型vector
     */
    vector<int> FindGreatestSumOfSubArray(vector<int>& array) {
        // write code here
        int n = array.size();
        vector<int> dp(n,0);

        int left = 0, right = 0;
        int res_l = 0, res_r = 0;
        int max_num = 0;
        for (int i=0;i<n;i++){
            if (i==0){
                dp[i] = array[i];
                max_num = dp[i];
            }
            else{
                right++;
                dp[i] = max(dp[i-1]+array[i], array[i]);
                if (dp[i-1]+array[i] < array[i]){
                    left = right;
                }
                if (max_num < dp[i] || (max_num == dp[i] && ((right-left+1)>(res_r-res_l+1)))){
                    max_num = dp[i];
                    res_l = left;
                    res_r = right;
                }
            }
        }

        vector<int> result;
        for (int j=res_l;j<res_r+1;j++){
            result.push_back(array[j]);
        }

        return result;
    }
};
