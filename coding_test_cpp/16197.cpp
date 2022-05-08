/*
백준 16197번 두 동전
브루트포스 재귀
*/
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>

using namespace std;

set<vector<int>> backtrack;
int dir[4][2] = {{0,1}, {1,0}, {-1,0}, {0,-1}};
char board[20][20] = {{0,},};
int n, m;
int ans = -1;

void move(int dir_i, vector<int>& coin_pos){
    for(int i=0; i<2; i++){
        int temp_i = coin_pos[i*2] + dir[dir_i][0];
        int temp_j = coin_pos[i*2+1] + dir[dir_i][1];
        if (temp_i >= 0 && temp_j >= 0 &&
            temp_i < n && temp_j < m){
            if(board[temp_i][temp_j] == '#'){
                temp_i = coin_pos[i*2];
                temp_j = coin_pos[i*2+1];
            }
        }else{
            temp_i = -1;
            temp_j = -1;
        }
        coin_pos[i*2] = temp_i;
        coin_pos[i*2+1] = temp_j;
    }
}

int main(){
    cin >> n >> m;
    int flag = 0;
    int coin_pos[4] = {0,0,0,0};
    for(int i=0; i<n; i++){
        string temp_str;
        cin >> temp_str;
        for(int j=0; j<m; j++){
            if(temp_str[j] == 'o'){
                coin_pos[flag] = i;
                coin_pos[flag+1] = j;
                board[i][j] = '.';
                flag += 2;
            }else{
                board[i][j] = temp_str[j];
            }
        }
    }
    queue<vector<int>> move_q;
    for(int i=0; i<4; i++){
        vector<int> temp_element = {1, i, coin_pos[0], coin_pos[1], coin_pos[2], coin_pos[3]};
        move_q.push(temp_element);
    }

    while(move_q.size()){
        vector<int> coin_pos = {move_q.front()[2], move_q.front()[3], move_q.front()[4], move_q.front()[5]};
        int num_move = move_q.front()[0];
        int dir_i = move_q.front()[1];
        move_q.pop();

        if(num_move>10){
            break;
        }

        move(dir_i, coin_pos);

        int minus_one_num = 0;
        for(int i=0; i<4; i++){
            if(coin_pos[i]==-1){
                minus_one_num++;
            }
        }
        if(minus_one_num==2){
            ans = num_move;
            break;
        }
        else if(minus_one_num==4){
            continue;
        }
        
        if(backtrack.find(coin_pos) != backtrack.end()){
            continue;
        }
        backtrack.insert(coin_pos);

        for(int i=0; i<4; i++){
            vector<int> temp_element = {num_move+1, i, coin_pos[0], coin_pos[1], coin_pos[2], coin_pos[3]};
            move_q.push(temp_element);
        }

    }

    cout << ans;
    return 0;
}