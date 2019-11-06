#define _CRT_SECURE_NO_WARNINGS
// ���� 3108 ������ ��
// 19.11.05

/// *** main.cpp ***
#include <stdio.h>
#include <ctime>
#include <chrono>
#include <random>
#define MAXN 1000000

using namespace std;

static int orgArr[MAXN], removeArr[MAXN], answer[1000], userAns[1000];
static int nCount, userCount;
static int orgCount, removeCount, answerCount;
static void SWAP(int &x, int &y) { int z = x; x = y; y = z; }

extern int card_find(int userAns[]);

auto seed = chrono::system_clock::now().time_since_epoch().count();
mt19937 mt(seed);

static int getRand() {
	int s = 0, e = 1 << 21;
	uniform_int_distribution<int> range(s, e);
	return range(mt);
}

int getNumber(int dir, int num) {
	nCount++;
	if (num < 0 || num >= MAXN) return 0;
	if (dir == 1) return orgArr[num];
	else if (dir == 2) return removeArr[num];
	else return 0;
}

static void input() {
	scanf("%d %d", &orgCount, &removeCount);
	int i;
	for (i = 0; i < orgCount; ++i) scanf("%d", orgArr + i);
	for (i = 0; i < removeCount; ++i) scanf("%d", removeArr + i);
	answerCount = orgCount - removeCount;
	for (i = 0; i < answerCount; ++i) scanf("%d", answer + i);
}

static void init(int t) {
	int i, j, k, delno;
	nCount = 0;
	orgCount = getRand() % 100000 + 100000 * (t + 1);
	answerCount = getRand() % 100 + 100 * (t + 1);
	//orgCount = 100; //
	//answerCount = 10;
	if (orgCount > MAXN) orgCount = MAXN;
	if (answerCount > 1000) answerCount = 1000;
	removeCount = orgCount - answerCount;

	for (i = 0; i < MAXN; i++) orgArr[i] = removeArr[i] = 0;
	for (i = 0; i < 1000; i++) userAns[i] = answer[i] = 0;
	for (i = 0; i < orgCount; i++) orgArr[i] = i + 1;
	for (i = 0; i < orgCount; i++) {
		SWAP(orgArr[i], orgArr[getRand() % orgCount]);
	}
	for (i = 0; i < orgCount; i++) removeArr[i] = orgArr[i];

	for (i = 0; i < answerCount; i++) {
		do {
			delno = getRand() % orgCount;
		} while (removeArr[delno] == 0);
		removeArr[delno] = 0;
	}
	for (i = j = k = 0; i < orgCount; i++) {
		if (removeArr[i]) {
			removeArr[i] = 0;
			removeArr[j++] = orgArr[i];
		}
		else answer[k++] = orgArr[i];
	}
}

static int check() {
	//printf("���� %d \n", answerCount);
	if (answerCount != userCount)
		return MAXN;
	for (int i = 0; i < answerCount; i++) {
		//printf("%d ", answer[i]);
		if (answer[i] != userAns[i])
			return MAXN;
	}
	return nCount;
}

///**** use_code : template *****

//extern int getNumber(int, int);
int cards1[1000000]; // card1�� �����Ϸ��� ������ �׷��� ��� ���ٰ� e+my_ans�� ������ ������ 0�� ����Ű�� ���� �߻�....���� �� �����µ� ���� �� �ȴ�...
int cards2[1000000];
int my_ans = 0;

void find_answer(int s, int e, int user_ans[])
{
	if (s > e) return;
	else if (s == e)
	{
		// �ϳ��� ���� ���� üũ�ؾ��� �޶� ���� �ű� ������
		int card1 = (cards1[s+my_ans] != -1) ? cards1[s+my_ans] : getNumber(1, s+my_ans);
		cards1[s+my_ans] = card1;
		int card2 = (cards2[s] != -1) ? cards2[s] : getNumber(2, s);
		cards2[s] = card2; // Ȥ�� ������Ʈ �Ǿ����� �𸣴ϱ� �־���

		// card1�� ���� ������ ã�ư���
		while (card1 != card2)
		{
			user_ans[my_ans] = card1;
			//printf("user_ans\n");
			//for (int i = 0; i<=my_ans; i++) printf("%d ", user_ans[i]);
			//printf("\n");
			my_ans++;
			card1 = getNumber(1, s + my_ans);
			// cards[s + my_ans] = card1;
			//for (int i = 0; i <= 100 + 2; i++) printf("%d ", cards[i]);
			//printf("\n");
		}
		return;
	}
	else
	{
		// e���� üũ�ؼ� ���̰� ������ ��� ��
		//printf("������ e %d (%d)\n", e, cards[e]);
		int card1 = (cards1[e+my_ans] != -1) ? cards1[e+my_ans] : getNumber(1, e + my_ans);
		cards1[e+my_ans] = card1;
		int card2 = (cards2[e] != -1) ? cards2[e] : getNumber(2, e);
		cards2[e] = card2;

		if (card1 != card2)
		{
			find_answer(s, (s + e) / 2, user_ans);
			find_answer((s + e) / 2 + 1, e, user_ans);
		}
		return;
	}
}
int card_find(int user_ans[]) {
	my_ans = 0;
	for (int i = 0; i < 1000000; i++) { cards1[i] = -1; cards2[i] = -1; }
	// card1�� ���鼭 0 ������ ã��
	int s = 0, e = 1000000;
	int sol;
	while (s <= e)
	{
		int m = (s + e) / 2;
		int card2 = getNumber(2, m);
		cards2[m] = card2;
		if (card2 == 0) { sol = m;  e = m - 1; } // ���� �������� 0�̾��� �� ����
		else s = m + 1;
	}

	//printf("���������? %d\n", sol);
	//for (int i = 0; i <= sol + 2; i++) printf("%d ", cards[i]);
	//printf("\n");
	// e ������ ���� sol����..
	// ��� ���鼭 ���� ���� �ٸ��� �� �ڸ���
	find_answer(0, sol-1, user_ans); // 0�� ����Ű�� �� �� 0�̶� �������� �� �ִ�...

	return my_ans;
}

int main(void) {

	int testCase;

#if 0  /// 1:file_IO or 0:ramdom generate

	freopen("input.txt", "r", stdin);
	scanf("%d", &testCase);
	for (int tc = 1; tc <= testCase; tc++) {
		input();
		userCount = card_find(userAns);
		nCount = check();
		printf("#%d : %d\n", tc, nCount);
		if (nCount == MAXN) break;
	}

#else

	testCase = 100;
	for (int tc = 1; tc <= testCase; tc++) {
		init(tc);
		//for (int i = 0; i < 100; i++) printf("%d ", orgArr[i]);
		//printf("\n");
		//for (int i = 0; i < 100; i++) printf("%d ", removeArr[i]);
		//printf("\n");
		userCount = card_find(userAns);
		nCount = check();
		printf("#%d : %d\n", tc, nCount);
		if (nCount == MAXN) break;
	}

#endif

	return 0;
}