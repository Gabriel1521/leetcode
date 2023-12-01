class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param prices int整型vector
     * @return int整型
     */
    int maxProfit(vector<int>& prices) {
        // write code here
        int min_price = prices[0];
        int max_profit = 0;

        int n = prices.size();

        for (int i=1;i<n;i++){
            if (prices[i] < min_price){
                min_price = prices[i];
            }
            max_profit = max(max_profit, prices[i]-min_price);
        }
        return max_profit;
    }
};
