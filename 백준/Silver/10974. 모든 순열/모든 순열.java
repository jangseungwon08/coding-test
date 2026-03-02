import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static StringBuilder sb;
    static List<Integer> arr;
    static boolean[] isVisited;
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        sb = new StringBuilder();
        arr = new ArrayList<>();
        isVisited = new boolean[n];
        dfs(0);
        System.out.println(sb.toString());
    }
    static void dfs(int depth){
        if(depth == n){
            for(int i = 0; i< n ; i++){
                sb.append(arr.get(i)).append(" ");
            }
            sb.append("\n");
            return;
        }
        for(int i = 0; i<n; i++){
            if(!isVisited[i]){
                isVisited[i] = true;
                arr.add(i+1);
                dfs(depth+1);
                isVisited[i] = false;
                arr.remove(arr.size()-1);
            }
        }
    }
}