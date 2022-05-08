/*
백준 14888번 연산자 끼워넣기 (2)
브루트포스 재귀
*/
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int add(int a, int b){
    return a + b;
}

int sub(int a, int b){
    return a - b;
}

int mul(int a, int b){
    return a * b;
}

int divi(int a, int b){
    return a / b;
}

int (*fp[4])(int, int) = {add, sub, mul, divi};
int min_ans = 1000000000;
int max_ans = -1000000000;
int n;
set<vector<int>> backtrack;
vector<int> ops;
vector<int> nums;

void permutation(int depth){
    if(depth == n-1){
        int a = nums[0];
        for(int i=0; i < n-1 ; i++){
            a = fp[ops[i]](a, nums[i+1]);
        }
        if(min_ans > a){
            min_ans = a;
        }
        if(max_ans < a){
            max_ans = a;
        }
    }else{
        for(int i=depth; i<ops.size(); i++){
            swap(depth, i);
            vector<int> temp_vector = vector<int>(ops.begin(), ops.begin()+depth+1);
            if (backtrack.find(temp_vector) == backtrack.end()){
                backtrack.insert(temp_vector);
                permutation(depth+1);
            }
            swap(depth, i);
        }
    }
}

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        int temp_num;
        cin >> temp_num;
        nums.push_back(temp_num);
    }

    for(int i = 0; i < 4; i++){
        int temp_op;
        cin >> temp_op;
        if(temp_op > 10) temp_op = 10;
        for(int j = 0; j < temp_op; j++)
            ops.push_back(i);
    }
    permutation(0);
    cout << max_ans << endl << min_ans;

    return 0;
}