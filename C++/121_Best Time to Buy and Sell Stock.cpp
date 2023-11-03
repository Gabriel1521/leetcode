class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxprofit = 0;
        int n = prices.size();
        for (int i=1;i<n;i++){
            for (int j=0;j<i;j++){
                if (prices[i] - prices[j] > maxprofit)
                    maxprofit = prices[i] - prices[j];
            }
        }
        return maxprofit;

    }
};


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxprofit = 0;
        int minprice = std::numeric_limits<int>::max();
        int n = prices.size();
        for (int i=0;i<n;i++){
            if (prices[i]<minprice)
                minprice = prices[i];
            if (prices[i]-minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;

    }
};
