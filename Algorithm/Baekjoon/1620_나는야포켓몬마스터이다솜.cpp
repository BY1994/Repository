/*
1620 포켓몬 마스터 이다솜 

hash table
백준에 index 라는 이름 쓰면 컴파일 에러 남
*/

#include <stdio.h>
#include <string.h>

#define MAX_KEY 21
#define MAX_DATA 1
#define MAX_TABLE 300003

char ind2name[100001][21];

typedef struct
{
	char key[MAX_KEY + 1];
	int data[MAX_DATA + 1];
}Hash;
Hash name2ind[MAX_TABLE];

unsigned long hash(const char *str)
{
	unsigned long hash = 5381;
	int c;

	while (c = *str++)
	{
		hash = (((hash << 5) + hash) + c) % MAX_TABLE;
	}

	return hash % MAX_TABLE;
}

int find(const char *key)
{
	unsigned long h = hash(key);
	int cnt = MAX_TABLE;

	while (name2ind[h].key[0] != 0 && cnt--)
	{
		if (strcmp(name2ind[h].key, key) == 0)
		{
			return name2ind[h].data[0];
		}
		h = (h + 1) % MAX_TABLE;
	}
	return 0;
}

int add(const char *key, int data)
{
	unsigned long h = hash(key);
	while (name2ind[h].key[0] != 0)
	{
		if (strcmp(name2ind[h].key, key) == 0)
		{
			return 0;
		}

		h = (h + 1) % MAX_TABLE;
	}
	strcpy(name2ind[h].key, key);
	name2ind[h].data[0] = data;
	return 1;
}

int main(int argc, char* argv[])
{
	int N, M;
	scanf("%d %d", &N, &M);
	
	for (int i = 1; i <= N; ++i) {
		scanf("%s", ind2name[i]);
		getchar();
		add(ind2name[i], i);
	}

	for (int i = 0; i < M; ++i) {
		char question[21] = {0,};
		scanf("%s", question);
		getchar();
		if (question[0] < 'A') {
			int cur = 0;
			for (int j = 0; question[j]; ++j) {
				cur *= 10;
				cur += question[j] - '0';
			}
			printf("%s\n", ind2name[cur]);
		} else {
			printf("%d\n", find(question));
		}
	}

	return 0;
}
