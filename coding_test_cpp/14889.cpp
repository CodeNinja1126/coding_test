/*
백준 1339번 스타트와 링크
브루트포스 순열
*/
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int n;
int stat[20][20];
vector<int> combi;
int ans = 100000;

int cal_team_stat(vector<int> arr){
    int ans = 0;
    for(int i=0; i<arr.size()-1; i++)
        for(int j=i+1; j<arr.size(); j++)
            ans += stat[arr[i]][arr[j]] + stat[arr[j]][arr[i]];
    return ans;
}

void procedure(){
    vector<int> temp_combi;
    for(int i=0; i<n; i++){
        int flg = 1;
        for(auto temp_num : combi){
            if(i==temp_num){
                flg = 0;
                break;
            }
        }
        if(flg){
            temp_combi.push_back(i);
        }
    }
    int team_a = cal_team_stat(combi);
    int team_b = cal_team_stat(temp_combi);
    if(ans > abs(team_a - team_b)){
        ans = abs(team_a - team_b);
    }
}

void combination(int index){
    if(combi.size()==n/2){ // 구할 조합의 길이
		procedure();
    }else{
        for(int i=index; i<n - (n/2-int(combi.size())) + 1; i++){
            combi.push_back(i);
            combination(i+1);
            combi.pop_back();
        }
    }
}

int main(){
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> stat[i][j];
        }
    }
    combination(0);
    cout << ans;
    return 0;
}