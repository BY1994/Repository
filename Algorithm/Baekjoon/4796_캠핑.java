/*
4796 캠핑

greedy
그리디 보다는 단순 수학문제인 것 같다.

문제를 풀다가 깨달은 java 문법에서 주의할 점
while(1) 은 안 된다.
if (L || P || V) 는 안 된다.
true / false 가 나오도록 해야한다.

Math 사용법 (min, max)
import 할 필요 없음
https://mine-it-record.tistory.com/140

문제 해석의 여지
https://www.acmicpc.net/board/view/92320
https://www.acmicpc.net/board/view/95620
*/
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        int tc = 1;
        int L, P, V;
        Scanner myObj = new Scanner(System.in);
        while (true) {
            L = myObj.nextInt();
            P = myObj.nextInt();
            V = myObj.nextInt();
            if (L == 0 && P == 0 && V == 0) break;
            System.out.printf("Case %d: %d\n", tc, (V / P)*L + Math.min((V % P), L));

            tc += 1;
        }
    }
}

// 다른 사람 코드 참고
// https://www.acmicpc.net/source/2703055
/*
#include <stdio.h>
int main()
{
	int L, P, V, i = 0;
	while (1)
	{
		i++;
		scanf("%d %d %d", &L, &P, &V);
		if (!L)
			break;
		printf("Case %d: %d\n", i, (V / P)*L + (V%P > L ? L : V%P));
	}
}
*/