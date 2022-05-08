/*
백준 14225번 부분수열의 합
브루트포스 재귀
*/
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int n;
set<int> ans;
vector<int> nums;
vector<int> combi;

void combination(int index){
    if(combi.size()==n){
        int sum = 0;
        for(auto temp_num : combi){
            sum += temp_num;
        }
        ans.insert(sum);
    }else{
        for(int i=index; i<nums.size() - (n-int(combi.size())) + 1; i++){
            combi.push_back(nums[i]);
            combination(i+1);
            combi.pop_back();
        }
    }
}

int main(){
    cin >> n;
    for(int i=0; i<n; i++){
        int temp_num;
        cin >> temp_num;
        nums.push_back(temp_num);
    }
    for(int i=1; i<nums.size()+1; i++){
        n = i;
        combination(0);
    }
    for(unsigned long long i=1; i<=-1; i++){
        if(ans.find(i) == ans.end()){
            cout << i;
            break;
        }
    }
    return 0;
}