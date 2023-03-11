/*
1333 ������ ��ȭ 

�ùķ��̼�

��Ÿ�� ��ġ�ϱ⳪ ���� �ɱ� ���� ���� 

�ùķ��̼� ���� ������ Ǯ�̴� �Ұ������� �ñ��ϴ�. 

������ �����ε� �ڵ�� ��Ȯ�ϰ� ������ ���� ��ٷο���.
�����ϸ鼭 �ణ�� �Ǽ��� break ������ ����������,
break �ƴ� ��� ������ �� Ŀ���ؾ��ϴµ�,
>= �� �ƴ� > �� �߸� ���� �ٶ��� � if �� �ɸ��� �ʾƼ�
���� ������ �������ȴ�. 
*/

#include <stdio.h>

int main(void) {
	int N, L, D;
	int song, call, end; 
	scanf("%d %d %d", &N, &L, &D);
	song = L;
	call = 0;
	end = N * L + (N-1) * 5;
	while (call < end) {
		if (song <= call && call < song + 5) break;
		if (call < song) call += D;
		if (call >= song + 5) song += 5 + L;
		//if (call >= song + 5 && song < end) song += 5 + L; // song < end ��� while �������� Ŀ���� 
	}
	printf("%d\n", call);
	return 0;
}

// ���ڵ�
// https://www.acmicpc.net/source/3334125
#if 0
i;main(N,L,D){scanf("%d%d%d",&N,&L,&D);for(N*=L+5;i<N&&i%(L+5)<L;i+=D);printf("%d",i);}
#endif 
