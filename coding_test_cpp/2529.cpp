/*
백준 2529번 부등호
브루트포스 재귀
*/
#include <iostream>
#include <cmath>

using namespace std;

int nums[10] = {0,1,2,3,4,5,6,7,8,9};
char inequ[10];
int64_t min_ans = 10000000000;
int64_t max_ans = 0;
int n;

bool check(){
    for(int i=0; i<n; i++){
        if(inequ[i] == '<'){
            if(nums[i] < nums[i+1]){
                continue;
            }else{
                return false;
            }
        }else{
            if(nums[i] > nums[i+1]){
                continue;
            }else{
                return false;
            }
        }
    }
    return true;
}

void permutation(int depth){
    if(depth == n+1){ // 순열의 길이
        if(check()){
            int64_t temp_ans = 0;
            for(int i=0; i<n+1; i++){
                temp_ans += nums[i] * int64_t(pow(10, (n-i)));
            }
            if(temp_ans > max_ans){
                max_ans = temp_ans;
            }
            if(temp_ans < min_ans){
                min_ans = temp_ans;
            }
        }
    }else{
        for(int i=depth; i<10; i++){
            swap(nums[depth], nums[i]);
            permutation(depth+1);
            swap(nums[depth], nums[i]);
        }
    }
}

int main(){
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> inequ[i];
    }
    permutation(0);
    for(int i=n; i>=0; i--){
        if(max_ans/int64_t(pow(10, i))){
            break;
        }
        cout << 0;
    }
    cout << max_ans << endl;
    for(int i=n; i>=0; i--){
        if(min_ans/int64_t(pow(10, i))){
            break;
        }
        cout << 0;
    }
    cout << min_ans << endl;
    return 0;
}