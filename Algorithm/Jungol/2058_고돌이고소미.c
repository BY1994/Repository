#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// 정올 2058 고돌이 고소미
// 191106

// 틀렸던 거
// - 설마 8x8이겠어 하고 for문으로 8번만 돌려고 했던거...
// - 주변 가시 말고 아예 같은 공간 오는 거 고려 안 함
// - 괜히 집에 도착하면 99로 바꾸겠다고 했다가 visited 인덱스 오류도 뜨고 둘 다 집에 가도 갔는지 체크 못한다. 99 로 못 돌아서 집 위치로 바꿔놓는 바람에...

// 1차 시도 런타임 에러 -> 큐의 사이즈를 늘려보자 (둘이 동시에 움직여서 큐가 크게 필요함)
// 2차 시도 틀림 => 고돌이가 고소미 집을 막아버림... (집에 도착했다고 멈추지 말 것)

/*
내가 틀리는 거
6
6 1 4 6
5 3 6 2
0 0 0 0 0 0
0 1 1 1 1 1
0 0 0 1 0 0
0 1 1 1 1 0
0 0 0 0 0 1
0 0 0 0 0 0

// 최대 한 칸이면 안 움직여도 된다는 소리?! ... 이거 때문에 두번째 케이스가 집을 못 찾아갔나 => 그렇다
5
1 5 5 5
5 5 1 5
0 0 0 0 0
0 1 1 1 1
0 0 0 1 1
0 1 1 1 1
0 0 0 0 0

// 이게 집을 만난다고 멈추면 안 된다.
// 내가 집에 들어가서 길을 막아버리는 바람에 고소미가 집에 못갔다.....
7
1 6 3 6
3 6 1 6
1 0 1 0 1 0 1
1 0 1 0 1 0 1
1 1 1 1 1 0 1
1 0 1 0 1 0 1
1 0 1 0 1 0 1
0 0 0 0 0 0 0
1 1 1 1 1 1 1

*/

int loca[2][2]; // 앞은 성별, 뒤는 xy
int home[2][2];
int town[30][30];
int visited[30][30][30][30]; // 상태가 4개 정보니까 4차원 배열
int dx[9] = { -1, -1, -1, 0, 1, 1, 1, 0, 0 };
int dy[9] = { -1, 0, 1, 1, 1, 0, -1, -1, 0 };
int rdptr = 0, wrptr = 0;

struct queue {
	int loca[2][2];
	int t;
};

struct queue q[1000000];// 사이즈를 몇으로 계산해야하지... 전체 판 크기 C 2 

int is_available(int mx, int my, int fx, int fy)
{
	if (mx == fx && my == fy) return 0; // 주변만 신경쓰다가 둘이 같은 공간에 오는 걸 생각 못 했다...

	// m의 8방향에 f가 있는지 확인
	for (int d = 0; d < 8; d++)
	{
		//if (mx == 99) mx = home[0][0];
		//if (fx == 99) fx = home[1][0];

		if (mx + dx[d] == fx && my + dy[d] == fy) return 0;
		if (fx + dx[d] == mx && fy + dy[d] == my) return 0;
		
	}
	return 1;
}

