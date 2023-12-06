class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param matrix char字符型vector<vector<>>
     * @param word string字符串
     * @return bool布尔型
     */
    bool checkpath(vector<vector<char>>& matrix, vector<vector<bool>> visited, string word, int x, int y, int m, int n, int word_len, int idx){

        if (x < 0 || y < 0 || x >= m || y >= n || visited[x][y] == true || matrix[x][y] != word[idx])
            return false;
        if (idx == word_len)
            return true;

        visited[x][y] = true;


        if (checkpath(matrix, visited, word, x-1, y, m, n, word_len, idx+1) || checkpath(matrix, visited, word, x+1, y, m, n, word_len, idx+1) || checkpath(matrix, visited, word, x, y-1, m, n, word_len, idx+1) || checkpath(matrix, visited, word, x, y+1, m, n, word_len, idx+1))
            return true;
        else
            return false;
    }

    bool hasPath(vector<vector<char> >& matrix, string word) {
        // write code here
        int m = matrix.size();
        int n = matrix[0].size();

        int word_len = word.length()-1;

        vector<vector<bool>> visited(m,vector<bool>(n, false));

        for (int i=0;i<m;i++){
            for (int j=0;j<n;j++){
                if (checkpath(matrix, visited, word, i, j, m, n, word_len, 0))
                    return true;
            }
        }
        return false;
    }
};
