#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// ���� 2058 ���� ��ҹ�
// 191106

// Ʋ�ȴ� ��
// - ���� 8x8�̰ھ� �ϰ� for������ 8���� ������ �ߴ���...
// - �ֺ� ���� ���� �ƿ� ���� ���� ���� �� ��� �� ��
// - ���� ���� �����ϸ� 99�� �ٲٰڴٰ� �ߴٰ� visited �ε��� ������ �߰� �� �� ���� ���� ������ üũ ���Ѵ�. 99 �� �� ���Ƽ� �� ��ġ�� �ٲ���� �ٶ���...

// 1�� �õ� ��Ÿ�� ���� -> ť�� ����� �÷����� (���� ���ÿ� �������� ť�� ũ�� �ʿ���)
// 2�� �õ� Ʋ�� => ���̰� ��ҹ� ���� ���ƹ���... (���� �����ߴٰ� ������ �� ��)

/*
���� Ʋ���� ��
6
6 1 4 6
5 3 6 2
0 0 0 0 0 0
0 1 1 1 1 1
0 0 0 1 0 0
0 1 1 1 1 0
0 0 0 0 0 1
0 0 0 0 0 0

// �ִ� �� ĭ�̸� �� �������� �ȴٴ� �Ҹ�?! ... �̰� ������ �ι�° ���̽��� ���� �� ã�ư��� => �׷���
5
1 5 5 5
5 5 1 5
0 0 0 0 0
0 1 1 1 1
0 0 0 1 1
0 1 1 1 1
0 0 0 0 0

// �̰� ���� �����ٰ� ���߸� �� �ȴ�.
// ���� ���� ���� ���� ���ƹ����� �ٶ��� ��ҹ̰� ���� ������.....
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

int loca[2][2]; // ���� ����, �ڴ� xy
int home[2][2];
int town[30][30];
int visited[30][30][30][30]; // ���°� 4�� �����ϱ� 4���� �迭
int dx[9] = { -1, -1, -1, 0, 1, 1, 1, 0, 0 };
int dy[9] = { -1, 0, 1, 1, 1, 0, -1, -1, 0 };
int rdptr = 0, wrptr = 0;

struct queue {
	int loca[2][2];
	int t;
};

struct queue q[1000000];// ����� ������ ����ؾ�����... ��ü �� ũ�� C 2 

int is_available(int mx, int my, int fx, int fy)
{
	if (mx == fx && my == fy) return 0; // �ֺ��� �Ű澲�ٰ� ���� ���� ������ ���� �� ���� �� �ߴ�...

	// m�� 8���⿡ f�� �ִ��� Ȯ��
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
		
		//printf("����!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
		//printf("%d %d %d %d %d\n", cur[0][0], cur[0][1], cur[1][0], cur[1][1], curt);
		//printf("\n");

		// ���� 8���� �� ��
		for (int d1 = 0; d1 < 9; d1++)
		{
			int g = 0;
			next[g][0] = cur[g][0] + dx[d1], next[g][1] = cur[g][1] + dy[d1];
			// ���� �����ߴٰ� ���߸� �� ��!!!!
			//if (cur[g][0] == home[g][0] && cur[g][1] == home[g][1]) next[g][0] = home[g][0], next[g][1] = home[g][1]; // �ؿ��� visited üũ�Ϸ��� ���Ⱑ 99�� �� �� �� 99 ��� ���̳ķ� ����
			if (next[g][0] < 1 || next[g][0] > N || next[g][1] < 1 || next[g][1] > N) continue;
			if (town[next[g][0]][next[g][1]] == 1) continue;
			

			// ��ҹ� 8���� ���鼭
			for (int d2 = 0; d2 < 9; d2++)
			{
				int g = 1;
				next[g][0] = cur[g][0] + dx[d2], next[g][1] = cur[g][1] + dy[d2]; // ���� �Ǽ��ϴ� �� ������...d2��� �� �ϰ� d1�̶�� �س���... ���� ����...
				//if (cur[g][0] == home[g][0] && cur[g][1] == home[g][1]) next[g][0] = home[g][0], next[g][1] = home[g][1]; // �ؿ��� visited üũ�Ϸ��� ���Ⱑ 99�� �� �� ��
				if (next[g][0] < 1 || next[g][0] > N || next[g][1] < 1 || next[g][1] > N) continue;
				if (town[next[g][0]][next[g][1]] == 1) continue;
				if (visited[next[0][0]][next[0][1]][next[1][0]][next[1][1]] == 1) continue;

				//printf("���������\n");
				// ���� ������ ����������, ���� ���� ħ������ �ʴ��� Ȯ���ϰ� �����ϸ� ť�� �ִ´�
				if (is_available(next[0][0], next[0][1], next[1][0], next[1][1]))
				{
					remain = 2; // �̰� �߸� ������ ��찡 �ֳ�?
					
					if (next[0][0] == home[0][0] && next[0][1] == home[0][1]) remain -= 1; //next[0][0] = 99;
					if (next[1][0] == home[1][0] && next[1][1] == home[1][1]) remain -= 1; //next[1][0] = 99;

					q[wrptr].loca[0][0] = next[0][0], q[wrptr].loca[0][1] = next[0][1];
					q[wrptr].loca[1][0] = next[1][0], q[wrptr].loca[1][1] = next[1][1];
					q[wrptr].t = curt + 1;
					wrptr++;

					//if (next[0][0] == 99) { next[0][0] = home[0][0]; remain -= 1; } // �̰� �� �ϸ� �ؿ� visited���� ��������...
					//if (next[1][0] == 99) { next[1][0] = home[1][0]; remain -= 1; }
					
					// ���� üũ
					if (remain == 0) { break; }

					// ���� �� visit üũ
					visited[next[0][0]][next[0][1]][next[1][0]][next[1][1]] = 1; // 99�� �����Ϸ��� �ϴ� ������ ����...�� 
					
					// ������ ���°�
					// printf("8�� ������ %d %d %d %d\n", next[0][0], next[0][1], next[1][0], next[1][1]);

				}
			}
			if (remain == 0) { break; }
		}
		if (remain == 0) { ans = curt + 1; break; }
	}

	printf("%d\n", ans);
	return 0;

}