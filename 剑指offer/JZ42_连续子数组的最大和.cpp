#include <algorithm>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param array int整型vector
     * @return int整型
     */
    int FindGreatestSumOfSubArray(vector<int>& array) {
        // write code here
        int n = array.size();
        vector<int> dp(n,0);

        for (int i=0;i<n;i++){
            if (i==0){
                dp[i] = array[i];
            }
            else{
                dp[i] = max(dp[i-1]+array[i],array[i]);

            }
        }

        int result = *std::max_element(dp.begin(), dp.end());
        return result;
    }
};

#include <algorithm>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param array int整型vector
     * @return int整型
     */
    int FindGreatestSumOfSubArray(vector<int>& array) {
        // write code here
        int n = array.size();
        int a = 0;
        int max_sum = 0;

        for (int i=0;i<n;i++){
            if (i==0){
                a = array[i];
                max_sum = a;
            }
            else{
                a = max(a+array[i],array[i]);
            }
            max_sum = max(a,max_sum);
        }

        return max_sum;
    }
};
