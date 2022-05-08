/*
백준 13460 구슬 탈출 2
브루트포스 비트마스크
*/
#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

char board[10][10] = {{0,},};
int n, m;
int dir[4][2] = {{0,1}, {1,0}, {0,-1}, {-1,0}};

void move_marble(int* pos, int dir_i){
    while(true){
        int new_pos_i = pos[0] + dir[dir_i][0];
        int new_pos_j = pos[1] + dir[dir_i][1];
        if(board[new_pos_i][new_pos_j] == 'O'){
            pos[0] = -1;
            pos[1] = -1;
            break;
        }else if(board[new_pos_i][new_pos_j] != '.'){
            board[pos[0]][pos[1]] = '1';
            break;
        }else{
            pos[0] = new_pos_i;
            pos[1] = new_pos_j;
        }
    }
}

void move(int dir_i, vector<int>& marble_pos){
    int r_pos[2] = {marble_pos[0], marble_pos[1]};
    int b_pos[2] = {marble_pos[2], marble_pos[3]};

    int r_val = r_pos[0]*dir[dir_i][0] + r_pos[1]*dir[dir_i][1];
    int b_val = b_pos[0]*dir[dir_i][0] + b_pos[1]*dir[dir_i][1];

    if(r_val > b_val){
        move_marble(r_pos, dir_i);
        move_marble(b_pos, dir_i);
    }else{
        move_marble(b_pos, dir_i);
        move_marble(r_pos, dir_i);
    }

    if(r_pos[0] != -1)
        board[r_pos[0]][r_pos[1]] = '.';
    if(b_pos[0] != -1)
        board[b_pos[0]][b_pos[1]] = '.';
    marble_pos[0] = r_pos[0];
    marble_pos[1] = r_pos[1];
    marble_pos[2] = b_pos[0];
    marble_pos[3] = b_pos[1];
}

int main(){
    cin >> n >> m;
    vector<int> marble_pos(4);
    int ans = -1;
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++){
            cin >> board[i][j];
            if(board[i][j] == 'R'){
                marble_pos[0] = i;
                marble_pos[1] = j;
                board[i][j] = '.';
            }
            else if(board[i][j] == 'B'){
                marble_pos[2] = i;
                marble_pos[3] = j;
                board[i][j] = '.';
            }
        }

    set<vector<int>> backtrack;

    queue<vector<int>> move_q;
    for(int i=0; i<4; i++){
        vector<int> temp_element = {1, i, marble_pos[0], marble_pos[1], marble_pos[2], marble_pos[3]};
                                                                //depth, dir, elements...
        move_q.push(temp_element);
    }
    // 초기 root 노드들을 큐에 삽입
    while(move_q.size()){
        vector<int> temp_pos = {move_q.front()[2], move_q.front()[3], move_q.front()[4], move_q.front()[5]};
        int num_move = move_q.front()[0];
        int dir_i = move_q.front()[1];
        if(num_move > 10){
            break;
        }
        move_q.pop();
            // 현재 front 정보를 지역변수에 저장하고 pop()

        move(dir_i, temp_pos);
            // 현재 depth에서 작업 수행

        if(temp_pos[0] == -1 &&
           temp_pos[1] == -1 &&
           temp_pos[2] == -1 &&
           temp_pos[3] == -1){
            continue;
        }
        
        if(temp_pos[0] == -1 &&
           temp_pos[1] == -1){
            ans = num_move;
            break;
        }
            // 조건에 맞으면 break로 while문 탈출

        if(backtrack.find(temp_pos) != backtrack.end()){
            continue;
        }
        backtrack.insert(temp_pos);

        for(int i=0; i<4; i++){
            vector<int> temp_element = {num_move+1, i, temp_pos[0], temp_pos[1], temp_pos[2], temp_pos[3]};
            move_q.push(temp_element);
        }
            // 현재 노드가 완성 조건도 아니고 드랍할 노드도 아니라면,
            // 현재 노드의 자식 노드들을 큐에 삽입.
    }
    cout << ans;

    return 0;
}