/*
2566 �ִ� 

���� 

���� �Խ��ǿ� �ִ� ���� ��κ��� �ݷʰ�
�� 0���� ������ ��쿴��.
�ʱ�ȭ ó���� ����� �� �Ǿ������� �ش� �ݷʿ� �ɸ��� �ȴ�.
�ش� �����ε� �亯�� �� �޸� ������ �־� �亯�� �߰��Ͽ���. 
https://www.acmicpc.net/board/view/102878 
*/

#include <stdio.h>

int main(void)
{
    int x = 1; int y = 1;
    int max = -1;
    int num;

    for (int i = 1; i < 10; ++i) {
        for (int j = 1; j < 10; ++j) {
            scanf("%d", &num);
            if (num > max) {
                max = num;
                x = i, y = j;
            }
        }
    }
    printf("%d\n%d %d\n", max, x, y);

    return 0;
}

