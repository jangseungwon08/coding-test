import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] arr;
    static int n, m;
    static int[] permutationsList;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n];
        permutationsList = new int[m];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i< n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        combinations(0,0, permutationsList);
        System.out.println(sb);
    }
    static void combinations(int depth, int start, int[] list){
        if(depth == m){
            for(int i = 0; i< m; i++) {
                sb.append(list[i]).append(" ");
            }
            sb.append("\n");
            return;
        }
        for(int i = start; i< n; i++) {
                list[depth] = arr[i];
                combinations(depth + 1, i+1, list);
        }
    }
}
