import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] arr;
    static int[] choose;
    static int n, m;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n];
        choose = new int[m];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i< n ; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        permutations(0);
        System.out.println(sb);
    }
    static void permutations(int depth){
        if(depth == m){
            for(int i = 0; i< m; i++){
                sb.append(choose[i]).append(" ");
            }
            sb.append("\n");
            return;
        }
        int before = -1;
        for(int i = 0; i< n; i++){
            if(before != arr[i]){
                choose[depth] = arr[i];
                before = arr[i];
                permutations(depth+1);
            }
        }
    }
}
