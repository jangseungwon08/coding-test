import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static boolean[] isVisited;
    static List<List<Integer>> graph;
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int vertex = Integer.parseInt(st.nextToken());
        int edge = Integer.parseInt(st.nextToken());
        isVisited = new boolean[vertex+1];
        graph = new ArrayList<>();
        for(int i = 0 ; i<= vertex; i++){
            graph.add(new ArrayList<>());
        }
        count = 0;
        for(int i = 0; i< edge; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
//        무방향 그래프 dfs
        for(int i = 1; i<= vertex; i++){
            if(!isVisited[i]){
                dfs(i);
                count++;
            }
        }
        System.out.println(count);
    }
    static void dfs(int depth){
        if(isVisited[depth]){
            return;
        }
        isVisited[depth] = true;
        List<Integer> next = graph.get(depth);
        for(int i = 0; i< next.size(); i++){
            dfs(next.get(i));
        }
    }
}