import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        boolean[][] visited = new boolean[n+1][n+1];
        for(int i = 0; i< m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            visited[a][b] = true;
        }
        for(int k = 1; k <= n; k++){
            for(int i = 1; i<= n; i++){
                for(int j = 1; j<= n; j++) {
//                    i에서 j로 갈 수 있음 판단 -> i에서 k로 k에서 j로 (즉, i정점에서 k정점을 거쳐서 j정점까지 갈 수 있으면)
                    if(visited[i][k] && visited[k][j]){
                        visited[i][j] = true;
                    }
                }
            }
        }
        int count = 0;
        for(int i = 1; i<=n ;i++){
            int rowCount = 0;
            for(int j = 1; j<=n; j++){
//                i에서 j로 갈 수 있거나 j에서 i로 갈 수 있으면
                if(visited[i][j] || visited[j][i]) rowCount++;
            }
            if(rowCount == n-1) count++;
        }
        System.out.println(count);
    }
}
