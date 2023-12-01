class Solution {
public:
    int rectCover(int number) {
        if (number <= 2)    return number;
        int dp_1 = 1;
        int dp_2 = 2;
        int res = 0;
        for (int i=3;i<=number;i++){
            res = dp_1 + dp_2;
            dp_1 = dp_2;
            dp_2 = res;
        }
        return res;
    }
};
