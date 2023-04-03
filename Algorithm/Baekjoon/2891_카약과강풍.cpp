/*
2891 카약과 강풍

그리디
카약이 손상된 팀을 기준으로 할지,
카약을 여분을 챙겨온 팀을 기준으로 할지 고민했는데,
손상된 팀 기준으로 짠 코드가 생각보다 잘 짜졌다.

문제에서 주의해야할 점은 여분을 챙겨온 팀 카약도 손상될 수 있다는 점이다.
또한 아래 구현할 때 왼쪽 인덱스를 0부터 시작해서 여분이 1개 있고,
오른쪽 인덱스도 11까지 접근 가능해서 여분이 1이 있기 때문에
-1 과 +1 을 이용한 순회가 편리했다.

좌우에 여분이 있는 팀이 2개가 아니라 1개인 팀부터 나눠주는 방법도 있다. 
*/

#include <stdio.h>
int N, S, R, team, ans;
int broken[12];
int kayak[12];

int main(void)
{
    scanf("%d %d %d", &N, &S, &R);
    ans = S;
    for (int i = 0; i < S; ++i) {
        scanf("%d", &broken[i]);
        kayak[broken[i]] -= 1;
    }
    for (int i = 0; i < R; ++i) {
        scanf("%d", &team);
        kayak[team] += 1;
    }
    for (int i = 0; i < S; ++i) {
        if (kayak[broken[i]] >= 0) ans--; // 여분이 손상된 팀 (문제 없음) 
        else {
            if (kayak[broken[i]-1] > 0) {
                kayak[broken[i]-1] -= 1; // 왼쪽 팀이 빌려줌 
                ans--;
            }
            else if (kayak[broken[i]+1] > 0) {
                kayak[broken[i]+1] -= 1; // 오른쪽 팀이 빌려줌 
                ans--;
            }
        }
    }
    printf("%d\n", ans);
    return 0;
}
