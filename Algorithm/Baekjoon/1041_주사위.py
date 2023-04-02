"""
1041 주사위

수학, 그리디

직접 경우의 수를 다 적어보고 그대로 코드로 옮김
    +---+        
    | D |        
+---+---+---+---+
| E | A | B | F |
+---+---+---+---+
    | C |        
    +---+        
이와 같이 서로 마주볼 수 없는 A-F, B-E, C-D 를 제외하고는 모두 2개씩과 3개씩 묶일 수 있다.
2면이 보이는 경우: 6C2 - 맞은편 관계인 3쌍 = 15 - 3 = 12
3면이 보이는 경우: 붙어있는 3개 면을 직접 따져보니 8가지 경우의 수가 나옴
1면이 보이는 경우: 모든 면 중 min 값

3면이 보이는 경우는 맨 위의 모서리 4개만 존재한다.
1면이 보이는 경우는 맨 위에는 아래처럼 (N-2)*(N-2)만 존재한다.
□□□□
□■■□
□■■□
□□□□
그러나 옆면의 경우에는 바닥에 닿는 부분도 1면만 보인다.
□□□□
□■■□
□■■□
□■■□
따라서 두 경우를 더해주면 된다. (N-2)*(N-2)*1 + (N-2)*(N-1)*4
2면이 보이는 경우는 옆 모서리 4곳에 있는 (N-1) 개가 있고,
□□□□
■□□■
■□□■
■□□■
맨 위에 N-2 만큼 4개가 있다
□■■□
■□□■
■□□■
□■■□
따라서 두 경우를 더하면 (N-1)*4 + (N-2)*4 개가 된다.
위의 식들은 N 이 반드시 2 이상이어야하는데,
N 이 1인 경우는 어차피 주사위가 1개 뿐이기 때문에
위의 식이 적용되지 않고 한 주사위의 5면이 모두 사용된다.
따라서 가장 숫자가 큰 한 면만 제외하고 나머지 면이 보이도록 하면 된다.

완전탐색을 한다면,
면을 가능한 방향으로 돌려가면서 최솟값을 찾도록 짤 수 있을 것
"""

N = int(input())
dice = list(map(int, input().split()))
if N == 1:
    print(sum(dice)-max(dice))
else:
    plane3 = 4
    plane1 = (N-2)*(N-1)*4 + (N-2)*(N-2)*1
    plane2 = (N-1)*4 + (N-2)*4
    min3 = min([dice[0]+dice[1]+dice[2], dice[0]+dice[1]+dice[3],
                dice[0]+dice[2]+dice[4], dice[0]+dice[3]+dice[4],
                dice[1]+dice[2]+dice[5], dice[1]+dice[3]+dice[5],
                dice[2]+dice[4]+dice[5], dice[3]+dice[4]+dice[5]])
    min2 = min([dice[0]+dice[1], dice[0]+dice[2], dice[0]+dice[3], dice[0]+dice[4],
                dice[1]+dice[2], dice[1]+dice[3], dice[1]+dice[5], dice[2]+dice[4],
                dice[2]+dice[5], dice[3]+dice[4], dice[3]+dice[5], dice[4]+dice[5]])
    min1 = min(dice)
    print(plane1*min1 + plane2*min2 + plane3*min3)

# https://www.acmicpc.net/source/4529507
"""
#include <stdio.h>

int main(){
    unsigned long long n;
    unsigned long long arr[6],min[3]={50,100,150},sp=0;
    scanf("%llu",&n);
    for(int i=0;i^6;i++){
        scanf("%llu",&arr[i]);
        if(sp<arr[i])sp=arr[i];
    }
    if(n==1)return 0*printf("%llu\n",arr[0]+arr[1]+arr[2]+arr[3]+arr[4]+arr[5]-sp);
    for(int i=0;i^3;i++)
        if(arr[i]<arr[5-i])min[i]=arr[i];
        else min[i]=arr[5-i];
    for(int i=0;i^2;i++)
        for(int j=i+1;j^3;j++)
            if(min[i]>min[j]){min[i]^=min[j];min[j]^=min[i];min[i]^=min[j];}
    min[1]+=min[0];
    min[2]+=min[1];
    printf("%llu\n",((n-2)*(n-2)+(n-2)*(n-1)*4)*min[0]+((n-1)*4+(n-2)*4)*min[1]+4*min[2]);
}
"""

# https://www.acmicpc.net/source/4265390
"""
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
	int n;
	scanf("%d", &n);

	int a[6];
	for(int i = 0; i < 6; i++)
		scanf("%d", a+i);

	swap(a[3], a[4]);

	if(n == 1)
	{
		int sum = 0, max_val = -1;
		for(int i = 0; i < 6; i++)
		{
			max_val = max(max_val, a[i]);
			sum += a[i];
		}
		printf("%d\n", sum - max_val);
		return 0;
	}

	int one=1500, two=1500, three=1500;
	long long num1, num2, num3;

	for(int j = 1; j < 5; j++)
	{
		int nj = (j == 4) ? 1 : j+1;
		one = min(one, a[j]);
		two = min(two, a[j]+a[nj]);
		two = min(two, min(a[0], a[5]) + a[j]);
		three = min(three, min(a[0], a[5]) + a[j]+a[nj]);
	}
	one = min(one, min(a[0], a[5]));

	num1 = (long long)(n-2) * (n-1) * 4 + (long long)(n-2)*(n-2);
	num2 = (n-2) * 4 + (n-1) * 4;
	num3 = 4;

	printf("%lld\n", one*num1 + two*num2 + three*num3);
	return 0;
}
"""

