class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        deque<deque<int>> matrix_cp;
        int m = matrix.size();
        int n = matrix[0].size();
        for (int i=0; i<m;i++){
            matrix_cp.push_back({});
            for (int j=0;j<n;j++){
                matrix_cp[i].push_back(matrix[i][j]);
            }
        }

        while (matrix_cp.empty() == false && matrix_cp[0].empty() == false){
            if (matrix_cp.empty() == false && matrix_cp[0].empty() == false){
                deque<int> first_row = matrix_cp.front();
                matrix_cp.pop_front();
                while (first_row.empty() == false){
                    res.push_back(first_row.front());
                    first_row.pop_front();
                }
            }

            if (matrix_cp.empty() == false && matrix_cp[0].empty() == false){
                for (auto& row: matrix_cp){
                    res.push_back(row.back());
                    row.pop_back();
                }
            }

            int last_row_idx = matrix_cp.size()-1;
            if (matrix_cp.empty() == false && matrix_cp[last_row_idx].empty() == false){
                deque<int> last_row = matrix_cp.back();
                matrix_cp.pop_back();
                while (last_row.empty() == false){
                    res.push_back(last_row.back());
                    last_row.pop_back();
                }
            }

            if (matrix_cp.empty() == false && matrix_cp[0].empty() == false){
                deque<int> tmp;
                for (auto& row : matrix_cp){
                    tmp.push_back(row.front());
                    row.pop_front();
                }
                for (auto& element: tmp){
                    res.push_back(tmp.back());
                    tmp.pop_back();
                }
            }

        }
        return res;
    }
};x
