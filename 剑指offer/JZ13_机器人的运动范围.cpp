#include <numeric>
class Solution {
public:
    int convert(int num){
        string s = to_string(num);
        int result = 0;
        for (int i=0;i<s.length();i++){
            result += s[i] - '0';
        }
        return result;
    }

    void dfs(int threshold, int rows, int cols, int x, int y, vector<vector<int>>& visited){
        if (x < 0 || x >= rows || y < 0 || y >= cols || visited[x][y] == 1)
            return;

        int num = convert(x) + convert(y);
        if (num > threshold)
            return;

        visited[x][y] = 1;

        dfs(threshold, rows, cols, x-1, y, visited);
        dfs(threshold, rows, cols, x+1, y, visited);
        dfs(threshold, rows, cols, x, y-1, visited);
        dfs(threshold, rows, cols, x, y+1, visited);
    }

    int movingCount(int threshold, int rows, int cols) {
        vector<vector<int>> visited(rows, vector<int>(cols, 0));

        dfs(threshold, rows, cols, 0, 0, visited);

        int result = 0;
        for (int i=0;i<rows;i++){
            result += accumulate(visited[i].begin(), visited[i].end(), 0);
        }

        return result;
    }
};
