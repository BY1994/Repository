/*
2075 N��° ū ��

�켱���� ť 

�޸� ������ 12MB �̱� ������
��� ������ �� �����ؼ� �����ϰų� ť�� ���� �� ����. 
ť�� �ּ����� ������ �����ϵ��� �����Ͽ���. 
(���� �׽�Ʈ B�� ���̵�� ��Ÿ�ϰ� ����� ��) 

ó���� ���� �ź��� ū ������ �����ؾ��ϴ� �� �˾Ҵµ�,
���� ū �ź��� �Ųٷ� N ��°�� ���ϴ� �ſ���. 
�����ϰ� ���� ������ �� ���ͼ� �˾����� ������ ��ġ��� �ſ� ������.
ť ������ �� -�� ���̸� �Ǳ� ������....
*/

#include <stdio.h>
#include <queue>
using namespace std;

int main()
{
    int N, temp;
    priority_queue<int> q;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &temp);
        q.push(-temp);
    }
    for (int i = 1; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &temp);
            if (-q.top() < temp) {
                q.pop();
                q.push(-temp);
            }
        }
    }
    printf("%d\n", -q.top());
    return 0;
}
