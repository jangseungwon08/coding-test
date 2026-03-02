
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class Node{
        int node;
        int weight;
        public Node(int node, int weight){
            this.node = node;
            this.weight = weight;
        }
    }
    static List<List<Node>> tree;
    static int maxSum;
    static int n;
    static int maxDisNode;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        tree = new ArrayList<>();
        maxSum = 0;
        for(int i = 0; i<=n; i++){
            tree.add(new ArrayList<>());
        }
        for(int i = 1; i< n; i++){
            StringTokenizer st= new StringTokenizer(br.readLine());
            int parent = Integer.parseInt(st.nextToken());
            int child = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            tree.get(parent).add(new Node(child, weight));
            tree.get(child).add(new Node(parent, weight));
        }
        boolean[] visited = new boolean[n+1];
        visited[1] = true;
//        루트 노드에서 가장 먼 노드 탐색
        dfs(1, visited, 0);
//        가장 먼 노드에서 다시 탐색?
        visited = new boolean[n+1];
        visited[maxDisNode] = true;
        dfs(maxDisNode, visited, 0);
        System.out.println(maxSum);
    }
    static void dfs(int startNode, boolean[] visited, int sum){
        if(maxSum < sum){
            maxSum = sum;
            maxDisNode = startNode;
        }
//        시작점부터 인접한 트리까지
        for(int i = 0 ; i< tree.get(startNode).size(); i++){
            Node node = tree.get(startNode).get(i);
//            인접 노드에 방문한 이력 없으면
            if(!visited[node.node]){
                visited[node.node] = true;
                dfs(node.node, visited, sum + node.weight);
            }
        }
    }
}