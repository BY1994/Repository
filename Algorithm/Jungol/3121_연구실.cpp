
///=============== main.cpp ===============

#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <stdio.h>


/*
�⺻ ��ǲ
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

Ʋ���� ���̽� => ������ ���⸸ ����Ű���� �����ϰ� ����
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

Ʋ���� ���̽� 2 => ��üũ ������ if id�ε� if d�� �״�� �����־��� (������ ����)
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

// �𼭸����� �𼭸� �پ�ٴ�
// �׷��� Ǯ�� �� ��. �űⰡ ������ �����ٴϴ� EV ���̾�߸� �Ű�Ÿ�� ���̴�.

// Ʋ�� ���� (�ݷ�) -> ������ �������� �̰Ű� �����ϴ� üũ�ؾ� �� �ݷʸ� ���� �� �ִ� (���� ���� �װ� üũ�� �Ŵϱ�)
// �׳� ������ �� ������ �� �� �����ϴ� �ع����� �갡 �𼭸����� ������� �̻��� �������� Ƣ�����
// �ܺ��� ���� ���°� �ƴ϶� �𼭸����� �� �𼭸��� �����ع���

int mymap[51][51];
int poss[4][51][51]; // �� �������� �������� üũ // ������ ���� 1�� üũ�� ��
int N;
int labs[1001][3]; // ������ ev
int visited[4][51][51];
int qx[100000];
int qy[100000];
int qd[100000];
int qt[100000];
int wrptr, rdptr;

int dx[4] = { 0, 0, 1, -1 }; // �������� ������⺰ ���� ��ġ
int dy[4] = { 1, -1, 0, 0 };


///=============== user.cpp ===============
void initUser(int tableSize) {
	// ���ɸ��� �ʱ�ȭ������ϴ� �ֵ�
	N = tableSize;
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= N; j++) mymap[i][j] = 0;

	for (int k = 0; k < 4; k++)
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++) poss[k][i][j] = 0;
}

void makeLabRoom(int id, int sr, int sc, int h, int w, int vr, int vc) {

	// 2���� �ʿ� ������ ǥ�� 1, �𼭸� ǥ�� 2 EV ��ġ ǥ�� x
	for (int i = sr; i < sr + h; i++)
		for (int j = sc; j < sc + w; j++) mymap[i][j] = 1; // ���� ������

	// �𼭸� �ε���
	mymap[sr - 1][sc - 1] = 2, mymap[sr-1][sc+w] = 2, mymap[sr+h][sc-1] = 2, mymap[sr+h][sc+w] = 2;
	
	// EV ��ġ�� �ʿ��� ����, ���� ������ �Ʒ��� ����� �ľ��ϱ�
	if (vr == sr + h - 1) labs[id][2] = 1, labs[id][0] = vr+1, labs[id][1] = vc; // ��
	else if (vr == sr) labs[id][2] = 0, labs[id][0] = vr-1, labs[id][1] = vc; //��
	else if (vc == sc) labs[id][2] = 3, labs[id][0] = vr, labs[id][1] = vc-1; // ��
	else labs[id][2] = 2, labs[id][0] = vr, labs[id][1] = vc+1; // ��-> ��ġ�� ������

	// �� ������ ����� ���� ����
	// EV ��ġ�� ������ ���� �α�

	// �� �� �ִ� ���� �̸� üũ�صα� => simple! �ش��� ����!
	// ���� �ݷ���� ���� ������ �ʿ��ϴ� => ���� �� �� �����̾�� �����ϴٷ� ����! (���� ����Ű�� ���� ȭ��ǥ)
	// ���ʿ� �ִ� �� (�������� �̵�) sc-1~sc+w-1 & ���ʿ� �ִ� �� (�������� �̵�) sc~sc+w
	for (int j = sc - 1; j <= sc + w-1; j++) poss[1][sr + h][j] = 1;
	for (int j = sc; j <= sc + w; j++) poss[0][sr - 1][j] = 1;
	//  ���ʿ� �ִ� �� (�������� �̵�) sr-1~sr+h-1& ���ʿ� �ִ� �� (�������� �̵�) sr~sr+h
	for (int i = sr - 1; i <= sr + h-1; i++) poss[3][i][sc - 1] = 1;
	for (int i = sr; i <= sr + h; i++) poss[2][i][sc + w] = 1;

	// for (int i = sr - 1; i <= sr + h; i++) poss[3][i][sc - 1] = 1, poss[2][i][sc + w] = 1; // ���� �� ���
}

int getShortestPath(int s, int e) {
	// �ش� ��ġ���� bfs�� ���鼭 �������� ���� ���� ����.... (�̻��� �������� ���� �ִ� ��Ʈ�� ���ϳ�...)
	for (int k = 0; k < 4; k++)
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++) visited[k][i][j] = 0;

	// �ʱ�ȭ
	rdptr = wrptr = 0;
	qx[wrptr] = labs[s][0], qy[wrptr] = labs[s][1], qd[wrptr] = labs[s][2], qt[wrptr] = 1; // ó���� 1��
	visited[qd[wrptr]][qx[wrptr]][qy[wrptr]] = 1; // �� ��ġ �湮�� ��!
	wrptr++;

	while (rdptr < wrptr)
	{
		int x = qx[rdptr], y = qy[rdptr], d = qd[rdptr], t = qt[rdptr];
		rdptr++;

		// ���� �𼭸���� => ������ ������ �������� ����������, �𼭸����� ������ 4������ ����������Ѵ�.
		if (mymap[x][y] == 2)
		{
			for (int id = 0; id < 4; id++)
			{
				if (poss[id][x + dx[id]][y + dy[id]] != 1) continue; // �� �� ���� ���̸� �� ��
				if (visited[id][x + dx[id]][y + dy[id]] == 1) continue;

				qx[wrptr] = x + dx[id], qy[wrptr] = y + dy[id], qd[wrptr] = id, qt[wrptr] = t + 1; // ������ �� �ð� �� ���� // �̰� ���鼭 ������ �Ŷ� �־���Ѵ� �ФФ� �� �ڸ� �״�ΰ� �ƴ϶� dx[d]�� ������ �Ŵϱ�!!
				visited[id][x + dx[id]][y + dy[id]] = 1;
				wrptr++;

				// �𼭸��� EV ���� �ƴ϶�� �����ϱ� üũ �� ��
				// ���� �𼭸� ���� ��Ҹ� ����Ű���� ���� üũ�����ϱ� üũ�ؾ���!!
				if (x + dx[id] == labs[e][0] && y + dy[id] == labs[e][1] && id == labs[e][2]) return t + 2;
			}
		}

		else
		{
			if (poss[d][x + dx[d]][y + dy[d]] != 1) continue; // �̰ɷ� ����ϰ� ����

			// ���� ���� �״�� 
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

