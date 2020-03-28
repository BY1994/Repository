#include <stdio.h>

/*
Ʋ�� �κ�
1 0 ���Դµ� 1 �� �ƴϰ� 0�� ���Դ�
10 0 ������ �� 10�̾���ϴµ� ������ ó���� �� ������ 1 �ϰ� �ؼ� 1 ���Դ�;;

student[a-1] �� �־���ϴµ� a-1�� �־���... ó�� �ʱ�ȭ���� �� �θ� ���� �����ϰ� ���Ŀ� �� ���� ������ �Ŷ� ������ ���߳�����
		if (student[a - 1] < student[b - 1]) student[b - 1] = a - 1;
		else student[a - 1] = b - 1;

���Ͽ� ���ε� �������� ������ ��ģ ���� ���� �Ÿ� ���󰡵��� ¥���ȴµ�
����Լ��� �־�����ߴ�....��
        if (visited[student[a - 1]] == 0) cnt++;
        visited[student[a - 1]] = 1;
? �׳� ������ ���� ���� �Ŵϱ� ��ü �� �ٸ� ������� �����ϰ� ������ ������ ������ �Ǵ� �� �ƴѰ�?
=> �ƴ�! �θ� �޶�߸� �ǹ̰� ����! ���Ͽ� ���ε��� ���� ������ �ű� ���� ��!

�������� �������� ���Ī������ �־ ���� ���� �Ŷ� �����ߴµ�,
		if (parenta < parentb) student[b - 1] = parenta;
		else student[a - 1] = parentb;
�����غ��� �ݷʰ� �־���.
7 5
3 4
5 6
5 7
4 6
4 5
3
���� ���� �׷������� ������ �ƴ϶� �߰�ģ���� ��ġ�� ������ ������ �� �𸥴ٴ� ��...
������ ������Ʈ �ؾ��Ѵ�!
(Ȥ�� �������� 4 7�� ���� ����...)
*/

int N, M, a, b;
int student[50001];
int visited[50001];
int cnt;


int findParent(int a)
{
	if (student[a] == a) return a; // �ڱ��ڽ� ������ �θ���
	return findParent(student[a]); // �ڱ��ڽ� �� ������ ���� ����? 
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
		student[i] = i; // �θ� �ڱ��ڽ�����
	}

	for (int i = 0; i < M; i++)
	{
		scanf("%d %d", &a, &b);
		//unionParent(a - 1, b - 1);
		//if (visited[a - 1] || visited[b - 1]) cnt -= 1; // �������� ������!
		
		// ���� ���� �θ� �������� �ڱⲨ�� 0��
		int parenta = findParent(student[a - 1]);
		int parentb = findParent(student[b - 1]);
		//if (findParent(student[a - 1]) != findParent(student[b - 1])) cnt -= 1; // �θ� �޶�� ��ġ�� ����
		if (parenta != parentb) cnt -= 1;

		//if (student[a - 1] < student[b - 1]) student[b - 1] = student[a - 1];
		//else student[a - 1] = student[b - 1];

		if (parenta < parentb)
		{
			student[b - 1] = parenta;
			//student[a - 1] = parenta; // �̰� ������ ����ϴ���?
			student[parentb] = parenta; // ��θӸ��� ��ȭ�� �߿��� ��!!
		}
		else
		{
			student[a - 1] = parentb;
			//student[b - 1] = parentb; // �̰� ������ ����ϴ���?
			student[parenta] = parentb;
		}

		//visited[a - 1] = 1;
		//visited[b - 1] = 1;
	}

	//if (cnt == 0) cnt = N; // �л��� 1�� ���� ��� ������ 1�� => �ٵ� �̰� Ȯ���ؾ���. �л� N���̸� N�� ������

	printf("%d\n", cnt);

	return 0;
}