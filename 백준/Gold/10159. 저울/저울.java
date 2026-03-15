import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static boolean[][] distance;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        distance = new boolean[n+1][n+1];
        for(int i = 0; i<=n; i++){
            distance[i][i] = true;
        }
        for(int i = 0; i< m; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            distance[from][to] = true;
        }
        for(int k= 1; k<=n; k++){
            for(int i = 1; i <=n; i++){
                for(int j = 1; j <=n; j++){
                    if(distance[i][k] && distance[k][j]){
                        distance[i][j] = true;
                    }
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            int count = 0;
            for (int j = 1; j <= n; j++) {
                //j i에서 j로 갈 수 있거나(i > j), 에서 i로 올 수 있다면(j > i) 관계를 아는 것
                // 둘 다 불가능하면 관계를 모르는 것
                if (!distance[i][j] && !distance[j][i]) {
                    count++;
                }
            }
            System.out.println(count);
        }
    }
}
