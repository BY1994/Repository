/*
2729 이진수 덧셈 

맨 앞에 한 자리만 더 체크하게 하면 안 된다.
입력이 000 으로 시작할 수도 있다고 한다. 

아예 0 으로만 이루어지는 반례도 가능
https://www.acmicpc.net/board/view/96088 

반례
1
1100000100011100010001101010100111001101011111001111010000110101011000000001 010111011000000101111101011110010111110011100000010101
내 틀린 코드에는 2가 섞여 나옴 

반례 찾기
https://www.acmicpc.net/board/view/110605
입력
2
001 111101
10100001 10101101101011100100101100111000011001010110100101101010011011111
정답
111110
10101101101011100100101100111000011001010110100101101010110000000
=====
2022.10.18 출력 초과 
틀렸던 이유
(1) 결과의 앞에 붙어있는 0 을 무시하기 위해 while 문을 사용했는데,
마지막까지 0 이면 접근할 수 없는 음수 인덱스를 접근해버렸다.
=> 출력초과의 원인
(2) A 보다 B가 짧은 경우, 2 올림이 되다가 멈추는 지점에서
2가 그대로 남아버렸다.
=> 틀렸습니다의 원인 
A, B 합 연산과 올림처리를 따로 분리하였다. 
2023.03.12 맞았습니다 
*/

// 띄어쓰기를 scanf 를 받을 때 끝에 null 문자 처리가 제대로 안 되어서 틀린 거라고 생각
// => A, B 초기화를 매번 해주게 변경했는데도 아니었다. 
// 시작부터 0 은 무시하도록 while 문 돌릴 때 0 보다 작은 인덱스를 접근하도록 잘못 짜져있었다. 
// => 틀렸습니다
// 랜덤 인풋 생성으로 반례를 만들었더니
// 2 가 출력되는 경우가 있었다. 
#include <stdio.h>
#include <string.h>

int main()
{
    int T;
    scanf("%d", &T);
    while (T--) {
    	char A[82] = {0,};
		char B[82] = {0,};
        char result[82] = {0,};
        scanf("%s", A);
        scanf("%s", B);
        int lenA = strlen(A);
        int lenB = strlen(B);
        int lenR = 81;
        int i = 0;
        int j = 0;
        while (lenA--) {
            result[i++] = A[lenA] - '0'; 
        }
        while (lenB--) {
            result[j++] += B[lenB] - '0';
    	}
    	for (i = 0; i < 81; ++i) {
            result[i+1] += result[i] / 2;
            result[i] %= 2;
		}
        while (lenR >= 0 && result[lenR] == 0) lenR--;
        if (lenR < 0) {
	        printf("0\n");
	        continue;
		}
        while (lenR >= 0) {
            printf("%d", result[lenR--]);
        }
        printf("\n");
    }

    return 0;
}

// 출력 초과 
#if 0
#include <stdio.h>
#include <string.h>

char A[82];
char B[82];

int max(int A, int B) {
    return A > B ? A : B;
}

int main()
{
    int T;
    scanf("%d", &T);
    while (T--) {
        char result[82] = {0};
        scanf("%s", A);
        scanf("%s", B);
        int lenA = strlen(A);
        int lenB = strlen(B);
        int lenR = 81;
        int i = 0;
        int j = 0;
        while (lenA--) {
            result[i++] += A[lenA] - '0'; 
        }
        while (lenB--) {
            result[j++] += B[lenB] - '0';
            result[j] += result[j-1] / 2;
            result[j-1] %= 2;
        }
        while (result[lenR] == 0) lenR--;
        if (lenR < 0) {
	        printf("0\n");
	        continue;
		}
        while (lenR >= 0) {
            printf("%d", result[lenR--]);
        }
        printf("\n");
    }

    return 0;
}
#endif

// 틀렸습니다
#if 0 
#include <stdio.h>
#include <string.h>

char A[82];
char B[82];

int max(int A, int B) {
    return A > B ? A : B;
}

int main()
{
    int T;
    scanf("%d", &T);
    while (T--) {
        char result[82] = {0};
        scanf("%s", A);
        scanf("%s", B);
        int lenA = strlen(A);
        int lenB = strlen(B);
        int lenR;
        int i = 0;
        int j = 0;
        while (lenA--) {
            result[i++] += A[lenA] - '0'; 
        }
        while (lenB--) {
            result[j++] += B[lenB] - '0';
            result[j] += result[j-1] / 2;
            result[j-1] %= 2;
        }
        lenR = max(i, j);
        if (result[lenR]) printf("%d", result[lenR]);
        while (lenR--) {
            printf("%d", result[lenR]);
        }
        printf("\n");
    }

    return 0;
}
#endif
