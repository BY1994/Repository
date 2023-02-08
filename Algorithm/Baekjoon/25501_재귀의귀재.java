/*
25501 재귀의 귀재

문제에서 주어진 Palindrome 재귀함수 활용하여
함수 호출 횟수, 리턴값 출력하기
*/

import java.util.Scanner;
public class Main{
    static int count = 0;

    public static int recursion(String s, int l, int r){
        count += 1;
        if(l >= r) return 1;
        else if(s.charAt(l) != s.charAt(r)) return 0;
        else return recursion(s, l+1, r-1);
    }
    public static int isPalindrome(String s){
        return recursion(s, 0, s.length()-1);
    }
    public static void main(String[] args){
        String word;
        int TC;
        
        Scanner sc = new Scanner(System.in);
        TC = sc.nextInt();
        while (TC > 0) {
            TC -= 1;
            word = sc.next();
            count = 0;
            System.out.printf("%d %d\n", isPalindrome(word), count);
        }
    }
}