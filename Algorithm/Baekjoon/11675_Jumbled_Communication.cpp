/*
11675 Jumbled Communication

비트마스킹

원래의 수를 a 라고 했을 때 (a) XOR (a << 1) 한 수가 주어질 때,
원래의 수 찾기

<< 1 하면 마지막 bit 가 0이므로, 이 값을 이용해 거꾸로 찾아갈 수도 있지만
(마지막 값이 0 이라면 두 개가 같다는 뜻이므로, <<1 한 값의 마지막 값이 0일 때
a 의 마지막 값도 0이라는 의미. 이걸 이용하면 <<1 한 값의 마지막 값 앞의 값이
0이되므로 다시 같은 원리로 하나씩 찾아갈 수 있음) 
최대 수가 255 이므로 미리 룩업 테이블을 만들어도 된다. 
시간 제한은 5초 
*/

#include <stdio.h>
int TBL[260];
void init(void) {
    for (int i = 0; i < 256; ++i) {
        TBL[(i^(i<<1))&255] = i;
    }
}

int main(void)
{
    int n,b;
    init();
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &b);
        printf("%d ", TBL[b]);
    }
    return 0;
}
