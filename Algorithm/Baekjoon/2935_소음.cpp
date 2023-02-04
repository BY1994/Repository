/*
2935 소음 

문자열, 사칙연산 
*/

#include <stdio.h>
char A[101], B[101];

int main(void)
{
    int lenA, lenB;
    char op;
    scanf("%s", A);
    scanf(" %c", &op);
    scanf("%s", B);
    
    lenA = strlen(A)-1;
    lenB = strlen(B)-1;
    
    if (op == '*') {
        printf("1");
        for (int i = 0; i < lenA + lenB; ++i) printf("0");
        printf("\n");
    } else {
        if (lenA >= lenB) {
            for (int i = lenB, j = lenA; i >= 0; --i, --j) A[j] += B[i] - '0';
            printf("%s\n", A);
        } else {
            for (int i = lenA, j = lenB; i >= 0; --i, --j) B[j] += A[i] - '0';
            printf("%s\n", B);
        }
    }

    return 0;
}
