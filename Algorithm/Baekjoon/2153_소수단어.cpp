/*
2153 �Ҽ� �ܾ�

����
�Ҽ� ������ ���������� �������� �ŷ� �ߴ�.
�������� ���� �������� ���� Ȯ���� ���� �״ϱ�
for ���� ��������� �� ���Ŷ�� �����ߴ�. 
*/

#include <stdio.h>

char dict[128];
char word[21];

void init(void) {
    for (int i = 1; i <= 26; ++i) {
        dict[i+'a'-1] = i;
        dict[i+'A'-1] = i+26;
    }
}

int main(void)
{
    int N = 0;
    int flag = 0;

    init();
    scanf("%s", word);
    for (int i = 0; word[i]; ++i) {
        N += dict[word[i]];
    }
    for (int i = 2; i < N; ++i) {
        if (N % i == 0) {
            flag = 1;
            break;
        }
    }
    if (flag) printf("It is not a prime word.\n");
    else printf("It is a prime word.\n");

    return 0;
}
