import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int[] arr;
    static int m, n;
    static int[] permuList;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int [n];
        permuList = new int[m];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i< n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        permutations(0);
        System.out.println(sb);
    }
    static void permutations(int depth){
        if(depth == m){
            for(int i = 0; i< m; i++){
                sb.append(permuList[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for(int i = 0; i< n; i++){
            permuList[depth] = arr[i];
            permutations(depth+1);
        }
    }

}
