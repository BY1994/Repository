/*
3059 �������� �ʴ� ������ �� 

����, ���ڿ�, ��Ʈ����
���� ���� �з��� ��Ʈ������ ��������, ���ĺ� 26���ڸ� ����ϸ� �Ǳ� ������
��Ʈ ������ �����ϱ⿡ �� ���� �� ���� ��Ʈ �������� �����Ͽ���. 
*/

#include <stdio.h>

char S[1001];

int main(void)
{
    int T;
    scanf("%d", &T);
    while (T--) {
        int count = 0; int ans = 0;
        scanf("%s", S);
        for (int i = 0; S[i]; ++i) {
            count |= 1 << (S[i]-'A');
        }
        for (int i = 0; i < 26; ++i) {
            if ((count >> i) & 1) continue;
            ans += 'A' + i;
        }
        printf("%d\n", ans);
    }

    return 0;
}
