#include <stdio.h>

/*
틀린 부분
1 0 들어왔는데 1 이 아니고 0이 나왔다
10 0 들어왔을 때 10이어야하는데 위에서 처리한 거 무조건 1 하게 해서 1 나왔다;;

student[a-1] 을 넣어야하는데 a-1을 넣었다... 처음 초기화했을 때 부모 값만 생각하고 이후에 그 값이 변했을 거란 생각을 못했나보다
		if (student[a - 1] < student[b - 1]) student[b - 1] = a - 1;
		else student[a - 1] = b - 1;

유니온 파인드 로직에서 무조건 합친 거중 작은 거를 따라가도록 짜버렸는데
재귀함수를 넣었어야했다....ㅠ
        if (visited[student[a - 1]] == 0) cnt++;
        visited[student[a - 1]] = 1;
? 그냥 어차피 종교 세는 거니까 전체 다 다른 종교라고 생각하고 합쳐질 때마다 넣으면 되는 거 아닌가?
=> 아님! 부모가 달라야만 의미가 있음! 유니온 파인드의 문제 함정은 거기 넣을 것!

합쳐지는 과정에서 비대칭적으로 넣어도 문제 없을 거라 생각했는데,
		if (parenta < parentb) student[b - 1] = parenta;
		else student[a - 1] = parentb;
생각해보니 반례가 있었다.
7 5
3 4
5 6
5 7
4 6
4 5
3
둘이 같은 그룹이지만 대장이 아니라 중간친구를 합치면 대장은 합쳐진 줄 모른다는 거...
대장을 업데이트 해야한다!
(혹은 마지막을 4 7로 했을 때도...)
*/

int N, M, a, b;
int student[50001];
int visited[50001];
int cnt;


int findParent(int a)
{
	if (student[a] == a) return a; // 자기자신 만나면 부모임
	return findParent(student[a]); // 자기자신 못 만나는 경우는 없나? 
}

/*
void unionParent(int a, int b)
{
	int parentA = findParent(a);
	int parentB = findParent(b);

	if (parentA < parentB) student[b] = parentA;
	else student[a] = parentB;
}
*/

int main()
{
	scanf("%d %d", &N, &M);

	cnt = N;

	for (int i = 0; i < 50001; i++)
	{
		student[i] = i; // 부모를 자기자신으로
	}

	for (int i = 0; i < M; i++)
	{
		scanf("%d %d", &a, &b);
		//unionParent(a - 1, b - 1);
		//if (visited[a - 1] || visited[b - 1]) cnt -= 1; // 합쳐지면 대통합!
		
		// 가장 상위 부모에 더해지고 자기꺼는 0개
		int parenta = findParent(student[a - 1]);
		int parentb = findParent(student[b - 1]);
		//if (findParent(student[a - 1]) != findParent(student[b - 1])) cnt -= 1; // 부모가 달라야 합치는 거지
		if (parenta != parentb) cnt -= 1;

		//if (student[a - 1] < student[b - 1]) student[b - 1] = student[a - 1];
		//else student[a - 1] = student[b - 1];

		if (parenta < parentb)
		{
			student[b - 1] = parenta;
			//student[a - 1] = parenta; // 이거 지워도 통과하는지?
			student[parentb] = parenta; // 우두머리의 변화가 중요한 것!!
		}
		else
		{
			student[a - 1] = parentb;
			//student[b - 1] = parentb; // 이거 지워도 통과하는지?
			student[parenta] = parentb;
		}

		//visited[a - 1] = 1;
		//visited[b - 1] = 1;
	}

	//if (cnt == 0) cnt = N; // 학생이 1명 뿐인 경우 종교는 1개 => 근데 이걸 확장해야함. 학생 N명이면 N개 종교임

	printf("%d\n", cnt);

	return 0;
}