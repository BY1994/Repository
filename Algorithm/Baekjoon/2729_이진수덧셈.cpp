/*
2729 ������ ���� 

�� �տ� �� �ڸ��� �� üũ�ϰ� �ϸ� �� �ȴ�.
�Է��� 000 ���� ������ ���� �ִٰ� �Ѵ�. 

�ƿ� 0 ���θ� �̷������ �ݷʵ� ����
https://www.acmicpc.net/board/view/96088 

�ݷ�
1
1100000100011100010001101010100111001101011111001111010000110101011000000001 010111011000000101111101011110010111110011100000010101
�� Ʋ�� �ڵ忡�� 2�� ���� ���� 

�ݷ� ã��
https://www.acmicpc.net/board/view/110605
�Է�
2
001 111101
10100001 10101101101011100100101100111000011001010110100101101010011011111
����
111110
10101101101011100100101100111000011001010110100101101010110000000
=====
2022.10.18 ��� �ʰ� 
Ʋ�ȴ� ����
(1) ����� �տ� �پ��ִ� 0 �� �����ϱ� ���� while ���� ����ߴµ�,
���������� 0 �̸� ������ �� ���� ���� �ε����� �����ع��ȴ�.
=> ����ʰ��� ����
(2) A ���� B�� ª�� ���, 2 �ø��� �Ǵٰ� ���ߴ� ��������
2�� �״�� ���ƹ��ȴ�.
=> Ʋ�Ƚ��ϴ��� ���� 
A, B �� ����� �ø�ó���� ���� �и��Ͽ���. 
2023.03.12 �¾ҽ��ϴ� 
*/

// ���⸦ scanf �� ���� �� ���� null ���� ó���� ����� �� �Ǿ Ʋ�� �Ŷ�� ����
// => A, B �ʱ�ȭ�� �Ź� ���ְ� �����ߴµ��� �ƴϾ���. 
// ���ۺ��� 0 �� �����ϵ��� while �� ���� �� 0 ���� ���� �ε����� �����ϵ��� �߸� ¥���־���. 
// => Ʋ�Ƚ��ϴ�
// ���� ��ǲ �������� �ݷʸ� ���������
// 2 �� ��µǴ� ��찡 �־���. 
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

// ��� �ʰ� 
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

// Ʋ�Ƚ��ϴ�
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
