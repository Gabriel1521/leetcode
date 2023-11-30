#include <string>

using namespace std;

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param n int整型
     * @return int整型
     */
    int findNthDigit(int n) {
        // write code here
        int digit = 1;
        long long start = 1;
        long long sum = 9;
        while (n>sum){
            n -= sum;
            start *= 10;
            digit++;
            sum = 9 * start * digit;
        }
        int num = start + (n-1) / digit;
        int idx = (n-1) % digit;
        int result = to_string(num)[idx] - '0';
        return result;
    }
};