# https://www.acmicpc.net/source/3016030
"""
//
//  main.cpp
//
//  Created by KJBS2 on 5/29/16.
//  Copyright © 2016 KJBS2. All rights reserved.
//

#include <stdio.h>
#include <algorithm>
#include <stdlib.h>

using namespace std;

const int INF = 0x7fffffff;

int N;
int Nr[6];

int main()
{
    scanf("%d", &N);
    for(int i=0; i<6; i++)
        scanf("%d", &Nr[i]);
    
    if(N == 1)
    {
        int maxNr = 0;
        int sum = 0;
        for(int i=0; i<6; i++)
        {
            maxNr = max(maxNr, Nr[i]);
            sum += Nr[i];
        }
        printf("%d\n", sum - maxNr);
        return 0;
    }
    
    int oneMin = INF;
    for(int i=0; i<6; i++)
        oneMin = min(oneMin, Nr[i]);
    
    int twoMin = INF;
    int side1[4] = {1, 1, 4, 4};
    int side2[4] = {2, 3, 2, 3};
    for(int i=0; i<4; i++)
        twoMin = min(twoMin, Nr[side1[i]] + Nr[side2[i]]);
    for(int i=1; i<=4; i++)
    {
        twoMin = min(twoMin, Nr[i] + Nr[0]);
        twoMin = min(twoMin, Nr[i] + Nr[5]);
    }
    
    int threeMin = INF;
    for(int i=0; i<4; i++)
    {
        threeMin = min(threeMin, Nr[0] + Nr[side1[i]] + Nr[side2[i]]);
        threeMin = min(threeMin, Nr[5] + Nr[side1[i]] + Nr[side2[i]]);
    }
    
    long long oneSum = 1ll * oneMin * ( 4*(N-2) + 1ll * 5*(N-2)*(N-2) );
    long long twoSum = 1ll * twoMin * ( 8*(N-2) + 4);
    long long threeSum = 1ll * threeMin * 4;
    printf("%lld", oneSum + twoSum + threeSum);
    
    return 0;
}
"""

# https://www.acmicpc.net/source/4174521
"""
#include	<cstdio>
#pragma warning(disable : 4996)
#define min2(x,y) ((x) > (y) ? (y) : (x))
#define min4(w,x,y,z) (min2(w,x) < min2(y,z) ? min2(w,x) : min2(y,z))
int main()
{
	int N;
	int d[6], dd[6];
	scanf("%d", &N);
	scanf("%d%d%d%d%d%d", &d[0], &d[1], &d[2], &d[3], &d[4], &d[5]);
	if (N == 1)
	{
		int max = 0;
		int locM = 0;
		for (int i = 0; i < 6; ++i)
		{
			if (max < d[i])
			{
				max = d[i];
			}
		}
		printf("%d", d[0] + d[1] + d[2] + d[3] + d[4] + d[5] - max);
		return 0;
	}
	dd[0] = 5;	dd[1] = 4;	dd[2] = 3;	dd[3] = 2;	dd[4] = 1;	dd[5] = 0;
	int loc1;
	int min = 100;
	for (int i = 0; i < 6; ++i)
	if (d[i] < min)
	{
		min = d[i];
		loc1 = i;
	}

	int top1, top2, top3;
	top1 = min;

	min = 100;
	for (int i = 0; i < 6; ++i)
	{
		if (i != loc1 && i != dd[loc1])
		{
			if (min > d[i])
				min = d[i];
		}
	}
	top2 = min + top1;//6의 옆에 있는 애 중 가장 큰애 

	top3 = top1;
	if (loc1 == 0 || loc1 == 5)
	{
		top3 += min4((d[1] + d[2]), (d[2] + d[4]), (d[3] + d[4]), (d[1] + d[3]));
	}
	else if (loc1 == 1 || loc1 == 4)
	{
		top3 += min4((d[0] + d[2]), (d[0] + d[3]), (d[2] + d[5]), (d[3] + d[5]));
	}
	else if (loc1 == 2 || loc1 == 3)
	{
		top3 += min4((d[0] + d[1]), (d[0] + d[4]), (d[1] + d[5]), (d[4] + d[5]));
	}
	long long int res = 0;
	res += 4 * top3;
	res += (long long int)(N - 2) * (N - 2) * top1 * 5;
	res += (long long int)(N - 2) * top2 * 8;
	res += 4 * top2;
	res += (long long int)(N - 2)*top1 * 4;

	printf("%lld\n", res);
	return 0;
}
"""
