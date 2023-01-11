/*
1411 ����� �ܾ� 

���� ���ڵ��� ��ġ�� �ʰ� �ٸ� ���ڷ� �ٲٸ� �� �ܾ ����ϴٰ� �����Ѵ�.
Ǯ�̸� �����ϴµ� �ð��� �ɷȴ�.
�ܼ� counting ����� ���ڹ迭�� ������ �Ȱ����� �Ǵ��� ����� ������,
���� ������ ������ �ε����� �������� ���ϰ� ®��. 
*/

#include <stdio.h>
char words[101][51];

int main(void)
{
    int N;
    int ans = 0;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) scanf("%s", words[i]);
    for (int a = 0; a < N; ++a) {
        for (int b = a+1; b < N; ++b) {
            int first[128] = {0,};
            int second[128] = {0,};
            ans++;
            for (int i = 0; words[a][i]; ++i) {
                if (first[words[a][i]] != second[words[b][i]]) {
                    ans--;
                    break;
                }
                first[words[a][i]] = i+1;
                second[words[b][i]] = i+1;
            }
        }
    }
    printf("%d\n", ans);

    return 0;
}
