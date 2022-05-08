/*
백준 6603번 로또
브루트포스 재귀
*/
#include <iostream>
#include <vector>

using namespace std;

vector<int> nums;

void combination(vector<int>& combi, int depth){
    if(depth == 6){
        for(int i = 0; i < 6; i++){
            cout << nums[combi[i]] <<  ' ';    
        }
        cout << endl;
        return;
    }else{
        if (combi.size() == 0)
            for (int i = 0; i < nums.size()+depth-6+1; i++){
                combi.push_back(i);
                combination(combi, depth+1);
                combi.pop_back();
            }
        else{
            for (int i = combi.back()+1; i < nums.size()+depth-6+1; i++){
                combi.push_back(i);
                combination(combi, depth+1);
                combi.pop_back();
            }
        }
    }
}

int main(){
    
    while(true){
        int n_num;
        vector<int> temp_nums;
        cin >> n_num;
        if(n_num==0) break;
        for(int i = 0; i < n_num; i++){
            int temp_num;
            cin >> temp_num;
            temp_nums.push_back(temp_num);
        }
        nums = temp_nums;
        vector<int> combi;
        combination(combi, 0);
        cout << endl;
    }
    
    return 0;
}