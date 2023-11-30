class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param target int整型
     * @param array int整型vector<vector<>>
     * @return bool布尔型
     */
    bool binary_search(vector<int> nums, int target){
        int l = 0;
        int h = nums.size()-1;

        int m = 0;
        while (l<=h){
            m = (l+h)/2;
            if (nums[m] < target)
                l = m+1;
            else if (nums[m] > target)
                h = m-1;
            else
                return true;
        }
        return false;

    }

    bool Find(int target, vector<vector<int> >& array) {
        // write code here
        int n = array.size();
        for (int i=0;i<n;i++){
            if (binary_search(array[i],target))
                return true;
        }
        return false;
    }
};
// 时间复杂度：O(Mlog N )
// 空间复杂度：O(1)

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param target int整型
     * @param array int整型vector<vector<>>
     * @return bool布尔型
     */

    bool Find(int target, vector<vector<int> >& array) {
        // write code here
        int m = array.size();
        int n = array[0].size();

        int m_idx = 0;
        int n_idx = n-1;
        while (m_idx < m && n_idx >= 0){
            if (array[m_idx][n_idx] == target)  return true;
            else if (array[m_idx][n_idx] > target)
                n_idx--;
            else
                m_idx++;
        }
        return false;
    }
};

// 时间复杂度:O(M+N)
// 空间复杂度:O(1)

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param target int整型
     * @param array int整型vector<vector<>>
     * @return bool布尔型
     */
    bool binary_search_advanced(vector<vector<int>>& nums, int l_i, int h_i, int l_j, int h_j, int target){
        if (l_i == h_i || l_j == h_j)   return false;
        int m_i = (l_i + h_i)/2;
        int m_j = (l_j + h_j)/2;

        if (nums[m_i][m_j] == target)   return true;
        else if (nums[m_i][m_j] < target){
            if (binary_search_advanced(nums, m_i+1, h_i, l_j, h_j, target))   return true;
            if (binary_search_advanced(nums, l_i, m_i+1, m_j+1, h_j, target))   return true;
        }
        else{
            if (binary_search_advanced(nums, l_i, m_i-1, l_j, h_j, target)) return true;
            if (binary_search_advanced(nums, m_i, h_i, l_j, m_j-1, target)) return true;
        }
        return false;
    }

    bool Find(int target, vector<vector<int> >& array) {
        // write code here
        int m = array.size();
        int n = array[0].size();

        int m_idx = 0;
        int n_idx = n-1;
        while (m_idx < m && n_idx >= 0){
            if (array[m_idx][n_idx] == target)  return true;
            else if (array[m_idx][n_idx] > target)
                n_idx--;
            else
                m_idx++;
        }
        return false;
    }
};

// 时间复杂度:O(logM*logN)
// 空间复杂度:O(1)
