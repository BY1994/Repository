/*
17952 ������ ������ �ʾ�!

���� 
stack ������ ��� ��Ƽ� �ð��ʰ� �� �� �� (���� �߸� ����)
������ ��Ÿ�� ������ �����ϴµ�, ���۰� �־�������. 
*/

#include <stdio.h>

int N, ans;
struct homework {
    int score;
    int remain;
}stack[1000001];
int sp;

int main(void)
{
    int val, score, remain;
    scanf("%d", &N);
    while (N--) {
        scanf("%d", &val);
        if (val) {
            scanf("%d %d", &score, &remain);
            if (--remain)
                stack[sp++] = {score, remain};
            else
                ans += score;
        } else if (sp > 0) {
            if (--stack[sp-1].remain == 0) {
                ans += stack[sp-1].score;
                sp--;
            }
        }
    }
    printf("%d\n", ans);
    return 0;
}
