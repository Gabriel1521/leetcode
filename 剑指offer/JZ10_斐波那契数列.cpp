class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param n int整型
     * @return int整型
     */
    int Fibonacci(int n) {
        // write code here
        int dp[n];
        dp[0] = 1;
        dp[1] = 1;

        for (int i=2;i<n;i++){
            dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n-1];
    }
};

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param n int整型
     * @return int整型
     */
    int Fibonacci(int n) {
        // write code here
        if (n==1|| n==2)    return 1;

        int a = Fibonacci(n-1);
        int b = Fibonacci(n-2);

        return a + b;

    }
};
