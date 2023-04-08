/*
17404 RGB 거리 2 

처음 생각한 건 첫번째 값을 알아야하니까 매번 max 값 구할 때마다 첫번째 값을 저장하면 된다고 생각했는데,
항상 max 가 맞는 방향이라는 보장이 없다.
그래서 가능한 모든 경우의 수를 9가지로 나눠서 풀이하였다. 

- %3 인데 %2 로 하는 실수 있었음 
- 다른 풀이들은 DP 배열을 N 만큼 잡지 않고 어떻게 하는 것인지 이해 못함 
*/

#include <stdio.h>
#define min(a, b) (((a)<(b))?(a):(b))

int DP[1001][9]; // 0 번의 색 x 현재 3가지 가능 
int RGB[1001][3];

int main(void){
	int N;
	int ans = 99999999;
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d %d %d", &RGB[i][0], &RGB[i][1], &RGB[i][2]);
	}
	DP[1][0] = 9999; // 빨빨 불가
	DP[1][1] = RGB[0][0] + RGB[1][1]; // 빨초
	DP[1][2] = RGB[0][0] + RGB[1][2]; // 빨파

	DP[1][3] = RGB[0][1] + RGB[1][0]; // 초빨 
	DP[1][4] = 9999; // 초초 불가 
	DP[1][5] = RGB[0][1] + RGB[1][2]; // 초파
	
	DP[1][6] = RGB[0][2] + RGB[1][0]; // 파빨 
	DP[1][7] = RGB[0][2] + RGB[1][1]; // 파초
	DP[1][8] = 9999; // 파파 불가
	 
	for (int i = 2; i < N; ++i) {
		for (int k = 0; k < 9; k += 3) {
			for (int j = 0; j < 3; ++j) {
				int color1 = k+(j+1)%3;
				int color2 = k+(j+2)%3;
				DP[i][k+j] = min(DP[i-1][color1], DP[i-1][color2]) + RGB[i][j];
			}
		}
	}
	for (int i = 0; i < 9; ++i) {
		if ((i == 0) || (i == 4) || (i == 8)) continue;
		if (ans > DP[N-1][i]) ans = DP[N-1][i];
	}
	printf("%d\n", ans);
	return 0;
}


// 처음에 잘못 착안한 코드 
#if 0
#include <stdio.h>
int DP[1001][3];
int RGB[1001][3];
int first[1001][3];

int main(void){
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d %d %d", &RGB[i][0], &RGB[i][1], &RGB[i][2]);
	}
	first[0][0] = 0; first[0][1] = 1; first[0][2] = 2;
	DP[0][0] = RGB[0][0]; DP[0][1] = RGB[0][1]; DP[0][2] = RGB[0][2];
	for (int i = 1; i < N; ++i) {
		for (int j = 0; j < 3; ++j) {
			int color1 = (j+1)%3;
			int color2 = (j+2)%3;
			DP[i][j] = DP[i-1][color1];
			first[i][j] = first[i-1][color1];
			if (DP[i][j] > DP[i-1][color2]) {
				DP[i][j] = DP[i-1][color2];
				first[i][j] = first[i-1][color2];
			}
			DP[i][j] += RGB[i][j];			
		}
	}
	return 0;
}
#endif

// https://www.acmicpc.net/source/52687959
#if 0
#define I 1000000
#define m(a,b)(a<b?a:b)
#define f(a,b,c)for(int i=a;i<b;i++)c
#define g(p)f(0,3,scanf("%d",&p[i]))
main(){int s[3],n,v=I;scanf("%d",&n);g(s);int d[9]={s[0],I,I,I,s[1],I,I,I,s[2]};f(1,n,{g(s);int t[9];f(0,9,t[i]=m(d[(i+1)%3+(i/3*3)],d[(i+2)%3+(i/3*3)])+s[i%3];)f(0,9,d[i]=t[i];)})f(0,9,if(i%3!=i/3)v=m(v,d[i]);)printf("%d",v);}
#endif 

// https://www.acmicpc.net/source/17922013
#if 0
#include<cstdio>
#include<algorithm>
#define D 1111111
#define x(a,b,c) t[a][i]=min(e[b][i],e[c][i])+d[a];
using namespace std;
int n,d[3],e[3][3],t[3][3],i,j,k;
int main(){
    scanf("%d",&n);
    scanf("%d%d%d",d,d+1,d+2);
    for(i=0;i<3;i++)for(j=0;j<3;j++)e[i][j]=i==j?d[i]:D;
    for(j=1;j<n;j++){
        scanf("%d%d%d",d,d+1,d+2);
        for(i=0;i<3;i++){x(0,1,2)x(1,0,2)x(2,0,1)}
        for(i=0;i<3;i++)for(k=0;k<3;k++)e[i][k]=t[i][k];
    }
    for(n=D,i=0;i<3;i++)for(j=0;j<3;j++){n=min(n,i==j?D:e[i][j]);}
    printf("%d",n);
}
#endif

// https://www.acmicpc.net/source/18024670
#if 0
a[3][3], t[3][3], r, g, b, n, m = 1000000;
f(int n1, int n2) { return (n1 < n2 && n1) || !n2 ? n1 : n2; }
main() {
	scanf("%d %d %d %d", &n, &a[0][0], &a[1][1], &a[2][2]);
	for (int i = 1; i < n; i++) {
		scanf("%d %d %d", &r, &g, &b);
		for (int j = 0; j < 3; j++) {
			t[j][0] = r + f(a[j][1], a[j][2]);
			t[j][1] = g + f(a[j][0], a[j][2]);
			t[j][2] = b + f(a[j][0], a[j][1]);
		}
		for (int j = 0; j < 3; j++)
			for (int k = 0; k < 3; k++)
				a[j][k] = (i != 1 || j != k) * t[j][k];
	}
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			if (m > a[i][j] && (i != j || n == 1))
				m = a[i][j];
	printf("%d", m);
}
#endif
