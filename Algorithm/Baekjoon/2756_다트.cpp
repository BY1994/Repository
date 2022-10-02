/*
2756 다트 

기하학 
(원 반지름) 

x, y 좌표를 double 로 선언하지 않고 int 로 선언했더니
값이 0 으로 받아지는 문제가 있었음

scanf 안에 \n 을 넣었더니 마지막에 값을 한 번 더 입력 안 하면
종료되지 않는 문제가 있었음 
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
