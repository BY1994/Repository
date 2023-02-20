/*
23375 Arm Coordination

원을 포함하는 가장 작은 사각형을 그리는데,
정수 좌표만 지원하기 때문에
웬만하면 반지름 길이만큼 빼서 그린 사각형으로 답을 유도하는 것 같다. 

10^9 범위기 때문에 int 로 처리하였다. 
*/
#include <stdio.h>

int main(void)
{
    int x, y, r;
    scanf("%d %d", &x, &y);
    scanf("%d", &r);

    printf("%d %d\n", x-r, y-r);
    printf("%d %d\n", x-r, y+r);
    printf("%d %d\n", x+r, y+r);
    printf("%d %d\n", x+r, y-r);

    return 0;
}
