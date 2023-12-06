class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param s string字符串
     * @return int整型
     */
    int lengthOfLongestSubstring(string s) {
        // write code here
        unordered_map<char,int> map;
        int res=0;

        vector<int> dp(s.length()+1,0);

        for (int i=1;i<s.length()+1;i++){
            if (map.find(s[i-1])==map.end()){
                dp[i] = dp[i-1] + 1;
            }
            else{
                dp[i] = min(dp[i-1]+1, i - map[s[i-1]]);
            }
            map[s[i-1]] = i;
            res = max(res, dp[i]);
        }

        return res;
    }
};
