/*
백준 1062번 가르침
브루트포스 비트마스크
*/
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;
int n, k;
vector<unsigned int> words;
char chs[21] = {'b','d','e','f','g','h','j',
                'k','l','m','o','p','q','r',
                's','u','v','w','x','y','z'};
unsigned int bit_combi = 0;
int ans = 0;

void combination(unsigned int index, int depth){
    if(depth == k){
        int temp_num = 0;
		for(auto temp_word : words){
            if((bit_combi&temp_word)==temp_word){
                temp_num += 1;
            }
        }
        if(ans < temp_num) ans = temp_num;
    }else{
        for(int i=index; i<21 - (k-depth) + 1; i++){
            bit_combi += 1 << i;
            combination(i+1, depth+1);
            bit_combi -= 1 << i;
        }
    }
}

int main(){
    cin >> n >> k;
    if(k < 5){
        cout << 0;
        return 0;
    }

    k -= 5;

    for(int i=0; i<n; i++){
        string temp_word;
        cin >> temp_word;
        unsigned int temp_bit = 0;
        for(int i=0; i<21; i++){
            for(auto ch : temp_word){
                if(chs[i] == ch){
                    temp_bit += 1 << i;
                    break;
                }
            }
        }
        words.push_back(temp_bit);
    }
    
    combination(0, 0);
    
    cout << ans;

    return 0;
}