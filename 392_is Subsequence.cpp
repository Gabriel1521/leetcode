/*392.is Subsequence*/

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int l1 = t.length();
        int l2 = s.length();
        int i = 0;
        int j = 0;
        while (i<l1){
            if (t[i] == s[j]){
                i += 1;
                j += 1;
            }
            else{
                i += 1;
            }

        }
        return j==l2;
    }
};
