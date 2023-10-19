// 207_Course Schedule

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {

        if (prerequisites.size()==0){
            return true;
        }

        // build graph
        int n = numCourses;
        // list of int list
        vector<int> edges[n];
        // list of int
        int ind[n];
        for (int j =0;j<n;j++){
            ind[j] = 0;
        }

        for (int i=0;i<prerequisites.size();i++){
            int a = prerequisites[i][0];
            int b = prerequisites[i][1];
            if (a==b){
                return false;
            }
            // add element to list
            edges[a].push_back(b);
            ind[b] += 1;
            std::cout << "i " << b << " ind is " << ind[b] << "\n";
        }

        vector<int> ans = topological_sort(edges, ind, n);
        std::cout << "ans " ;
        for (int i=0;i<ans.size();i++){
            std::cout<< ans[i] << " ";
        }
        std::cout << "\n" ;

        if (ans.size() == n){
            return true;
        }
        return false;
    }

    vector<int> topological_sort(vector<int> *edges, int *ind, int n){
        vector<int> ans;
        queue<int> q;

        for (int i=0; i<n; i++){
            if (ind[i] == 0){
                q.push(i);

            }
        }
        while (!q.empty()){
            int x = q.front();
            q.pop();
            ans.push_back(x);
            int tmp_n = edges[x].size();
            for (int j=0;j<tmp_n;j++){
                int y = edges[x][j];
                ind[y] -= 1;
                if (ind[y] == 0){
                    q.push(y);
                }
            }
        }

        return ans;
    }
};
