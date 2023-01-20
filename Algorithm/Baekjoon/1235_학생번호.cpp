/*
1235 학생 번호

구현, 문자열 

한 학생을 기준으로 잡고 다른 학생들 겹치는 번호를 다 셀 것이므로
1000 x 1000 은 시간 제한 안에 들어옴 (2초 제한) 

다시 생각해보니 그냥 숫자 정해서 가능한지 완전탐색하면 되는 문제로 보임
크기가 더 컸다면 이분탐색일 것이고.. 
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
