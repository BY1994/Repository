/*
1673 ġŲ ����

�ʵ��б� �� �� ��ȯ�ϱ� ����...

k �� �ݵ�� 1���� ũ�ٴ� ���� ����  

ó�� Ǭ �ڵ�� ������ �¾Ƽ� �´� �����̶�� �����ߴµ�,
������ ó���� �� �ؼ� ����� ������ �־���
���� ���� �ݷ�
5 3
���� 7
�߸��� �� 6 

* ���� �Խ��� �ݷ� ã�� 
long long ���������Ѵٰ� �����ؼ� ���� �ݷ�
1000000000 2
1999999999 
�׷��� int �����ε� �Ѿ�� �ʾҴ�.
�Ʒ� �ڵ��� ������ int ������ �ƴ϶� �Է��� 1���� �޾Ƽ�����.
https://www.acmicpc.net/board/view/59059

��͸� �Ἥ segmentation fault �� �߻��ϴ� �ڵ�
https://www.acmicpc.net/board/view/32147

* ����ȭ
k �� 3�̸�,
3 �� ������ (+1) 
������ 2���� � ���̴��� ���� �ٷ� ��� ���� ((n-3) / 2)
3 ���� ������ 1���� �Ǳ� ������ ������ 2���� ���ļ� �ٽ� 3���� �ȴ�!
3 2 2 2 2 ... �̷� ���̸� 2�� ������ ������ŭ ��� ���������� 3���� ���� �� ����
 
* ���ڵ� 
include ���� ���� (���� �����Ϸ����� stdio.h �ٿ���) 
main �� int ���� ���� (���� �����Ϸ����� default �� �ٿ���) 
int main �̾ return 0; ���� ���� 
main �ȿ� argument �� int ������ ���� ����
%d %d �� �ʿ� ����
scanf() > 0 ���� EOF ó���� �ʿ� ���� 
*/

// ���ڵ� 
// ���� ���� ���� (main �տ� int �ڵ����� �ٿ���) 
#if 1
main(n,k){while(~scanf("%d%d",&n,&k))printf("%d\n",n+1+(n-k)/(k-1));}
#endif

// ���� �ڵ� 2
#if 0
#include <stdio.h>

int main(void)
{
    long long n, k;
    while (scanf("%lld %lld", &n, &k) > 0)
        printf("%lld\n", n + 1 + (n-k) / (k-1));
    return 0;
}
#endif 

// ���� �ڵ� 
#if 0
#include <stdio.h>

int main(void)
{
    long long n, k, chicken;
    while (scanf("%lld %lld", &n, &k) > 0) {
        chicken = n;
        while (n/k) {
            chicken += n/k;
            n = n/k + n%k;
        }
        printf("%lld\n", chicken);
    }

    return 0;
}
#endif

// Ʋ�� �ڵ� 
#if 0
#include <stdio.h>

int main(void)
{
    long long n, k, chicken;
    while (scanf("%lld %lld", &n, &k) > 0) {
        chicken = 0;
        while (n) {
            chicken += n;
            n /= k;
        }
        printf("%lld\n", chicken);
    }

    return 0;
}
#endif
