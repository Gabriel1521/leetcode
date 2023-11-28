#include <algorithm>
#include <vector>
#include <stack>
#include <deque>

using namespace std;

class Solution {
public:
    deque<int> dq;
    void push(int value) {
        dq.push_back(value);
    }
    void pop() {
        dq.pop_back();
    }
    int top() {
        int element = dq.back();
        return element;
    }
    int min() {
        int min_num = *std::min_element(dq.begin(),dq.end());
        return min_num;
    }
};
