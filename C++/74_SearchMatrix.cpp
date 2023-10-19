class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int left =0, right = m*n-1;
        v1(matrix[0]);

        while (left <= right){
            int mid = left + (right - left) / 2;
            int mid_val = matrix[mid/n][mid%n];

            if (mid_val == target)
                return true;
            else if (mid_val < target)
                left = mid+1;
            else
                right = mid-1;
        }

        return false;
    }

    void v1(vector<int>& nums){
        cout << "nums 0 is " << nums[0] << "\n";
    }
};
