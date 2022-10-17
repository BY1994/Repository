/*
2547 사탕 선생 고창영

틀렸던 이유
1. unsigned long long 으로 선언하더라도
모든 학생들의 사탕을 다 받으면 범위를 벗어남
% N 을 매번 해주는 작업이 필요하다
https://www.acmicpc.net/board/view/1422

2. 초기화를 Test Case 마다 해주어야하는데, 딱 한 번만 해줬다.
문제 예제가 맞아서 엄청 틀린 후에 발견했다. 
초기화를 다시 생각해보게 해준 질문 게시글
https://www.acmicpc.net/board/view/80377 
*/
#include <stdio.h>

int main()
{
    int T;
    unsigned long long N;
    unsigned long long total;
    unsigned long long candy;
    scanf("%d", &T);
    while (T--) {
        getchar();
        scanf("%llu", &N);
        total = 0;
        for (unsigned long long i = 0; i < N; ++i) {
            scanf("%llu", &candy);
            total += candy;
            total %= N;
        }
        if (total % N) printf("NO\n");
        else printf("YES\n");
    }

    return 0;
}
