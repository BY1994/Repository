
///=============== main.cpp ===============

#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <stdio.h>


/*
기본 인풋
1
15
1 300 10 8 5 7 14 13
1 1000 4 4 5 4 8 6
2 1000 300
1 500 3 9 5 5 3 12
2 500 300
2 500 1000
2 300 500
3

틀리는 케이스 => 들어오는 방향만 가리키도록 수정하고 맞음
1
50
1 3 2 2 43 3 43 4
1 4 6 7 39 3 44 8
1 5 46 2 3 43 48 3
2 3 5
2 4 3
2 5 3
2 3 4
3

틀리는 케이스 2 => 답체크 구문이 if id인데 if d로 그대로 남아있었다 (복사의 흔적)
1
30
1 11 3 11 3 4 4 14
1 999 2 16 4 9 4 16
2 11 999
2 999 11
1 250 7 2 9 13 11 2
2 999 250
2 250 11
1 31 8 16 6 4 11 16
2 999 31
2 31 11
1 423 2 3 3 7 3 9
2 423 11
2 31 423
3
*/

// 모서리에서 모서리 뛰어다님
// 그렇게 풀면 안 됨. 거기가 누군가 지나다니는 EV 길이어야만 옮겨타는 것이다.

// 틀린 이유 (반례) -> 들어오는 방향으로 이거가 가능하다 체크해야 저 반례를 잡을 수 있다 (들어가기 전에 그걸 체크할 거니까)
// 그냥 들어오는 거 나가는 거 다 가능하다 해버리면 얘가 모서리에서 마음대로 이상한 방향으로 튀어나간다
// 외벽을 따라 가는게 아니라 모서리에서 또 모서리로 점프해버림

int mymap[51][51];
int poss[4][51][51]; // 각 방향으로 가능한지 체크 // 가능한 길을 1로 체크할 것
int N;
int labs[1001][3]; // 연구실 ev
int visited[4][51][51];
int qx[100000];
int qy[100000];
int qd[100000];
int qt[100000];
int wrptr, rdptr;

int dx[4] = { 0, 0, 1, -1 }; // 동서남북 진행방향별 다음 위치
int dy[4] = { 1, -1, 0, 0 };


///=============== user.cpp ===============
void initUser(int tableSize) {
	// 테케마다 초기화해줘야하는 애들
	N = tableSize;
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= N; j++) mymap[i][j] = 0;

	for (int k = 0; k < 4; k++)
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++) poss[k][i][j] = 0;
}

void makeLabRoom(int id, int sr, int sc, int h, int w, int vr, int vc) {

	// 2차원 맵에 연구실 표시 1, 모서리 표시 2 EV 위치 표시 x
	for (int i = sr; i < sr + h; i++)
		for (int j = sc; j < sc + w; j++) mymap[i][j] = 1; // 여긴 연구실

	// 모서리 인덱스
	mymap[sr - 1][sc - 1] = 2, mymap[sr-1][sc+w] = 2, mymap[sr+h][sc-1] = 2, mymap[sr+h][sc+w] = 2;
	
	// EV 위치가 맵에서 왼쪽, 위쪽 오른쪽 아래쪽 어딘지 파악하기
	if (vr == sr + h - 1) labs[id][2] = 1, labs[id][0] = vr+1, labs[id][1] = vc; // 남
	else if (vr == sr) labs[id][2] = 0, labs[id][0] = vr-1, labs[id][1] = vc; //북
	else if (vc == sc) labs[id][2] = 3, labs[id][0] = vr, labs[id][1] = vc-1; // 서
	else labs[id][2] = 2, labs[id][0] = vr, labs[id][1] = vc+1; // 동-> 위치는 남으로

	// 그 랩에서 출발할 때의 방향
	// EV 위치도 밖으로 빼서 두기

	// 갈 수 있는 방향 미리 체크해두기 => simple! 해답을 위해!
	// 여기 반례잡기 위한 수정이 필요하다 => 들어올 때 이 방향이어야 가능하다로 수정! (나를 가리키는 방향 화살표)
	// 남쪽에 있는 길 (서쪽으로 이동) sc-1~sc+w-1 & 북쪽에 있는 길 (동쪽으로 이동) sc~sc+w
	for (int j = sc - 1; j <= sc + w-1; j++) poss[1][sr + h][j] = 1;
	for (int j = sc; j <= sc + w; j++) poss[0][sr - 1][j] = 1;
	//  서쪽에 있는 길 (북쪽으로 이동) sr-1~sr+h-1& 동쪽에 있는 길 (남쪽으로 이동) sr~sr+h
	for (int i = sr - 1; i <= sr + h-1; i++) poss[3][i][sc - 1] = 1;
	for (int i = sr; i <= sr + h; i++) poss[2][i][sc + w] = 1;

	// for (int i = sr - 1; i <= sr + h; i++) poss[3][i][sc - 1] = 1, poss[2][i][sc + w] = 1; // 수정 전 모습
}

