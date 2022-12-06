/*
2160 �׸� �� 

�ݷ�: ������ �ٸ� ��츦 ����ؼ� �ʱ�ȭ�� �ʿ���
�̰� ������ �� �� Ʋ�� 
https://www.acmicpc.net/board/view/75825
Input:
2
.......
.......
.......
.......
.......
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX

Output:
1 2

4 �� ������ ���� ��������
35 �� ���̹Ƿ� 0�� 1�� ��ȯ�ؼ�
unsigned long long �� bit �� ������
xor �������� ������ ã�� �� ���� �� ����. 
*/

#include <stdio.h>

char figure[51][5][8];

int main(void)
{
    int N;
    scanf("%d", &N);
    for (int n = 1; n <= N; ++n) {
        for (int i = 0; i < 5; ++i) {
            scanf("%s", figure[n][i]);
        }
    }
    
    int min = 35;
    int ans[2] = {1, 2};
    for (int first = 1; first <= N; ++first) {
        for (int second = first + 1; second <= N; ++second) {
            int diff = 0;
            for (int i = 0; i < 5; ++i) {
                for (int j = 0; j < 7; ++j) {
                    if (figure[first][i][j] != figure[second][i][j])
                        diff++;
                }
                if (min < diff) break;
            }
            if (min > diff) {
                min = diff;
                ans[0] = first;
                ans[1] = second;
            }
        }
    }
    printf("%d %d\n", ans[0], ans[1]);

    return 0;
}
