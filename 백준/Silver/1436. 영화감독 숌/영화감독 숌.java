import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str_N = br.readLine();
        int N = Integer.parseInt(str_N);
        int count = 1;
        int startNum = 666;
            while (N != count) {
                startNum += 1;
                if (String.valueOf(startNum).contains("666")) {
                    count++;
                }
        }
        System.out.println(startNum);
    }
}
