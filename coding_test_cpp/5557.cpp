#include <iostream>

using namespace std;

long long dp[100][21];

int main(){
    int N;
    cin >> N;
    for(int i = 0; i < N-1; i++){
        int tmp;
        cin >> tmp;
        if(i==0){
            dp[i][tmp] = 1;
            continue;
        }
        for(int j=0; j<21; j++){
            int ttmp = j + tmp;
            if(ttmp <= 20){
                dp[i][ttmp] += dp[i-1][j];
            }
            ttmp = j - tmp;
            if(ttmp >= 0){
                dp[i][ttmp] += dp[i-1][j];
            }
        }
    }
    int ans;
    cin >> ans;
    cout << dp[N-2][ans];
    return 0;
}