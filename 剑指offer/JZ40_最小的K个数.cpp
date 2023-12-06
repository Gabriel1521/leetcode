class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param input int整型vector
     * @param k int整型
     * @return int整型vector
     */
    vector<int> GetLeastNumbers_Solution(vector<int>& input, int k) {
        // write code here
        vector<int> res = {};
        priority_queue<int, vector<int>> pq;

        if (k == 0 || k > input.size()) return res;

        for (int val: input){
            if (pq.size()<k){
                pq.push(val);
            }else{
                if (val < pq.top()){
                    pq.pop();
                    pq.push(val);
                }
            }
        }

        while (!pq.empty()){
            res.push_back(pq.top());
            pq.pop();
        }

        sort(res.begin(),res.end());

        return res;
    }
};
