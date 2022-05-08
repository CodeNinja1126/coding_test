/*
백준 4574번 스도미노쿠
브루트포스 재귀
*/
#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int sdoku[9][9];
int check_square[9][10] = {{0,},};
int check_row[9][10] = {{0,},};
int check_col[9][10] = {{0,},};
vector<pair<int, int>> dominos;

void empty_board(){
    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            sdoku[i][j] = 0;
        }
    }
    for(int i=0; i<9; i++){
        for(int j=0; j<10; j++){
            check_square[i][j] = 0;
            check_row[i][j] = 0;
            check_col[i][j] = 0;
        }
    }
}

void print_board(){
    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            cout << sdoku[i][j];
        }
        cout << endl;
    }
}

inline int cal_squ(int i, int j){
    return (i/3) * 3 + (j/3); 
}

inline void toggle(int num, int i, int j){
    check_square[cal_squ(i, j)][num] = !check_square[cal_squ(i, j)][num];
    check_row[i][num] = !check_row[i][num];
    check_col[j][num] = !check_col[j][num];
}

bool is_ok(int num_1, int i, int j){
    if(check_square[cal_squ(i, j)][num_1]){
        return false;
    }
    if(check_row[i][num_1]){
        return false;
    }
    if(check_col[j][num_1]){
        return false;
    }
    return true;
}

bool permutation(int);

bool inner_permu(int index, int dom_i, int num_1, int num_2, int i, int j, int k, int l){
    if( k < 9 && l < 9 &&
        !sdoku[k][l] &&
        is_ok(num_1, i, j) &&
        is_ok(num_2, k, l)){
        sdoku[i][j] = num_1;
        sdoku[k][l] = num_2;
        toggle(num_1, i, j);
        toggle(num_2, k, l);
        auto temp_domino = dominos[dom_i];
        dominos.erase(dominos.begin()+dom_i);
        if(permutation(index+1)){
            return true;
        }
        dominos.insert(dominos.begin()+dom_i, temp_domino);
        sdoku[i][j] = 0;
        sdoku[k][l] = 0;
        toggle(num_1, i, j);
        toggle(num_2, k, l);
    }
    return false;
}

bool permutation(int index){
    if(index==81){
        return true;
    }else{
        int pos_i = index/9;
        int pos_j = index%9;
        if(sdoku[pos_i][pos_j]){
            if(permutation(index+1)){
                return true;
            }
        }else{
            for(int i=0; i<dominos.size(); i++){
                if(inner_permu(index, i, dominos[i].first, dominos[i].second,
                                pos_i, pos_j, pos_i, pos_j+1)) return true;
                if(inner_permu(index, i, dominos[i].second, dominos[i].first,
                                pos_i, pos_j, pos_i, pos_j+1)) return true;
                if(inner_permu(index, i, dominos[i].first, dominos[i].second,
                                pos_i, pos_j, pos_i+1, pos_j)) return true;
                if(inner_permu(index, i, dominos[i].second, dominos[i].first,
                                pos_i, pos_j, pos_i+1, pos_j)) return true;
            }
        }
    }
    return false;
}

void sdominoku(int n){
    for(int i=1; i<9; i++){
        for(int j=i+1; j<10; j++){
            dominos.push_back(make_pair(i,j));
        }
    }

    for(int ii=0; ii<n; ii++){
        int i, j, num;
        string pos;
        pair<int,int> domino;

        cin >> num >> pos;
        i = pos[0]-'A';
        j = pos[1]-'1';
        sdoku[i][j] = num;
        toggle(num, i, j);
        domino.first = num;

        cin >> num >> pos;
        i = pos[0]-'A';
        j = pos[1]-'1';
        sdoku[i][j] = num;
        toggle(num, i, j);
        domino.second = num;

        if(domino.first > domino.second){
            swap(domino.first, domino.second);
        }
        
        for(int ij = 0; ij < dominos.size(); ij++){
            if(dominos[ij] == domino){
                dominos.erase(dominos.begin()+ij);
                break;
            }
        }
    }

    for(int i=0; i<9; i++){
        string pos;
        cin >> pos;
        sdoku[pos[0]-'A'][pos[1]-'1'] = i+1;
        toggle(i+1, pos[0]-'A', pos[1]-'1');
    }

    permutation(0);
    print_board();
    dominos.clear();
    empty_board();
}


int main(){
    int i = 1;
    while(true){
        int n;
        cin >> n;
        if(n == 0) break;
        cout << "Puzzle " << i << endl;
        sdominoku(n);
        i++;
    }
    return 0;
}
