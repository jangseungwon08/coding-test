import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;

public class Main {
    static int[][] minCost;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        minCost = new int[n + 1][n + 1];
        for(int i = 0; i< n+1; i++) {
            Arrays.fill(minCost[i], Integer.MAX_VALUE);
        }
//        자기자신은 비용 0
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == j) minCost[i][j] = 0;
            }
        }
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            if(minCost[s][e] != Integer.MAX_VALUE && minCost[s][e] < c) continue;
            minCost[s][e] = c;
        }
//        k는 노드 숫자
        for(int k = 1; k < n+1; k++) {
            for(int a = 1; a < n+1; a++){
                for(int b = 1; b < n+1; b++){
                    if(minCost[a][k] != Integer.MAX_VALUE && minCost[k][b] != Integer.MAX_VALUE) {
//                   a에서 b로 가는 경우는 min(그냥 a에서 b로 바로 가는 경우 , 1번 노드를 거쳐가는 경우)
                        minCost[a][b] = Math.min(minCost[a][b], minCost[a][k] + minCost[k][b]);
                    }
                }
            }
        }
        for(int i = 1; i< n+1; i++){
            for(int j =1 ; j< n+1; j++){
                if(minCost[i][j] == Integer.MAX_VALUE) minCost[i][j] = 0;
            }
        }
        for(int i = 1; i< n+1; i++){
            for(int j = 1; j< n+1; j++){
                System.out.print(minCost[i][j] + " ");
            }
            System.out.println();
        }
    }

}