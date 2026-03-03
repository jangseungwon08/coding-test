import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static boolean[] isVisited;
    static int[][] arr;
    static int n, l;
    static int maxFlavor;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int tc = 1; tc <= T; tc++){
            StringTokenizer st= new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            l = Integer.parseInt(st.nextToken());
            isVisited = new boolean[n];
            arr = new int[n][2];
            maxFlavor = 0;
            for(int i = 0; i< n; i++){
                st = new StringTokenizer(br.readLine());
                int flavor = Integer.parseInt(st.nextToken());
                int kcal = Integer.parseInt(st.nextToken());
                arr[i][0] = flavor;
                arr[i][1] = kcal;
            }
            combinations(0,0,0);
            System.out.println("#" + tc + " " + maxFlavor);
        }
    }
    static void combinations(int limit, int flavorSum, int depth){
//       제한 칼로리보다 낮고 현재까지 maxFlavor보다 크면
        if(depth == n) {
            if (limit <= l && flavorSum > maxFlavor) {
                maxFlavor = flavorSum;
            }
            return;
        }
        isVisited[depth] = true;
        combinations(limit + arr[depth][1], flavorSum + arr[depth][0], depth+1);
        isVisited[depth] = false;
        combinations(limit, flavorSum, depth+1);
    }
}
