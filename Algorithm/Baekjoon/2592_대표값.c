/*
2592 대표값

10개 수 평균과 최빈값 구하기
*/

#include <stdio.h>

int count[1001];
int _sum;
int _max;
int _ind;

int main(void)
{
    int num;
    
    for (int i = 0; i < 10; ++i) {
        scanf("%d", &num);
        _sum += num;
        count[num] += 1;
    }
    
    for (int i = 1; i <= 1000; ++i) {
        if (count[i] > _max) {
            _max = count[i]; 
            _ind = i;
        }
    }
    printf("%d\n%d\n", _sum/10, _ind);

    return 0;
}