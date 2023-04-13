/*
6588 골드바흐의 추측 

에라토스테네스의 체에서 실수가 있었다.
최종 곱한 결과가 100만이 되기만 하면 된다고 생각했는데
i = 1000, j = 2 일 때 둘은 곱한 결과는 2000 밖에 안 된다.
매 수마다 곱한 결과가 100만이 될 때까지 돌아야한다! 

반례
999370
0
혹은
1000000
0
https://www.acmicpc.net/board/view/87525 
*/

// 맞은 코드
#include <stdio.h>

int prime[1000001];
int main(void)
{
    int n;
    for (int i = 2; i < 500001; ++i) {
        for (int j = 2; i*j < 1000001; ++j) {
            prime[i*j] = 1;
        }
    }
    prime[0] = prime[1] = 1;
    
    while (1) {
        scanf("%d", &n);
        if (n == 0) break;
        for (int i = 2; i <= n/2+1; ++i) {
            if (prime[i] == 0 && prime[n-i] == 0) {
                printf("%d = %d + %d\n", n, i, n-i);
                break;
            }
        }
    }

    return 0;
}

// 틀린 코드 
#if 0
#include <stdio.h>

int prime[1000001];
int main(void)
{
    int n;
    for (int i = 2; i < 1001; ++i) {
        for (int j = 2; j < 1001; ++j) {
            prime[i*j] = 1;
        }
    }
    prime[0] = prime[1] = 1;
    
    while (1) {
        scanf("%d", &n);
        if (n == 0) break;
        // 값이 반드시 존재하므로 1개 넘어가도 넘어가는 경우는 없음
		// 5 / 2 = 2 이므로 중간 지점인 3까지 포함하려면 +1이 필요했다. 
		// 제대로 하려면 n/2 + n%2 가 맞을 것 
        for (int i = 2; i <= n/2+1; ++i) {
            if (prime[i] == 0 && prime[n-i] == 0) {
                printf("%d = %d + %d\n", n, i, n-i);
                break;
            }
        }
    }

    return 0;
}
#endif
