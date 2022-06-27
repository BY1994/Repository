/*
2616 질문 게시판에 올라온 코드의 반례 찾기 코드 
https://www.acmicpc.net/board/view/16440
랜덤 input 생성은 2616_소형기관차.py 을 참고 
*/
#include <stdio.h>
#include <algorithm>
using namespace std;
int n,m,i,j,h,p;
struct ABC{
    int a,x;
}e[50001];
bool compare(ABC x,ABC y){
    return x.a<y.a;
}
int main(){
	FILE *fin = freopen("2616_input.txt", "r", stdin);
	FILE *fout = fopen("2616_output_compare.txt", "w");

	for (register int test = 0; test < 100; test ++) {
	h = 0; p = 0;
    scanf("%d",&n);
    for (i=0;i<n;i++){
        scanf("%d",&e[i].a);
        e[i].x=i+1;
        h+=e[i].a;
    }
    scanf("%d",&m);
    sort(e,e+n,compare);
    for (i=0;i<n;i++){
        if (n-p==m*3) break;
        if ((e[i].x%m==0 || n-e[i].x%m==0) && m!=1) continue;
        h-=e[i].a;
        p++;
    }
    printf("%d\n",h);
    fprintf(fout, "%d\n", h);		
	}
    fclose(fin);
    fclose(fout);
    return 0;
}

