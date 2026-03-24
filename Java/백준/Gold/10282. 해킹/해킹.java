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
    static int[] distance;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(int tc = 1; tc <= t; tc++){
            StringTokenizer st = new StringTokenizer(br.readLine());
//            노드 개수
            int n = Integer.parseInt(st.nextToken());
//            정점 개수
            int d = Integer.parseInt(st.nextToken());
//            시작 지점
            int start = Integer.parseInt(st.nextToken());
            graph = new ArrayList<>();
            distance = new int[n+1];
            Arrays.fill(distance, Integer.MAX_VALUE);
            for(int i = 0; i <= n; i++){
                graph.add(new ArrayList<>());
            }
            for(int i = 0 ; i< d; i++){
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int weight = Integer.parseInt(st.nextToken());
                graph.get(b).add(new Node(a, weight));
            }
            dijkstra(start);
            int dist = 0;
            int nodeCount = 0;
            for(int i = 1; i<= n; i++){
                if(distance[i] != Integer.MAX_VALUE){
                    nodeCount++;
                if(dist < distance[i]){
                    dist = distance[i];
                }
            }
            }
            System.out.println(nodeCount + " " + dist);
        }
    }
    static void dijkstra(int start){
        PriorityQueue<Node> pq = new PriorityQueue<>((o1,o2) -> Integer.compare(o1.weight, o2.weight));
        pq.add(new Node(start, 0));
        distance[start] = 0;
        while(!pq.isEmpty()){
            Node current = pq.poll();
            List<Node> nextNodeList = graph.get(current.v);
            for(Node next: nextNodeList){
//                최소값 보장하면
                if(distance[next.v] > next.weight + distance[current.v]){
                    pq.offer(new Node(next.v, next.weight + distance[current.v]));
                    distance[next.v] = next.weight + distance[current.v];
                }
            }
        }
    }
}