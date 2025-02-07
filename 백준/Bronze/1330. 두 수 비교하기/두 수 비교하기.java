import java.io.*;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        /*사용자로부터 입력받아
        BufferedReader로부터 한줄을 입력받아서 입력된 값은 String형태로 저장됨.
        Ex) 3 5를 입력하면 str = "3 5";로 된다.*/
        String str = br.readLine();
        /*공백을 기준으로(" ") 단어(토큰)을 분리한다.
        * str에서 " "공백을 기준으로 토큰들을 분리한다.
        * "3 5"라는 문자열을 "3"과 "5" 두개의 토큰으로 나눈다.
        * 즉 st에서는 "3"과 "5"가 저장된다.
        *  */
        StringTokenizer st = new StringTokenizer(str, " ");
        //st.nextToken()-> 으로 st의 현재토큰을 반환하고 Integer.parseInt로 정수 3으로 반환
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        //삼항 연산자
        //A>B 보다 크면 ">" 출력
        System.out.println((A>B) ? ">" : ((A<B) ? "<" : "=="));
      }
    }