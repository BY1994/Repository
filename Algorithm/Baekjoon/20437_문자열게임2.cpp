#include <stdio.h>

char W[10010];
int idx[26][10010];

int main(void)
{
    int T, K;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int min = 10001;
        int max = 0;

        scanf("%s", W);
        scanf("%d", &K);

        for (int i = 0; i < 26; i++)
        	idx[i][0] = 0;

		for (int i = 0; W[i]; i++) {
			int val = W[i]-'a';
			idx[val][0] += 1;
			idx[val][idx[val][0]] = i;
			
			//printf("[%d](%d)=%d\n", idx[val][0], idx[val][idx[val][0]]);
		}
		
		for (int i = 0; i < 26; i++) {
			if (idx[i][0] < K) continue;
			for (int j = 1; j <= idx[i][0]+1 - K; j++) {
				int dist = idx[i][j+K-1] - idx[i][j]+1;
				if (min > dist) min = dist;
				if (max < dist) max = dist;
				//printf("dist %d - %d min %d max %d\n", idx[i][j+K-1], idx[i][j])
			}
		}

        if (max == 0) {
            printf("-1\n");
        } else{
            printf("%d %d\n", min, max);
        }
    }
    return 0;
}


# 아래는 한 13% 정도에서 시간초과 나는 코드
#if 0
#include <stdio.h>
char W[10010];

int main(void)
{
    int T, K;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int min = 10001;
        int max = 0;
        int cur = 0;
        //char alpha[27] = {0,};

        scanf("%s", W);
        scanf("%d", &K);

        for (int p1 = 0; W[p1]; p1++) {
            int alpha = 0;
            for (int p2 = p1; W[p2]; p2++) {
                if (W[p2] == W[p1]) alpha++;
                if (alpha == K) {
                    int dist = p2-p1+1;
                    if (min > dist) min = dist;
                    if (max < dist) max = dist;
                    break;
                }
                //alpha[W[p1]-'a'] += 1
            }
        }
        if (max == 0) {
            printf("-1\n");
        } else{
            printf("%d %d\n", min, max);
        }
    }
    return 0;
}
#endif
