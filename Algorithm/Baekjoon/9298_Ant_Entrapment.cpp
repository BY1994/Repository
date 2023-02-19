/*
9298 Ant Entrapment

기하학
개미들을 다 포함하는 직사각형의 면적, 둘레 구하기 
*/

#include <stdio.h>

inline double fabs(double x) {
    return (x >= 0.0)? x : -x;
}

inline double fmax(double a, double b) {
    return (a >= b)? a : b;
}

inline double fmin(double a, double b) {
    return (a >= b)? b : a;
}

int main(void)
{
    int TC, N;
    double x, y;
    double _minx, _miny, _maxx, _maxy;
    
    scanf("%d", &TC);
    for (int i = 1; i <= TC; ++i) {
        _minx = _miny = 1001.0;
        _maxx = _maxy = -1001.0;
        scanf("%d", &N);
        while (N--) {
            scanf("%lf %lf", &x, &y);
            _minx = fmin(_minx, x);
            _miny = fmin(_miny, y);
            _maxx = fmax(_maxx, x);
            _maxy = fmax(_maxy, y);
        }
        printf("Case %d: Area %lf, Perimeter %lf\n", i,\
        fabs((_maxx - _minx) * (_maxy - _miny)),\
        fabs((_maxx - _minx)*2) + fabs((_maxy - _miny)*2));
    }

    return 0;
}
