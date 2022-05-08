/*
백준 9663번 N-Queen
브루트포스 재귀
*/
#include <iostream>

using namespace std;

int n = 0;
int ans = 0;
int board[15] = {0,};

bool check(int depth){
    for(int i=0; i<depth; i++){
        if(board[depth]==board[i] || (depth - i)==abs(board[depth]-board[i])){
            return false;
        }
    }
    return true;
}

void n_queen(int depth){
    if(depth == n){
        ans += 1;
    }else{
        for(int i=0; i<n; i++){
            board[depth] = i;
            if(check(depth)){
                n_queen(depth+1);
            }
        }
    }
}

int main(){
    cin >> n;
    n_queen(0);
    cout << ans;
}