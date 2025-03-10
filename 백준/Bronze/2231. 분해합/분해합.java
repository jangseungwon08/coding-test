import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str_N = br.readLine();
        int N_len = str_N.length();

        int N = Integer.parseInt(str_N);
        int res = 0;
        for(int i = (N-(9*N_len)); i < N; i++){
            int num = i;
            int sum = 0;
            while(num != 0){
                sum += num % 10;
                num = num / 10;
            }
            if(sum + i == N){
                res = i;
                break;
            }
        }
        System.out.println(res);
    }
}
