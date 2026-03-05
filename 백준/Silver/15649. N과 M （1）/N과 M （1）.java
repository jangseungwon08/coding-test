import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, m;
    static int[] arr;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[m];
        boolean[] visited = new boolean[n];
        permutations(0, visited);
    }
    static void permutations(int depth, boolean[] visited){
        if(depth == m){
            for(int i = 0; i< m; i++){
                System.out.print(arr[i] + " ");
            }
            System.out.println();
            return;
        }
        for(int i = 0; i< n; i++){
            if(!visited[i]){
                visited[i] = true;
                arr[depth] = i+1;
                permutations(depth+1, visited);
                visited[i] = false;
            }
        }
    }
}
