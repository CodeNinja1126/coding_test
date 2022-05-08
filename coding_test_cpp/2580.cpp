/*
백준 2580번 스도쿠
브루트포스 재귀
*/
#include <iostream>
#include <vector>

using namespace std;

int sdoku[9][9];
int check_square[9][10] = {{0,},};
int check_row[9][10] = {{0,},};
int check_col[9][10] = {{0,},};

inline int cal_squ(int i, int j){
    return (i/3) * 3 + (j/3); 
}

bool check_sdoku(){
    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            if(sdoku[i][j]){
                return false;
            }
        }
    }
    return true;
}

bool is_ok(int num, int i, int j){
    if(check_square[cal_squ(i, j)][num]){
        return false;
    }
    if(check_row[i][num]){
        return false;
    }
    if(check_col[j][num]){
        return false;
    }
    return true;
}

bool permutation(int index){
    if(index==81){
        return true;
    }else{
        if(sdoku[index/9][index%9]){
            if(permutation(index+1)){
                return true;
            }
        }else{
            for(int i=1; i<10; i++){
                if(is_ok(i, index/9, index%9)){
                    sdoku[index/9][index%9] = i;
                    check_square[cal_squ(index/9, index%9)][i] = 1;
                    check_row[index/9][i] = 1;
                    check_col[index%9][i] = 1;
                    if(permutation(index+1)){
                       return true;
                    }
                    sdoku[index/9][index%9] = 0;
                    check_square[cal_squ(index/9, index%9)][i] = 0;
                    check_row[index/9][i] = 0;
                    check_col[index%9][i] = 0;
                }
            }
        }
    }
    return false;
}

int main(){
    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            cin >> sdoku[i][j];
            check_row[i][sdoku[i][j]] = 1;
            check_col[j][sdoku[i][j]] = 1;
            check_square[cal_squ(i, j)][sdoku[i][j]] = 1;
        }
    }

    permutation(0);

    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            cout << sdoku[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}