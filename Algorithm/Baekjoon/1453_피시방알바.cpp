/*
1453 피시방 알바

구현 
사람들이 이미 앉아서 나중에 요청한 사람이 거절당한 횟수 세기 
*/

#include <stdio.h>
int computer[101];

int main(void)
{
    int N; int count = 0; int seat;
    scanf("%d", &N);
    while (N--) {
        scanf("%d", &seat);
        if (computer[seat]) count++;
        else computer[seat] = 1;
    }
    printf("%d\n", count);

    return 0;
}
