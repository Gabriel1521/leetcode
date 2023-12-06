class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param numbers int整型vector
     * @return int整型
     */
    int duplicate(vector<int>& numbers) {
        // write code here
        if (numbers.size()<=1)  return -1;
        sort(numbers.begin(),numbers.end());
        for (int i=1;i<numbers.size();i++){
            if (numbers[i] == numbers[i-1])
                return numbers[i];
        }
        return -1;
    }
};
