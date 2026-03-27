import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class Node{
        int v;
        int weight;
        Node(int v, int weight){
            this.v = v;
            this.weight = weight;
        }
    }
    static List<List<Node>> graph;
    static int n,m;
    static int[] distance;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        distance = new int[n+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        graph = new ArrayList<>();
        for(int i = 0; i<=n; i++){
            graph.add(new ArrayList<>());
        }
        for(int i = 0; i< m; i++){
            st=  new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph.get(v1).add(new Node(v2,weight));
            graph.get(v2).add(new Node(v1, weight));
        }
        dijkstra(1);
        System.out.println(distance[n]);
    }
    public static void dijkstra(int start){
        PriorityQueue<Node> pq = new PriorityQueue<>((o1,o2) -> Integer.compare(o1.weight, o2.weight));
        pq.add(new Node(start, 0));
        distance[start] = 0;
        while(!pq.isEmpty()){
            Node current = pq.poll();
            if(current.weight > distance[current.v]) continue;
            List<Node> nextNodeList = graph.get(current.v);
            for(Node next: nextNodeList){
                if(distance[next.v] > distance[current.v] + next.weight){
                    distance[next.v] = distance[current.v] + next.weight;
                    pq.offer(new Node(next.v, distance[current.v] + next.weight));
                }
            }
        }
    }
}