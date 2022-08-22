/*
16486 운동장 한 바퀴
기하학

원의 둘레가 지름 * π 인 이유는 그게 원주율의 정의이기 때문이었다!
Java 의 float 의 유효자릿수는 7자리라고 한다.
https://devlog-wjdrbs96.tistory.com/254
(소수점 6자리 오차를 커버하려면 double 로 변경해야하는 것 아닌가?)
*/
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        float d1 = myObj.nextFloat();
        float d2 = myObj.nextFloat();
        
        System.out.println(d1*2 + d2*2*3.141592);
    }
}