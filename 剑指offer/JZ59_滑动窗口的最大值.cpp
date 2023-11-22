#include <deque>
#include <iostream>

using namespace std;

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param num int整型vector
     * @param size int整型
     * @return int整型vector
     */


    vector<int> maxInWindows(vector<int>& num, int size) {
        // write code here
        deque<int> dq={};
        vector<int> res={};
        int n = num.size();
        int k = size;
        if (n*k == 0 || n<k)   return {};

        for (int i=0;i<size;i++){
            while (!dq.empty() && num[i] > num[dq.back()]){
                    dq.pop_back();
                }

            dq.push_back(i);
        }

        res.push_back(num[dq[0]]);

        for (int j=k;j<n;j++){
            if (dq[0]+k <= j){
                dq.pop_front();
            }
            while (!dq.empty() && num[j] >= num[dq.back()]){
                dq.pop_back();
            }
            dq.push_back(j);
            res.push_back(num[dq[0]]);
        }

        return res;
    }
};
