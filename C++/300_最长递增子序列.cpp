class Solution {
public:
    int cmp(int a, int b){
        if (a>b)
            return a;
        else
            return b;
    }
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n,1);

        for (int i=0;i<n;i++){
            for (int j=0;j<i;j++){
                if (nums[i] > nums[j])
                    dp[i] = cmp(dp[i],dp[j]+1);
            }
        }

    int result = *std::max_element(dp.begin(),dp.end());
    return result;
    }
};
