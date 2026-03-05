import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] parent;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        parent = new int[n+1];
        for(int i = 0; i<=n; i++){
            parent[i] = i;
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i< m; i++){
            st = new StringTokenizer(br.readLine());
            int calc = Integer.parseInt(st.nextToken());
            if(calc == 0){
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                union(a,b);
            }
            if(calc == 1){
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                if(find(a) != find(b)) sb.append("NO").append("\n");
                else sb.append("YES").append("\n");
            }
        }
        System.out.println(sb);
    }
    static void union(int a, int b){
        int fa = find(a);
        int fb = find(b);
        if(fa != fb) parent[fa] = fb;
    }
//    부모와 같은 값을 찾는 것
    static int find(int x){
        if(x == parent[x]) return x;
        else return parent[x] = find(parent[x]);
    }

}
