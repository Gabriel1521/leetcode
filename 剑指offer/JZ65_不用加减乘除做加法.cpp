class Solution {
public:
    int Add(int num1, int num2) {
        int add = num2;
        int sum = num1;
        while (add != 0){
            int tmp = sum ^ add;
            add = (sum & add) << 1;
            sum = tmp;
        }
        return sum;
    }
};
