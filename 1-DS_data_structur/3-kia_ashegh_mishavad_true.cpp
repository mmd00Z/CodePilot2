#include <bits/stdc++.h>
using namespace std;
 
typedef long long int ll;
const int maxn = 1e5 + 7;

int n , a[maxn] ;
stack<int> st ;
map<int , int> cnt ;

void solve() {
    cin >> n ;
    for(int i = 1 ; i <= n ; i++)
        cin >> a[i] ;
    cnt[a[1]]++ ;
    st.push(1) ;
    int ans = 1 ;
    for (int i = 2 ; i <= n ; i++) {
        while(!st.empty() && a[st.top()] > a[i]) {
            cnt[a[st.top()]] = 0 ;
            st.pop() ;
        }
        cnt[a[i]]++ ;
        if (!st.empty() && a[i] == a[st.top()])
			ans = max(ans , cnt[a[i]]) ;
		else
			st.push(i) ;
    }
    cout << ans << endl;
}

int main() {
    solve();
}