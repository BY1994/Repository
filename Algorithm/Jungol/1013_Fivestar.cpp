//dfs 공식 만들 때... chk 방문 step 이랑 누적합... 

/*
2 6
*****.
.*****
2 이어야하는데 1이 나옴... 
=> 5개 잘 만나면 cnt+=1을 항상 해줘야하는데,
마지막이 5인 애만 해주니까 첫번째 줄은 계산 못했음
if문 밖으로 cnt+=1을 빼줘서 해결함 

문제 예제 
5 6
.*....
.*****
.*....
*****.
.*....

제출했더니 틀린 부분
5 10
**********
********.*
**********
*.********
********** 
12가 나와야하는데 13이 나옴 
=> 중간에 . 만나면 무조건 return 100 하게 짰는데,
그게 아니라 그 앞에 6 ... 이런 큰 수 있으면 겹치게 덮으면 되니까
조건을 더 세분화해야했다. 문제 없이 덮는 경우 있는 거니까!! 

5 10
*********.
.******.*.
.*.******.
**********
.*..*****.
9가 나와야하는데 -1이 나옴
=> s==M인 조건 처리를 먼저하는 바람에 마지막에 .이 있는 애는 문제가 있는 앤 줄 알고 끝내버렸다.... 

*/

#include <stdio.h>

// 세로로 누적한 개수 rcnt
// 누적 사용할 때는 0번 비워두는 게 좋다 
int N, M, rcnt[6][11], ccnt[6][11], ans = 100, chk[11];

int Min(int a, int b) {
	return (a > b)? b: a;
}

// 불가능한 경우 100을 리턴?? 
int calc(int cnt)
{
	// 세로 
	for (int i = 1; i <= N; i++){
		// 시작점이 여러개 있을 수 있음
		int s = 1, j;
		while(s <= M){
			// 현재의 시작점 정하기 (chk 되어있으면 패스함) 
			for (j = s; j <= M; j++) if (chk[j] == 0 && ccnt[i][j] >= 1) break;
			s = j; // 시작점 정함
			if (s > M) break;
			//printf("## i %d 시작점 정해짐!! %d\n", i, s);
			// 거기서부터 5개씩 이동하는데 다 가능해야함
			// => 5까지 못 만나면 100 리턴해야 함 
			for (; s<=j+5-1; s++) {
				//printf("## for 문 %d\n", s);
				// 1) 이 조건이 선행 되어야함!!! 

				// 5 를 못 만나고 0으로 리셋... 
				// 그런데 0 (.을 만나도) 이어도 그 앞까지 자리가 5 이상이면 상관 없을 듯.. 
				// return 100 말고 break 하면 될 듯 
				if (ccnt[i][s] == 0) {
					if (ccnt[i][s-1] < 5) return 100; // . 을 만났는데 * 이 5개 안 되고 끝겨야 문제!! 
					else break;	
				}
				
				// 2) s==M인 경우에 0 만난 경우 예외 처리가 안됨!! 
				
				// 5개 가기 전에 벽에 부딪히면 5 이상이어야함
				// => 이 조건도 만족 안 되면 100 리턴해야함 
				if (s == M) {
					if (ccnt[i][s] < 5) return 100;
					//else cnt += 1; 
					s++; // s가 M을 넘어야 while문도 탈출함 
					break;
				} 
				
			}	
			// 5개 잘 만났으면
			cnt += 1;	
		} 
	}
	//printf("################### cnt %d\n", cnt); 
	return cnt;
}

void dfs(int step, int cnt)
{
	// debugging
	/*
	int check = 0;
	for (int a = 3; a< M-1; a++) if (chk[a] != 0) {
		check = 1;
		break;	
	}
	if (check == 0 && chk[1] == 0 && chk[2] == 1 && chk[M-1] == 1 && chk[M] == 0) check = 0;
	else check = 1;
	if (check == 0) printf("###################################### 이 경우\n");
	
	printf("## dfs step %d cnt %d\n", step, cnt); 
	*/
	if (step > M) {
		ans = Min(ans, calc(cnt));
		return;
	}
	if (rcnt[5][step] == 5) {
		chk[step] = 1;
		dfs(step + 1, cnt + 1);
		chk[step] = 0;
	}
	dfs(step + 1, cnt);
}

int main()
{
	char ch;
	scanf("%d %d", &N, &M);
	for (int i = 1; i <= N; i++) for (int j = 1; j <= M; j++) {
		scanf(" %c", &ch);
		if (ch == '*') {
			rcnt[i][j] += rcnt[i-1][j] + 1;
			ccnt[i][j] += ccnt[i][j-1] + 1;
		}
	}
	if (N < 5) ans = calc(0); // greedy를 calc로 대체해도 될  
	else dfs(1, 0); // 현재까지 세로로 놓은 개수 0
	if (ans == 100) ans = -1;
	printf("%d\n", ans);
	return 0; 
}
