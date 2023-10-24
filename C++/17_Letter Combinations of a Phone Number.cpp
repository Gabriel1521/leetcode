class Solution {
public:
    vector<string> letterCombinations(string digits) {
        map<char,string> d;
        d['2'] = "abc";
        d['3'] = "def";
        d['4'] = "ghi";
        d['5'] = "jkl";
        d['6'] = "mno";
        d['7'] = "pqrs";
        d['8'] = "tuv";
        d['9'] = "wxyz";

        vector<string> result = {};
        if (digits.size() > 0){
            dfs(digits, "", result, d);
        }
        return result;
    }

    void dfs(string digits, string path, vector<string>& result, map<char,string> d){
        if (digits.size() == 0){
            result.push_back(path);
            return ;
        }
        for (auto& decode: d[digits[0]]){
            int l = digits.size();
            string cur_digits = digits.substr(1,l);
            dfs(cur_digits, path + decode, result, d);
        }
    }

};
