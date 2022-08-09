/*
11382 input/output 연습
Java 연습

1. class 이름은 Main으로
https://limu-study.tistory.com/5

2. Scanner 로 input 받는 법
https://www.w3schools.com/java/java_user_input.asp

3. BufferedReader 사용법 (사용한 샘플 풀이)
https://www.acmicpc.net/source/13515632
*/

import java.util.Scanner;  // Import the Scanner class

public class Main {
    public static void main(String args[]) {
        Scanner myObj = new Scanner(System.in);
        long A = myObj.nextLong();  // Read user input
        long B = myObj.nextLong();
        long C = myObj.nextLong();
        
        System.out.println(A+B+C);
    }
}

// 1등 풀이
// https://www.acmicpc.net/source/13515632
/*
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());
        long C = Long.parseLong(st.nextToken());
        System.out.println(A + B + C);
    }
}
*/