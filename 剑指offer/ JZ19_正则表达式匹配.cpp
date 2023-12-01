class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param str string字符串
     * @param pattern string字符串
     * @return bool布尔型
     */
    bool match(string str, string pattern) {
        // write code here
        int n1 = str.length();
        int n2 = pattern.length();

        vector<vector<bool>> dp(n1+1, vector<bool>(n2+1, false));

        dp[0][0] = true;

        for (int i=2;i<=n2;i++){
            if (pattern[i-1]=='*'){
                dp[0][i] = dp[0][i-2];
            }
        }

        for (int i=1;i<=n1;i++){
            for (int j=1;j<=n2;j++){
                if (pattern[j-1]!='*' && (pattern[j-1] == '.' || pattern[j-1] == str[i-1])){
                    dp[i][j] = dp[i-1][j-1];
                }
                else if (j >=2 && pattern[j-1] == '*'){
                    if (pattern[j-2] == '.' || pattern[j-2] == str[i-1]){
                        dp[i][j] = dp[i-1][j] || dp[i][j-2];
                    }
                    else{
                        dp[i][j] = dp[i][j-2];
                    }
                }
            }
        }

        return dp[n1][n2];

    }
};
