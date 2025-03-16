import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        System.out.println(recursive_factorial(N));
    }
    //Long으로 하는 이유는 int 자료형 최대값을 초과함
    public static long recursive_factorial(int n){
        //Base Case --> 재귀 호출을 멈추는 조건
        if (n <= 0 ) return 1;
        //recursive Case --> 재귀 호출이 반복적으로 일어나는 부분
        //n을 곱해줌으로써 값이 증가할 수 있다.
        else return n * recursive_factorial(n-1);
    }
}
