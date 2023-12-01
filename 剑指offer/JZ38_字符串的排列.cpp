#include <vector>

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param str string字符串
     * @return string字符串vector
     */
    vector<string> Permutation(string str) {
        // write code here
        if (str.empty()) return {};
        vector<string> result = {};
        dfs(str,"",result);
        return result;
    }

    void dfs(string s, string path, vector<string>& result){
        if (s.empty()){
            vector<string>::iterator it;
            it = find(result.begin(),result.end(),path);
            if (it == result.end()){
                result.push_back(path);
            }
        }
        int n = s.length();
        for (int i=0;i<n;i++){
            string slice_a = s.substr(0,i);
            string slice_b = s.substr(i+1,n);
            dfs(slice_a+slice_b, path + s[i], result);
        }
    }

};

#include <vector>

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param str string字符串
     * @return string字符串vector
     */
    unordered_set<string> st;    // 用于字符串去重
    vector<bool> vis;        // 标记当前访问的字符
    string path;            // 记录当前情况

    vector<string> Permutation(string str) {
        vector<string> ans;
        vis.resize(str.size(), false);    // 初始化为false
        dfs(str);    // 回溯入口
        for(auto & s : st) ans.push_back(s);    // 将结果加入ans数组
        sort(ans.begin(), ans.end());    // 按字典序排序
        return ans;
    }

    void dfs(string& str){
        if(path.size() == str.size()){    // 得到一种排列
            st.insert(path);
            return;
        }

        for(int i = 0; i < str.size(); i++){
            if(vis[i]) continue;    // 若当前字符已经使用过, 跳过
            vis[i] = true;    // 标记为使用
            path.push_back(str[i]);    // 加入结果
            dfs(str);    // 继续递归
            path.pop_back();    // 状态回溯
            vis[i] = false;
        }
    }

};
