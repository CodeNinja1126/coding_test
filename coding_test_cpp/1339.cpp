/*
백준 1339번 단어 수학
브루트포스 재귀
*/
#include <iostream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

int64_t weights[30] = {0,};
vector<string> str_vec;
int n;
int64_t max_ans = 0;

void cal_alphabet_weight(){
    for(auto str: str_vec){
        for(int i=0; i<str.size(); i++){
            int temp_i = str[i]-'A';
            weights[temp_i] += int64_t(pow(10, (str.size()-i-1)));
        }
    }
}

int main(){
    cin >> n;
    for(int i=0; i<n; i++){
        string temp_str;
        cin >> temp_str;
        str_vec.push_back(temp_str);
    }
    cal_alphabet_weight();
    for(int i=9; i>=0; i--){
        int64_t temp_max_val = 0;
        int temp_max_i = 0;
        for(int j=0; j<30; j++){
            if(i*weights[j] > temp_max_val){
                temp_max_val = i*weights[j];
                temp_max_i = j;
            }
        }
        max_ans += temp_max_val;
        weights[temp_max_i] = 0;
    }
    cout << max_ans;
    return 0;
}