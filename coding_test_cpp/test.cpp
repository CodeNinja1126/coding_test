#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

int main() {
    int N, S, P, Q;
    cin >> N >> S >> P >> Q;
    set<int> res_set;
    int a = S % int(pow(2,31));
    res_set.insert(a);
    for(int i=1; i<N; i++){
        a = (a * P + Q) % int(pow(2,31));
        res_set.insert(a);
    }
    cout << res_set.size();
    return 0;
}