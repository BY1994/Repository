/*
14487 욱제는 효도쟁이야!! 

백준 분류: 구현, 그리디 알고리즘
가장 비용이 많이 드는 거리를 빼는 게 그리디 풀이 방법인지? 
현재의 최선의 선택이 아니라 다 보고 가장 비용이 많이 드는 걸 빼는 것인데? 
*/

#include <stdio.h>

int main(void)
{
    int n, cost;
    int max_cost = 0;
    int total_cost = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &cost);
        if (max_cost < cost) max_cost = cost;
        total_cost += cost;
    }
    printf("%d\n", total_cost - max_cost);

    return 0;
}
