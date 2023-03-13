/*
2765 자전거 속도

수학, 사칙연산
소수점 반올림 연습 
*/
#include <stdio.h>
#include <math.h>

int main(void)
{
    double d, cycle, t;
    double dist, MPH;
    int tc = 0;
    while (1) {
        tc++;
        scanf("%lf %lf %lf", &d, &cycle, &t);
        if (cycle == 0) break;
        dist = (d*cycle*3.1415927 / (12*5280));
        MPH = dist / (t/3600);
        printf("Trip #%d: %0.2lf %0.2lf\n", tc, round(dist*100)/100, round(MPH*100)/100);
    }
    return 0;
}
