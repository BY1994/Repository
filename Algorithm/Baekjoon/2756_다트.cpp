/*
2756 ��Ʈ 

������ 
(�� ������) 

x, y ��ǥ�� double �� �������� �ʰ� int �� �����ߴ���
���� 0 ���� �޾����� ������ �־���

scanf �ȿ� \n �� �־����� �������� ���� �� �� �� �Է� �� �ϸ�
������� �ʴ� ������ �־��� 
*/

#include <stdio.h>
 
double radius[5] = {9.0, 36.0, 81.0, 144.0, 225.0};
int score[5] = {100, 80, 60, 40, 20};

int main(void)
{
	int tc;
	double x, y, cur_radius;
	scanf("%d", &tc);
	while (tc--) {
		int player[2] = {0, };
		for (int p = 0; p < 2; p++) {
			for (int turn = 0; turn < 3; turn++) {
				scanf("%lf %lf", &x, &y);
				cur_radius = x*x + y*y;
				for (int s = 0; s < 5; s++) {
					if (cur_radius <= radius[s]) {
						player[p] += score[s];
						break;
					}
				}
			}
		}
		printf("SCORE: %d to %d, ", player[0], player[1]);
		if (player[0] < player[1]) {
			printf("PLAYER 2 WINS.\n");
		} else if (player[0] > player[1]) {
			printf("PLAYER 1 WINS.\n");
		} else {
			printf("TIE.\n");
		}
	}

	return 0;
} 
