/*
1411 비슷한 단어 

같은 문자들을 겹치지 않게 다른 문자로 바꾸면 두 단어를 비슷하다고 정의한다.
풀이를 생각하는데 시간이 걸렸다.
단순 counting 방법은 문자배열이 완전히 똑같은지 판단할 방법이 없으니,
같은 문자의 마지막 인덱스가 같은지로 비교하게 짰다. 
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
