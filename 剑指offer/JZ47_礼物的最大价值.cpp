class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param grid int整型vector<vector<>>
     * @return int整型
     */
    int maxValue(vector<vector<int> >& grid) {
        // write code here
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>> dp(m, vector<int>(n, 0));
        dp[0][0] = grid[0][0];

        for (int i=1;i<m;i++){
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        for (int j=1;j<n;j++){
            dp[0][j] = dp[0][j-1] + grid[0][j];
        }

        for (int i=1;i<m;i++){
            for (int j=1;j<n;j++){
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + grid[i][j];
            }
        }

        return dp[m-1][n-1];
    }
};
