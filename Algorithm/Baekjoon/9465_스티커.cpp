/*
9465 스티커 

DP
- DP 배열을 100000 만큼 선언할 필요가 없음
앞에 2칸만 보면 되기 때문에 2칸 씩만 가지고 있어도 됨 
- 속도를 높이기 위해서는 scanf 대신 직접 read 해야한다. 
*/

#include <stdio.h>
#define max(a, b) (((a) > (b))?(a):(b))
int dp[100001][2];
int sticker[100001][2];

int main(void) {
	int T, n;
	scanf("%d", &T);
	while (T--) {
		int ans = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &sticker[i][0]);
		for (int i = 0; i < n; ++i)
			scanf("%d", &sticker[i][1]);
		
		dp[0][0] = sticker[0][0];
		dp[0][1] = sticker[0][1];
		dp[1][0] = dp[0][1] + sticker[1][0];
		dp[1][1] = dp[0][0] + sticker[1][1];
	
		for (int i = 2; i < n; ++i) {
			dp[i][0] = max(dp[i-1][1], dp[i-2][1]) + sticker[i][0];
			dp[i][1] = max(dp[i-1][0], dp[i-2][0]) + sticker[i][1];
		}
		printf("%d\n", max(dp[n-1][0], dp[n-1][1]));
	}
	return 0;
}

// https://www.acmicpc.net/source/8666869
#if 0
#include <unistd.h>
#include <cstdio>
#define N 100000
namespace io
{
	const int is = 1024 * 72, os = 1024 * 2;
	char ib[is], *ip = ib;
	char ob[os + 16], *op = ob;

	inline char get()
	{
		if(ib + is == ip) syscall(0, 0, ip = ib, is);
		return *ip;
	}

	inline int scan()
	{
		int n = 0;
		while(get() <= ' ') ip++;
		while(get() >= '0') n = (n * 10) + (*ip++ & 15);
		return n;
	}

	inline void flush() { syscall(1, 1, op = ob, op - ob); }
	struct f { ~f() { flush(); } } flusher;

	inline void print(int n)
	{
		char temp[16], *t = temp;
		do *t++ = n % 10 | 48; while(n /= 10);
		do *op++ = *--t; while(t != temp);
		*op++ = '\n';
		if(op >= ob + os) flush();
	}
}
inline int max(int x, int y) { return x > y ? x : y; }
using namespace io;

int main() {
	char *a = new char[N];
	int t = scan();
	while(t--) {
		int n = scan();
		for(int i = 0; i < n; i++)
			a[i] = scan();
		int d[2][2] = {{0, a[0]}, {0, scan()}}, t1, t2;
		for(int i = 1; i < n; i++) {
			t1 = max(d[0][0], d[0][1]);
			t2 = max(d[1][0], d[1][1]);
			d[0][0] = d[0][1];
			d[0][1] = t2 + a[i];
			d[1][0] = d[1][1];
			d[1][1] = t1 + scan();
		}
		print(max(d[0][1], d[1][1]));
	}
}
#endif

// https://www.acmicpc.net/source/3939483
#if 0
#include <cstdio>

char buf[0x40000], line[100000];
int  idx, bytes;

inline int max(int x, int y) { return x > y ? x : y; }
inline static int read() {
	if (!(idx - bytes)) {
		bytes = fread(buf, sizeof(char), sizeof(buf), stdin);
		idx = 0;
	}
	return buf[idx++];
}
inline static int parse() {
	int ret = 0,
		num = read();

	while (num - 0x0A && num - 0x20) {
		ret = ret*10 + (num & 0x0F);
		num = read();
	}
	return ret;
}

int main() {
	int testCase;
	scanf("%d", &testCase), read();

	while (testCase--) {
		int n		 = parse(),
			dp[2][3] = { 0, };

		for (int i = 0; i < n; i++)
			line[i] = parse();
		for (int i = 0; i < n; i++) {
			dp[0][2] = max(max(dp[1][0], dp[1][1]), dp[0][0]) + line[i];
			dp[1][2] = max(max(dp[0][0], dp[0][1]), dp[1][0]) + parse();

			for (int j = 0; j < 2; j++)
				dp[0][j] = dp[0][j + 1], dp[1][j] = dp[1][j + 1];
		}
		printf("%d\n", max(dp[0][2], dp[1][2]));
	}
}
#endif

// https://www.acmicpc.net/source/52563281
#if 0
#include <cstdio>
#include <algorithm>

char rbuf[1<<17];
int idx, ridx;

inline char read(){
    if(ridx == idx){
        ridx = fread(rbuf, 1, 1<<17, stdin);
        if(!ridx) return 0;
        idx = 0;
    }
    return rbuf[idx++];
}

inline int readInt(){
    int sum = 0;
    char now = read();
    
    while(now <= 32) now = read();
    while(now >= 48) sum = sum * 10 + now - '0', now = read();
    
    return sum;
}

int main(void) {
    int T = readInt(), n, dp[100000][2];
    while (T--) {
        n = readInt();
        for (int i = 0; i < n; i++) dp[i][0] = readInt();
        for (int i = 0; i < n; i++) dp[i][1] = readInt();
        if (n == 1) {
            printf("%d\n", dp[0][0] > dp[0][1] ? dp[0][0] : dp[0][1]);
            continue;
        }
        dp[1][0] += dp[0][1], dp[1][1] += dp[0][0];

        for (int i = 2; i < n; i++) {
            dp[i][0] += std::max({ dp[i - 1][1], dp[i - 2][0], dp[i - 2][1] });
            dp[i][1] += std::max({ dp[i - 1][0], dp[i - 2][0], dp[i - 2][1] });
        }

        printf("%d\n", std::max({ dp[n - 1][0], dp[n - 1][1], dp[n - 2][1], dp[n - 2][0] }));
    }
}
#endif