int getShortestPath(int s, int e) {
	// 해당 위치부터 bfs를 돌면서 도착점에 가면 답을 꺼냄.... (이상한 방향으로 가는 애는 컨트롤 못하나...)
	for (int k = 0; k < 4; k++)
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++) visited[k][i][j] = 0;

	// 초기화
	rdptr = wrptr = 0;
	qx[wrptr] = labs[s][0], qy[wrptr] = labs[s][1], qd[wrptr] = labs[s][2], qt[wrptr] = 1; // 처음에 1초
	visited[qd[wrptr]][qx[wrptr]][qy[wrptr]] = 1; // 그 위치 방문한 거!
	wrptr++;

	while (rdptr < wrptr)
	{
		int x = qx[rdptr], y = qy[rdptr], d = qd[rdptr], t = qt[rdptr];
		rdptr++;

		// 만일 모서리라면 => 나한테 들어오는 방향으로 수정했으니, 모서리에서 나가는 4방향을 조사해줘야한다.
		if (mymap[x][y] == 2)
		{
			for (int id = 0; id < 4; id++)
			{
				if (poss[id][x + dx[id]][y + dy[id]] != 1) continue; // 갈 수 없는 길이면 안 감
				if (visited[id][x + dx[id]][y + dy[id]] == 1) continue;

				qx[wrptr] = x + dx[id], qy[wrptr] = y + dy[id], qd[wrptr] = id, qt[wrptr] = t + 1; // 돌리는 건 시간 안 넣음 // 이건 가면서 돌리는 거라서 넣어야한다 ㅠㅠㅠ 그 자리 그대로가 아니라 dx[d]로 진행한 거니까!!
				visited[id][x + dx[id]][y + dy[id]] = 1;
				wrptr++;

				// 모서리는 EV 앞이 아니라고 했으니까 체크 안 함
				// 이제 모서리 다음 장소를 가리키도록 수정 체크했으니까 체크해야함!!
				if (x + dx[id] == labs[e][0] && y + dy[id] == labs[e][1] && id == labs[e][2]) return t + 2;
			}
		}

		else
		{
			if (poss[d][x + dx[d]][y + dy[d]] != 1) continue; // 이걸로 깔끔하게 정리

			// 진행 방향 그대로 
			qx[wrptr] = x + dx[d], qy[wrptr] = y + dy[d], qd[wrptr] = d, qt[wrptr] = t + 1;
			visited[d][x + dx[d]][y + dy[d]] = 1;
			wrptr++;

			//printf("x+dx %d y+dy %d t+1 %d\n", x + dx[d], y + dy[d], t + 1);
			if (x + dx[d] == labs[e][0] && y + dy[d] == labs[e][1] && d == labs[e][2]) return t + 2;

		}
	}

}


typedef enum {
	INIT_ORDER,
	ADD_ORDER,
	GET_SP_ORDER,
	FINISH_ORDER
} ORDER;

static void process() {
	int N, order;
	int LabRoomID, startR, startC;
	int height, width, evR, evC;
	int startNum, arrivalNum, userResult;

	scanf("%d", &N);

	initUser(N);
	while (true) {
		scanf("%d", &order);
		if (order == ADD_ORDER) {
			scanf("%d %d %d", &LabRoomID, &startR, &startC);
			scanf("%d %d", &height, &width);
			scanf("%d %d", &evR, &evC);
			makeLabRoom(LabRoomID, startR, startC,
				height, width, evR, evC);
		}
		else if (order == GET_SP_ORDER) {
			scanf("%d %d", &startNum, &arrivalNum);
			userResult = getShortestPath(startNum, arrivalNum);
			printf("%d\n", userResult);
		}
		else if (order == FINISH_ORDER)
			break;
	}

}

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int testCase, tc;

	scanf("%d", &testCase);

	for (tc = 1; tc <= testCase; tc++) {
		process();
	}
	return 0;
}

