/*
1673 치킨 쿠폰

초등학교 때 병 교환하기 문제...

k 는 반드시 1보다 크다는 조건 있음  

처음 푼 코드는 예제가 맞아서 맞는 방향이라고 생각했는데,
나머지 처리를 안 해서 생기는 오류가 있었다
직접 만들어본 반례
5 3
정답 7
잘못된 답 6 

* 질문 게시판 반례 찾기 
long long 범위여야한다고 생각해서 만든 반례
1000000000 2
1999999999 
그러나 int 범위로도 넘어가지 않았다.
아래 코드의 문제는 int 여서가 아니라 입력을 1개만 받아서였다.
https://www.acmicpc.net/board/view/59059

재귀를 써서 segmentation fault 가 발생하는 코드
https://www.acmicpc.net/board/view/32147

* 최적화
k 가 3이면,
3 개 빼놓고 (+1) 
나머지 2개씩 몇개 묶이는지 보면 바로 계산 가능 ((n-3) / 2)
3 개를 먹으면 1개가 되기 때문에 나머지 2개와 합쳐서 다시 3개가 된다!
3 2 2 2 2 ... 이런 식이면 2가 나오는 개수만큼 계속 오른쪽으로 3개를 만들어갈 수 있음
 
* 숏코딩 
include 생략 가능 (백준 컴파일러에서 stdio.h 붙여줌) 
main 에 int 제거 가능 (백준 컴파일러에서 default 로 붙여줌) 
int main 이어도 return 0; 생략 가능 
main 안에 argument 로 int 변수들 선언 가능
%d %d 띄어쓸 필요 없음
scanf() > 0 으로 EOF 처리할 필요 없음 
*/

// 숏코딩 
// 백준 한정 가능 (main 앞에 int 자동으로 붙여줌) 
#if 1
main(n,k){while(~scanf("%d%d",&n,&k))printf("%d\n",n+1+(n-k)/(k-1));}
#endif

// 정답 코드 2
#if 0
#include <stdio.h>

int main(void)
{
    long long n, k;
    while (scanf("%lld %lld", &n, &k) > 0)
        printf("%lld\n", n + 1 + (n-k) / (k-1));
    return 0;
}
#endif 

// 정답 코드 
#if 0
#include <stdio.h>

int main(void)
{
    long long n, k, chicken;
    while (scanf("%lld %lld", &n, &k) > 0) {
        chicken = n;
        while (n/k) {
            chicken += n/k;
            n = n/k + n%k;
        }
        printf("%lld\n", chicken);
    }

    return 0;
}
#endif

// 틀린 코드 
#if 0
#include <stdio.h>

int main(void)
{
    long long n, k, chicken;
    while (scanf("%lld %lld", &n, &k) > 0) {
        chicken = 0;
        while (n) {
            chicken += n;
            n /= k;
        }
        printf("%lld\n", chicken);
    }

    return 0;
}
#endif
