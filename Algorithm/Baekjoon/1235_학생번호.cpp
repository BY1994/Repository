/*
1235 �л� ��ȣ

����, ���ڿ� 

�� �л��� �������� ��� �ٸ� �л��� ��ġ�� ��ȣ�� �� �� ���̹Ƿ�
1000 x 1000 �� �ð� ���� �ȿ� ���� (2�� ����) 

�ٽ� �����غ��� �׳� ���� ���ؼ� �������� ����Ž���ϸ� �Ǵ� ������ ����
ũ�Ⱑ �� �Ǵٸ� �̺�Ž���� ���̰�.. 
*/

#include <stdio.h>
#include <string.h>

char students[1001][101];
int count[1001][101];

int main(void)
{
    int N, len, k = 0;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
        scanf("%s", students[i]);
    }
    len = strlen(students[0]);
    for (int i = 0; i < N; ++i) {
        for (int j = i+1; j < N; ++j) {
            for (int ind = len-1; ind >= 0; --ind) {
                if (students[i][ind] == students[j][ind]) count[i][len-ind] += 1;
                else break;
            }
        }
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 1; j <= 100; ++j) {
            if (count[i][j] == 0) {
                if (k < j) k = j;
                break;
            }
        }
    }
    printf("%d\n", k);
    return 0;
}
