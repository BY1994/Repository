/*
14487 ������ ȿ�����̾�!! 

���� �з�: ����, �׸��� �˰���
���� ����� ���� ��� �Ÿ��� ���� �� �׸��� Ǯ�� �������? 
������ �ּ��� ������ �ƴ϶� �� ���� ���� ����� ���� ��� �� ���� ���ε�? 
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
