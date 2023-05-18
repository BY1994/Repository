/*
11538 Pyro Tubes

비트마스킹
총 18개의 튜브가 있는데,
원래 불을 뿜으려는 튜브에서 2개까지만 달라도 허용된다.
주어진 보기 중 대체 가능한 형태의 개수 출력하기

완전탐색으로 하려면 25만개마다 나머지 25만개와의 대체 가능 여부를 확인해야하기 때문에
(대체 가능 여부 확인은 또 18번 for문 돌아야한다.)
시간 제한이 13초더라도 부족하다.

그래서 어차피 18개이므로 1개 혹은 2개가 다른 경우의 수를 직접 만들어서
(18*18 은 324이므로 순회해도 부담이 되지 않는다.)
주어진 보기 중 존재하는지 확인하도록 했다. 
*/

#include <stdio.h>
int c, l;
int cand[343];
int pyro[262145];
int L[250001];

void init(void)
{
    for (int i = 0; i < 17; ++i) {
        for (int j = i+1; j < 18; ++j) {
            cand[c++] = (1 << i) | (1 << j);
        }
    }
    for (int i = 0; i < 18; ++i) {
        cand[c++] = (1<<i);
    }
}

int main(void)
{
    init();
    for (int i = 0; i < 250000; ++i) {
        scanf("%d", &L[i]);
        if (L[i] == -1) break;
        pyro[L[i]] = 1;
        l++;
    }
    
    for (int i = 0; i < l; ++i) {
        int count = 0;
        for (int j = 0; j < c; ++j) {
            int alter = L[i] ^ cand[j];
            if (alter >= L[i] && pyro[alter]) count++;
        }
        printf("%d:%d\n", L[i], count);
    }

    return 0;
}