int main(void)
{
	int N;
	int ans = 0;
	int remain = 2;

	scanf("%d", &N);
	scanf("%d %d %d %d", &loca[0][0], &loca[0][1], &home[0][0], &home[0][1]);
	scanf("%d %d %d %d", &loca[1][0], &loca[1][1], &home[1][0], &home[1][1]);

	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			scanf("%d", &town[i][j]);
		}
	}

	q[wrptr].loca[0][0] = loca[0][0], q[wrptr].loca[0][1] = loca[0][1];
	q[wrptr].loca[1][0] = loca[1][0], q[wrptr].loca[1][1] = loca[1][1];
	visited[loca[0][0]][loca[0][1]][loca[1][0]][loca[1][1]] = 1;
	wrptr++;
	
	while (rdptr < wrptr)
	{
		int cur[2][2], curt, next[2][2];
		cur[0][0] = q[rdptr].loca[0][0], cur[0][1] = q[rdptr].loca[0][1];
		cur[1][0] = q[rdptr].loca[1][0], cur[1][1] = q[rdptr].loca[1][1];

		curt = q[rdptr].t;
		rdptr++;
		
		//printf("뭐야!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
		//printf("%d %d %d %d %d\n", cur[0][0], cur[0][1], cur[1][0], cur[1][1], curt);
		//printf("\n");

		// 고돌이 8방향 돌 때
		for (int d1 = 0; d1 < 9; d1++)
		{
			int g = 0;
			next[g][0] = cur[g][0] + dx[d1], next[g][1] = cur[g][1] + dy[d1];
			// 집에 도착했다고 멈추면 안 됨!!!!
			//if (cur[g][0] == home[g][0] && cur[g][1] == home[g][1]) next[g][0] = home[g][0], next[g][1] = home[g][1]; // 밑에서 visited 체크하려면 여기가 99면 안 될 것 99 대신 집이냐로 변경
			if (next[g][0] < 1 || next[g][0] > N || next[g][1] < 1 || next[g][1] > N) continue;
			if (town[next[g][0]][next[g][1]] == 1) continue;
			

			// 고소미 8방향 돌면서
			for (int d2 = 0; d2 < 9; d2++)
			{
				int g = 1;
				next[g][0] = cur[g][0] + dx[d2], next[g][1] = cur[g][1] + dy[d2]; // 내가 실수하는 건 뻔하지...d2라고 안 하고 d1이라고 해놨다... 복붙 문제...
				//if (cur[g][0] == home[g][0] && cur[g][1] == home[g][1]) next[g][0] = home[g][0], next[g][1] = home[g][1]; // 밑에서 visited 체크하려면 여기가 99면 안 될 것
				if (next[g][0] < 1 || next[g][0] > N || next[g][1] < 1 || next[g][1] > N) continue;
				if (town[next[g][0]][next[g][1]] == 1) continue;
				if (visited[next[0][0]][next[0][1]][next[1][0]][next[1][1]] == 1) continue;

				//printf("여기까지는\n");
				// 둘의 방향이 정해졌으면, 서로 영역 침범하지 않는지 확인하고 가능하면 큐에 넣는다
				if (is_available(next[0][0], next[0][1], next[1][0], next[1][1]))
				{
					remain = 2; // 이게 잘못 빠지는 경우가 있나?
					
					if (next[0][0] == home[0][0] && next[0][1] == home[0][1]) remain -= 1; //next[0][0] = 99;
					if (next[1][0] == home[1][0] && next[1][1] == home[1][1]) remain -= 1; //next[1][0] = 99;

					q[wrptr].loca[0][0] = next[0][0], q[wrptr].loca[0][1] = next[0][1];
					q[wrptr].loca[1][0] = next[1][0], q[wrptr].loca[1][1] = next[1][1];
					q[wrptr].t = curt + 1;
					wrptr++;

					//if (next[0][0] == 99) { next[0][0] = home[0][0]; remain -= 1; } // 이거 안 하면 밑에 visited에서 오류난다...
					//if (next[1][0] == 99) { next[1][0] = home[1][0]; remain -= 1; }
					
					// 도착 체크
					if (remain == 0) { break; }

					// 넣을 때 visit 체크
					visited[next[0][0]][next[0][1]][next[1][0]][next[1][1]] = 1; // 99를 접근하려고 하니 오류가 났다...ㅠ 
					
					// 다음에 들어가는거
					// printf("8개 들어가야함 %d %d %d %d\n", next[0][0], next[0][1], next[1][0], next[1][1]);

				}
			}
			if (remain == 0) { break; }
		}
		if (remain == 0) { ans = curt + 1; break; }
	}

	printf("%d\n", ans);
	return 0;

}