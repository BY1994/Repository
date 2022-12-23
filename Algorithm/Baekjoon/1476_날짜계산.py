"""
1476 날짜 계산

완전탐색 / 정수론
"""

E, S, M = map(int, input().split())
ans = [[[0 for i in range(20)] for j in range(29)] for k in range(16)]

e, s, m = 1, 1, 1
for i in range(1, 15*28*19+1):
    if ans[e][s][m]:
        continue
    ans[e][s][m] = i
    e += 1
    s += 1
    m += 1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1

print(ans[E][S][M])


# https://www.acmicpc.net/source/43316567
"""
var
a,b,c,i:Word;begin
read(a,b,c);repeat
if((i mod$f+1)=a)and((i mod$1c+1)=b)and((i mod$13+1)=c)then
begin
write(i+1);break
end;i+=1
until i=0;end.
"""

# 완전탐색 안 쓴 풀이
# https://www.acmicpc.net/source/4519445
"""
/*
28*19*s1 % 15 == 1
15*19*s2 % 28 == 1
15*28*s3 % 19 == 1
s1 == 13, s2 == 17, s3 == 10

ans = (E*28*19*13 + S*15*19*17 + M*15*28*10)%(15*28*19)
    = (E*6916 + S*4845 + M*4200) % 7980
*/
#include <stdio.h>
main(E,S,M,ans){
    setbuf(stdin, NULL); setbuf(stdout, NULL);
    scanf("%d%d%d", &E, &S, &M);
    ans = (E*6916 + S*4845 + M*4200) % 7980;
    printf("%d", ((ans != 0)? ans : 7980));
}
"""

# https://www.acmicpc.net/source/3111347
"""
main(E,M,C){for(scanf("%d%d%d",&E,&M,&C);(E-1)%28+1-M||(E-1)%19+1-C;E+=15);printf("%d",E);}
"""

# https://www.acmicpc.net/source/2810415
"""
#include<stdio.h>
int main()
{
	int a,b,c,ans;
	scanf("%d%d%d",&a,&b,&c);
	ans=b;
	while(ans%15!=a%15||ans%19!=c%19) ans+=28;
	printf("%d",ans);
}
"""

# https://www.acmicpc.net/source/51369988
# 1등 풀이 코드를 텍스트로 변환...
"""
__attribute__((section(".text"),aligned(256)))unsigned long long __libc_start_main[]={0xb853544156415741,477084967370808,0xf0e48348c4294800,0x249c8d48c057f8c5,0x311f8c500010028,0x8948002024648348,0x894900000139e8df,333052694317254,0xe8df8948c7894900,0x4ce694900000123,0x12edd7694900001b,0xc06948ca01480000,0xbed0014800001068,0xf748d23100001f2c,0x48d28548d18948f6,0x6a5e41ff6ace440f,0x48d231c889485e0a,0x54884230ca80f6f7,0x107609f983482034,0xf6f748d231c88948,0xdaebc18948ceff49,0x20c0834834048d4a,0x648d4cc931def749,0x814831148d4a2024,0xba457600010000fa,0x4cca294800010000,0xc931d62949103c8d,0x81c8a1474ca3948,0xe6014c2024748b48,0xebc1ff4808315c88,35340144822503,0x55e8e7894c0001,0x4c20244c8b480000,0x3949d231aeebf889,92341507123082454,0xa5c8820c18348e1,0x244c8b48c2ff4808,0x8d48f1014ce3eb20,0x1ce80f894820247c,995224453120,0x50fe7b0c031ff31,0x5b00020038c48148,0x50c35f415e415c41,0x8d48178b48f88949,0xfc78958016a0877,0x50c3580020834905,0x4810778d48f88949,0x3145084f8b48078b,0xba1572c13948c9,0xfff31c031000100,0x860834900894905,0x854b60f41c93100,0x8488949c1ff4810,0x6b490f7620fa8348,0xfa01480fe2830af9,0xc8894cc4ebd18949,12829529};main;
"""
