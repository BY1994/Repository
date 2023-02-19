/*
1296 팀 이름 정하기 

mystrcmp 를 잘못 짜서 2번 틀림
이름 하나가 더 짧은 경우 (NULL 만난 경우)까지 고려해야하는데
그런 경우 그냥 종료해버려서 답을 잘못 찾음 

구현, 문자열 
*/

#include <stdio.h>

char myname[21];
char teamname[51][21];
int count[128];
int max_score = -1;
int max_ind;
int N; 

int get_score(char *name) {
	long long L, O, V, E, score;
	L = count['L'];
	O = count['O'];
	V = count['V'];
	E = count['E'];

	for (int i = 0; name[i]; ++i) {
		if (name[i] == 'L') L++;
		else if (name[i] == 'O') O++;
		else if (name[i] == 'V') V++;
		else if (name[i] == 'E') E++;
	}

	score = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100LL;

	return score;
}

int mystrcmp(char *name1, char *name2) {
	for (int j = 0; name1[j] || name2[j]; ++j) {
		if (name1[j] > name2[j]) return 1;
		else if (name1[j] < name2[j]) return -1;
	}
	return 0;
}

int main(void) 
{
	scanf("%s", myname);
	for (int i = 0; myname[i]; ++i) {
		if (myname[i] == 'L' || myname[i] == 'O' || \
		myname[i] == 'V' || myname[i] == 'E') count[myname[i]] += 1;
	}
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%s", teamname[i]);
		int cur_score = get_score(teamname[i]);
		//printf("cur_score: %d\n", cur_score);
		if (max_score < cur_score) {
			max_score = cur_score;
			max_ind = i;
		} else if (max_score == cur_score) {
			// dictionary order
			int ret = mystrcmp(teamname[i], teamname[max_ind]);
			if (ret < 0) max_ind = i;
		}
	}
	printf("%s\n", teamname[max_ind]);
	return 0;
}
