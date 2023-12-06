class Solution {
  public:
    priority_queue<int, vector<int>> min_pq;
    priority_queue<int, vector<int>, greater<int>> max_pq;
    void Insert(int num) {
        min_pq.push(num);
        max_pq.push(min_pq.top());
        min_pq.pop();
        if (min_pq.size() < max_pq.size()){
            min_pq.push(max_pq.top());
            max_pq.pop();
        }
    }
    double GetMedian() {
        if (min_pq.size()>max_pq.size()){
            return (double)min_pq.top();
        }
        else{
            return (double)(min_pq.top()+max_pq.top())/2;
        }
    }
};
