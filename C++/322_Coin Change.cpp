#include <limits>

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int inf = std::numeric_limits<int>::max()-1;
        vector<int> dp(amount+1, inf);
        dp[0] = 0;


        for (int x=1;x<amount+1;x++){
            for (int coin: coins){
                if (x >= coin){
                    dp[x] = min(dp[x], dp[x-coin]+1);
                    //cout << "x coin dp[x] "<<x<<" "<<coin<<" "<<dp[x]<<"\n";
                }
            }
        }

        if (dp[amount] != inf)
            return dp[amount];
        else
            return -1;
    }
};
