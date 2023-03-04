/*
1526 가장 큰 금민수

brute force
그리디스러운 풀이를 떠올리다가
수의 범위가 크지 않아서
가장 쉬운 풀이는 brute force 라는 것을 깨달음 
*/

#include <stdio.h>

int main(void)
{
    int N, temp, flag;
    scanf("%d", &N);
    for (int i = N; i > 0; --i) {
        temp = i, flag = 1;
        while (temp) {
            if (temp % 10 != 4 && temp % 10 != 7) {
                flag = 0;
                break;
            }
            temp /= 10;
        }
        if (flag) {
            printf("%d\n", i);
            break;
        }
    }

    return 0;
}
