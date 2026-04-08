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
        scores = new int[n];
        double scoresAvg = 0.0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++){
            scores[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(scores);
        int max = scores[n-1];
        for(int i = 0; i< n; i++){
            scoresAvg += 100.0 * scores[i] / max;
        }
        scoresAvg /= n;
        System.out.println(scoresAvg);
    }
}