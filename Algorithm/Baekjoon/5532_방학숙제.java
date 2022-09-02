/*
5532 방학 숙제

- 국어와 수학을 하루에 얼마나 풀 수 있는지 나눠야하는줄 알았는데 그건 아니었다.
하루에 국어도 풀고 수학도 풀 수 있는 거였다.
그래서둘 중 max로 풀면 된다.
- / 를 한 후 나온 소수점을 올림으로 해서 풀려고 했는데,
그러면 library 도 찾아야하고 형변환이 어려워서 불편할 거로 예상되어
단순히 나머지가 있는지 확인하는 방식으로 풀이하였다.
*/
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner myObj = new Scanner(System.in);
        int L = myObj.nextInt();
        int A = myObj.nextInt();
        int B = myObj.nextInt();
        int C = myObj.nextInt();
        int D = myObj.nextInt();
        
        int Korean = A/C;
        if (A % C > 0) Korean += 1;
        int Math = B/D;
        if (B % D > 0) Math += 1;
        
        if (Korean > Math) {
            System.out.println(L - Korean);
        }
        else System.out.println(L - Math);
    }
}