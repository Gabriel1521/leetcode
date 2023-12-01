class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param number int整型
     * @return int整型
     */
    int jumpFloor(int number) {
        // write code here
        vector<int> dp(number+1,0);

        for (int i=0;i<=number;i++){
            if (i <= 1){
                dp[i] = 1;
            }
            else{
                dp[i] = dp[i-1] + dp[i-2];
            }
        }

        return dp[number];
    }
};
