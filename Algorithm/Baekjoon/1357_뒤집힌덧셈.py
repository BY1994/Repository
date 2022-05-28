"""
1357 뒤집힌 덧셈

숫자 뒤집으려고 하면 몇 자리까지 있는지 확인해야하는데,
문자열 뒤집기로 하면 간단
마지막에 숫자로 변환 안 해주면 10 뒤집은 01이 1이 아니라 그대로 01로 출력됨
"""
        
X, Y = input().split()
print(int(str(int(X[::-1])+int(Y[::-1]))[::-1]))

# 정답 예시
# https://www.acmicpc.net/source/4324342
"""
R(x,r){for(r=0;x;x/=10)r=10*r+x%10;return r;}
main(x,y){scanf("%d%d",&x,&y);printf("%d",R(R(x)+R(y)));}
"""
