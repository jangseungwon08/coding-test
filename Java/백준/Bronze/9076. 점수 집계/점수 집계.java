import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] scores;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        scores = new int[5];
        for(int i = 0; i< n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 5; j++){
                scores[j] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(scores);
            int sum = 0;
            for(int j = 1; j< 4; j++){
                sum += scores[j];
            }
            sb.append(scores[3] - scores[1] >= 4? "KIN": sum).append("\n");
        }
        System.out.println(sb);
    }
}