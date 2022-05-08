/*
백준 16198번 에너지 모으기
브루트포스 재귀
*/
#include <iostream>
#include <vector>

using namespace std;

vector<int> marbles;
int ans = 0;
int n;

void permutation(int energy){
    if(marbles.size() == 2){
        if(energy > ans){
            ans = energy;
        }
    }else{
        for(int i=1; i<marbles.size()-1; i++){
            int temp_marble = marbles[i];
            marbles.erase(marbles.begin()+i);
            permutation(energy+(marbles[i-1]*marbles[i]));
            marbles.insert(marbles.begin()+i, temp_marble);
        }
    }
}

int main(){
    cin >> n;
    for(int i=0; i<n; i++){
        int temp_n;
        cin >> temp_n;
        marbles.push_back(temp_n);
    }
    permutation(0);
    cout << ans;
    return 0;
}