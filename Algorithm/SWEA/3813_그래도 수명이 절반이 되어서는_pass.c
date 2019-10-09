#include <stdio.h>
/*
3813 �׷��� ������ ������ �Ǿ��

2019.10.4 PBY
*/

// '�Ϻ� �����͸� ������ �̵��Ͻʽÿ�' -> ���������� ����
int blocks[200000];
int data[200000];

int main(void)
{
	int test_case;
	int T;

	int N, K;
	int i;
	int min;
	int max;
	int mid;
	int ans = 0;
	int cum_ind;
	int data_ind;

	setbuf(stdout, NULL);
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		min = 0;
		max = 0;
		scanf("%d %d", &N, &K);
		for (i = 0; i < N; i++) {
			scanf("%d", blocks+i);
			// max �� �̸� ã�Ƴ��� (�̺�Ž�� ������ �Ϸ���)
			if (max < blocks[i]) max = blocks[i];
		}
		
		for (i = 0; i < K; i++) {
			scanf("%d", data + i);
		}
		
		// �̺�Ž��
		while (min <= max)
		{
			mid = (min + max) / 2;

			// ���ɿ��� Ȯ��
			cum_ind = 0;
			data_ind = 0;
			for (i = 0; i < N; i++) {
				if (blocks[i] <= mid) cum_ind++;
				else cum_ind = 0;
				if (cum_ind >= data[data_ind]) {
					cum_ind = 0;
					data_ind++;
				}
			}

			if (data_ind < K) {
				// ���н�
				min = mid + 1;
			}
			else {
				ans = mid;
				max = mid - 1;
			}
		}

		printf("#%d %d\n", test_case, ans);
	}
	return 0; //��������� �ݵ�� 0�� �����ؾ� �մϴ�.
}
