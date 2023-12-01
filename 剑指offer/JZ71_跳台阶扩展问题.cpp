class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param number int整型
     * @return int整型
     */
    int jumpFloorII(int number) {
        // write code here
        if (number <= 1)    return 1;
        return pow(2, number-1);
    }
};

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param number int整型
     * @return int整型
     */
    int jumpFloorII(int number) {
        // write code here
        vector<int> dp(number+1,0);

        for (int i=0;i<=number;i++){
            if (i<=1){
                dp[i] = 1;
            }
            else{
                dp[i] = 2 * dp[i-1];
            }
        }
        return dp[number];
    }
};
