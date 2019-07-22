#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        int i = 0;
        int max_c = 0;
        vector<int>::iterator iter;
        while (nums.size()>0){
            int n = nums[nums.size()-1];
            nums.pop_back();
            int l1 = 0;
            int l2 = 0;
            int k = n + 1;
            iter = find(nums.begin(), nums.end(), k);
            while (iter != nums.end()){
                nums.erase(iter);
                l1 += 1;
                k += 1;
                iter = find(nums.begin(), nums.end(), k);
            }
            k = n-1;
            iter = find(nums.begin(), nums.end(), k);
            while (iter != nums.end()){
                nums.erase(iter);
                l2 += 1;
                k -= 1;
                iter = find(nums.begin(), nums.end(), k);
            }
            if (l1+l2+1>max_c){
                max_c = l1+l2+1;
            }

        }


        return max_c;
    }
};
