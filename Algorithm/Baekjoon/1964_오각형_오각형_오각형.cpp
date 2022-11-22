/*
1964 오각형 오각형 오각형 

DP (수열) 
*/

#include <stdio.h>

int arr[10000001];

int main(void)
{
    int n;
    int add = 7;
    scanf("%d", &n);
    arr[1] = 5;
    for (int i = 2; i <= n; ++i) {
        arr[i] = (arr[i-1] + add) % 45678;
        add += 3;
    }
    printf("%d\n", arr[n]);
    return 0;
}
