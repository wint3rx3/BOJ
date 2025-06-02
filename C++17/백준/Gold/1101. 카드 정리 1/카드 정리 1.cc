#include <iostream>
#include <cstring>

using namespace std;

int main() {    
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N,M,i,j,arr[50][50],joker,ans=0,cnt;
    bool used[50] = {};

    cin >> N >> M;
    ans = N-1;
    for(i=0;i<N;i++) {
        for(j=0;j<M;j++) {
            cin >> arr[i][j];
        }
    }

    for(joker=0;joker<N;joker++) {
        memset(used,false,sizeof(used));
        cnt = 0;
        for(i=0;i<N;i++) {
            if(joker == i)
                continue;
            else {
                int flag = 0;  // check number of not 0
                for(j=0;j<M;j++) {
                    if(arr[i][j] != 0) {
                        flag++;
                    }
                }
                if(!flag) // all 0 -> dont have to move
                    continue;
                if(flag == 1) { // only one color
                    int color;
                    for(j=0;j<M;j++) // find which color
                        if(arr[i][j])
                            color = j;
                    if(used[color]) // already used color
                        cnt++;
                    else // first time
                        used[color] = true;
                } else if(flag>1) { // over two colors, have to move
                    cnt++;
                }
            }
        }
        ans = min(ans, cnt);
    }
    cout << ans << "\n";
    return 0;
}