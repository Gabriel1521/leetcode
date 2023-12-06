class Solution {
public:
    void dfs(vector<int> nums, vector<int>& path, vector<vector<int>>& result){
        if (nums.empty()){
            result.push_back(path);
            return;
        }

        for (int i=0;i<nums.size();i++){
            path.push_back(nums[i]);
            nums.erase(nums.begin()+i);
            dfs(nums, path, result);
            nums.insert(nums.begin()+i,path.back());
            path.pop_back();
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result = {};
        vector<int> path = {};
        dfs(nums, path, result);
        return result;
    }
};


class Solution {
public:
    void dfs(vector<int> nums, vector<int>& path, vector<vector<int>>& result){
        if (path.size() == nums.size()){
            result.push_back(path);
            return;
        }

        for (int i=0;i<nums.size();i++){
            if (find(path.begin(),path.end(),nums[i])==path.end()){
                path.push_back(nums[i]);
                dfs(nums, path, result);
                path.pop_back();
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result = {};
        vector<int> path = {};
        dfs(nums, path, result);
        return result;
    }
};
