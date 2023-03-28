/*
3460 이진수 

수학, 구현 
TC 여러개 주어지는 문제는
예제에 1개만 있더라도 반드시 2개 이상 넣어볼 것!
본 문제에서도 \n 빠뜨렸었다. 
*/

#include <stdio.h>

int main(void)
{
    int T, n, bit;
    scanf("%d", &T);
    while (T--) {
        bit = 0;
        scanf("%d", &n);
        while (n) {
            if (n & 1) printf("%d ", bit);
            n >>= 1;
            bit++;
        }
        printf("\n");
    }

    return 0;
}
