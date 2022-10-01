"""
5073 삼각형과 세 변

삼각형 변의 길이 관계에 따라 맞는 이름 출력하기
기초 if 연습 문제
"""
while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0 and numbers[1] == 0 and numbers[2] == 0:
        break
    
    _max = max(numbers)
    if sum(numbers) - _max <= _max:
        print("Invalid")
        continue
    
    if numbers[0] == numbers[1] and numbers[1] == numbers[2]:
        print("Equilateral")
    elif numbers[0] != numbers[1] and numbers[0] != numbers[2] and numbers[1] != numbers[2]:
        print("Scalene")
    else:
        print("Isosceles")

# https://www.acmicpc.net/source/42366282    
"""
main(a,b,c){while(scanf("%d%d%d",&a,&b,&c),a)puts(a^b|b^c?a<b+c&b<a+c&c<a+b?a==b|b==c|a==c?"Isosceles":"Scalene":"Invalid":"Equilateral");}
"""

# https://www.acmicpc.net/source/32960132
"""
#include<cstdio>

int main(){
	int a,b,c;
	while(1){
		scanf("%d %d %d",&a,&b,&c);
		if(!a)break;
		if(a>=b+c||b>=a+c||c>=a+b)printf("Invalid\n");
		else if(a==b&&b==c)printf("Equilateral\n");
		else if(a==b||b==c||a==c)printf("Isosceles\n");
		else printf("Scalene\n");
	}
}
"""
