import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String str = br.readLine();
        int sum = 0;
        for(int i = 0; i< N; i++){
            char c = str.charAt(i);
            int m = Character.getNumericValue(c);
            sum += m;
        }
        System.out.println(sum);
    }
    }