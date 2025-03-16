import java.io.*;
import java.util.*;

public class Main {
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for(int i = 0; i< N; i++){
            //출력할 때마다 count를 초기화 시켜줘야함
            count = 0;
            System.out.println(isPalindrome(br.readLine()) + " " + count);
        }
        br.close();
    }
    public static int recursion(String s, int l, int r) {
        count++;
        if (l >= r) return 1;//왼쪽값이 오른쪽 값보다 높아졌으면(펠린드롬이라는 뜻)
        else if (s.charAt(l) != s.charAt(r)) return 0;//왼쪽값과 오른쪽 값이 다르면(펠린드롬이 아니라는 뜻)
        else return recursion(s, l + 1, r - 1);//l번째 값과 r번째 값이 같지만 l이 r보다 작을 때

    }

    public static int isPalindrome(String s){
        return recursion(s, 0, s.length()-1);
    }
}
