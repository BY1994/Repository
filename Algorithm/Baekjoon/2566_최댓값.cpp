/*
2566 최댓값 

구현 

질문 게시판에 있는 거의 대부분의 반례가
다 0으로 가득찬 경우였다.
초기화 처리가 제대로 안 되어있으면 해당 반례에 걸리게 된다.
해당 문제인데 답변이 안 달린 질문이 있어 답변을 추가하였다. 
https://www.acmicpc.net/board/view/102878 
*/

#include <stdio.h>

int main(void)
{
    int x = 1; int y = 1;
    int max = -1;
    int num;

    for (int i = 1; i < 10; ++i) {
        for (int j = 1; j < 10; ++j) {
            scanf("%d", &num);
            if (num > max) {
                max = num;
                x = i, y = j;
            }
        }
    }
    printf("%d\n%d %d\n", max, x, y);

    return 0;
}

