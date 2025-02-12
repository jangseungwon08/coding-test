import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        int N = Integer.parseInt(str[0]);
        int X = Integer.parseInt(str[1]);
        String[] str1 = br.readLine().split(" ");
        int[] arr = new int[str1.length];
        for(int i = 0; i< str1.length; i++){
            arr[i] = Integer.parseInt(str1[i]);
        }
        //ArrayList동적배열 생성
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i = 0; i < str1.length; i++){
            if (arr[i] < X){
                answer.add(arr[i]);
            }
        }
        for(int i = 0; i< answer.size(); i++){
            System.out.print(answer.get(i) + " ");
        }
    }
}