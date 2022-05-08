/*
백준 12100번 2048 (Easy)
브루트포스 비트마스크
*/
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> board;
int ans = 0;

void move(int dir){
    vector<vector<int>> temp_board;
    if(dir == 0 || dir == 1){
        for(auto row : board){
            vector<int> temp_row;
            for(auto num : row){
                if(num != 0){
                    temp_row.push_back(num);
                }
            }
            vector<int> temp_row_;
            if(dir == 0){
                for(int i=0; i<temp_row.size(); i++){
                    if(i == temp_row.size()-1){
                        temp_row_.push_back(temp_row[i]);
                    }
                    else if(temp_row[i] == temp_row[i+1]){
                        temp_row_.push_back(temp_row[i]*2);
                        i++;
                    }else{
                        temp_row_.push_back(temp_row[i]);
                    }
                }
                for(int i=temp_row_.size(); i<row.size(); i++)
                    temp_row_.push_back(0);
            }
            else{
                for(int i=temp_row.size()-1; i>=0; i--){
                    if(i == 0){
                        temp_row_.insert(temp_row_.begin(),temp_row[i]);
                    }
                    else if(temp_row[i] == temp_row[i-1]){
                        temp_row_.insert(temp_row_.begin(),temp_row[i]*2);
                        i--;
                    }else{
                        temp_row_.insert(temp_row_.begin(),temp_row[i]);
                    }
                }
                for(int i=temp_row_.size(); i<row.size(); i++)
                    temp_row_.insert(temp_row_.begin(), 0);
            }
            temp_board.push_back(temp_row_);
        }
    }
    else{
        for(int i=0; i<board.size(); i++){
            vector<int> temp_row(board.size());
            temp_board.push_back(temp_row);
        }
        for(int i=0; i<board.size(); i++){
            vector<int> temp_col;
            for(int j=0; j<board.size(); j++){
                if(board[j][i] != 0){
                    temp_col.push_back(board[j][i]);
                }
            }
            vector<int> temp_col_;
            if(dir == 2){
                for(int j=0; j<temp_col.size(); j++){
                    if(j == temp_col.size()-1){
                        temp_col_.push_back(temp_col[j]);
                    }
                    else if(temp_col[j] == temp_col[j+1]){
                        temp_col_.push_back(temp_col[j]*2);
                        j++;
                    }else{
                        temp_col_.push_back(temp_col[j]);
                    }
                }
                for(int j=temp_col_.size(); j<board.size(); j++)
                    temp_col_.push_back(0);
            }
            else{
                for(int j=temp_col.size()-1; j>=0; j--){
                    if(j == 0){
                        temp_col_.insert(temp_col_.begin(),temp_col[j]);
                    }
                    else if(temp_col[j] == temp_col[j-1]){
                        temp_col_.insert(temp_col_.begin(),temp_col[j]*2);
                        j--;
                    }else{
                        temp_col_.insert(temp_col_.begin(),temp_col[j]);
                    }
                }
                for(int j=temp_col_.size(); j<board.size(); j++)
                    temp_col_.insert(temp_col_.begin(), 0);
            }
            for(int j=0; j<board.size(); j++){
                temp_board[j][i] = temp_col_[j];
            }
        }
    }
    board = temp_board;
}

int find(){
    int max_num = 0;
    for(auto row : board)
        for(auto num : row)
            if(num > max_num) max_num = num;
    return max_num;
}

void permutation(int depth){
    if(depth==5){
        int temp_num = find();
        if(temp_num > ans) ans = temp_num;
    }else{
        for(int i=0; i<4; i++){
            vector<vector<int>> temp_board = board;
            move(i);
            permutation(depth+1);
            board = temp_board;
        }
    }
}

int main(){
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        vector<int> temp_vector(n);
        for(int j=0; j<n; j++){
            cin >> temp_vector[j];
        }
        board.push_back(temp_vector);
    }
    permutation(0);
    cout << ans;
    return 0;
}