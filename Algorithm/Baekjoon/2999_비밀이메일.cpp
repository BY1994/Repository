/*
2999 비밀 이메일 

구현
R와 C의 대소 관계를 잘못 이해해서 틀렸음 
*/

#include <stdio.h>
#include <math.h>
#include <string.h>

char message[101];
char array[101][101];

int main(void)
{
    scanf("%s", message);
    int n = strlen(message);
    int C = sqrt(n);
    int R;
    int ind = 0;
    if (C*C == n) {
    	R = C;
	} else {
	    for (int i = C+1; i <= n; ++i) {
	        if (n % i == 0) {
	            C = i;
	            break;
	        }
	    }
	    R = n/C;		
	}
    for (int j = 0; j < C; ++j) {
        for (int i = 0; i < R; ++i) {
            array[i][j] = message[ind++];
        }
    }
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            printf("%c", array[i][j]);
        }
    }
    printf("\n");
    return 0;
}

// 1등 풀이 
#if 0
#include <stdio.h>
int main(){
	int r,c,i,j;char C[101];
	gets(C);for(c=0;C[c];c++);for(r=c;;r--)if(!(c%r)&&r<=c/r){c/=r;break;}
	for(j=0;j<r;j++)for(i=0;i<c;i++)putchar(C[r*i+j]);
}
#endif 
