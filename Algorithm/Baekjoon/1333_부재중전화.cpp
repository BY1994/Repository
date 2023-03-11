/*
1333 부재중 전화 

시뮬레이션

울타리 설치하기나 나무 심기 같은 형태 

시뮬레이션 없이 수학적 풀이는 불가능한지 궁금하다. 

간단한 문제인데 코드로 정확하게 만들어내기 조금 까다로웠다.
구현하면서 약간의 실수는 break 조건을 설정했으면,
break 아닌 모든 조건을 다 커버해야하는데,
>= 가 아닌 > 로 잘못 쓰는 바람에 어떤 if 도 걸리지 않아서
무한 루프에 빠져버렸다. 
*/

#include <stdio.h>

int main(void) {
	int N, L, D;
	int song, call, end; 
	scanf("%d %d %d", &N, &L, &D);
	song = L;
	call = 0;
	end = N * L + (N-1) * 5;
	while (call < end) {
		if (song <= call && call < song + 5) break;
		if (call < song) call += D;
		if (call >= song + 5) song += 5 + L;
		//if (call >= song + 5 && song < end) song += 5 + L; // song < end 없어도 while 조건으로 커버됨 
	}
	printf("%d\n", call);
	return 0;
}

// 숏코딩
// https://www.acmicpc.net/source/3334125
#if 0
i;main(N,L,D){scanf("%d%d%d",&N,&L,&D);for(N*=L+5;i<N&&i%(L+5)<L;i+=D);printf("%d",i);}
#endif 
