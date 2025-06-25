#include <iostream>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    int a[n];

    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for(int i = 0; i < q; i++) {
        int cmd, in1, in2;
        cin >> cmd >> in1 >> in2;
        in1--;
        
        if(cmd == 1) {
            a[in1] = in2;
        } 
        else if(cmd == 2) {
            int progress = 0, max_a = 0;
            
            for(int j=0; j<in2; j++) {
                if(j >= in1) {
                    progress += (a[j] - max_a > 0)? a[j] - max_a:0;
                }
                max_a = (max_a > a[j])? max_a:a[j];
            }
            cout << progress << endl;
        }
    }

    return 0;
}