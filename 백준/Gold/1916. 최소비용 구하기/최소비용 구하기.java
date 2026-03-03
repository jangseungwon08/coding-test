import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class Node{
        int vertex;
        int weight;
        Node(int vertex, int weight){
            this.vertex = vertex;
            this.weight = weight;
        }
    }
    static List<List<Node>> adjList;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        adjList = new ArrayList<>();
        for(int i = 0; i<=n; i++){
            adjList.add(new ArrayList<>());
        }
        for(int i = 0; i< m; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            adjList.get(start).add(new Node(end,weight));
        }
        StringTokenizer st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());
//        거리 비용 업데이트를 위한 dist배열
        int[] dist = new int[n+1];
//        최소한의 비용을 구해야하기 때문에 maxValue값으로 업데이트
        Arrays.fill(dist, Integer.MAX_VALUE);
//        가중치가 작은 값들로 내림차순
        PriorityQueue<Node> pq = new PriorityQueue<>((o1,o2) -> Integer.compare(o1.weight, o2.weight));
//        시작지점
        pq.offer(new Node(start, 0));
        while(!pq.isEmpty()){
            Node current = pq.poll();
//            현재까지 구한 최소비용이 현재 비용보다 작으면 이 길은 답 없음
            if(dist[current.vertex] < current.weight){
                continue;
            }
//            현재 정점과 연결되어있는 간선 찾기
            for(int i = 0; i< adjList.get(current.vertex).size(); i++){
//                다음 노드
                Node nextNode = adjList.get(current.vertex).get(i);
//                현재까지의 최소 비용이 현재 노드와 다음 노드 더한 값 보다 크면 최소 비용 업데이트
                if(dist[nextNode.vertex] > current.weight + nextNode.weight){
                    dist[nextNode.vertex] = current.weight + nextNode.weight;

                    pq.offer(new Node(nextNode.vertex, dist[nextNode.vertex]));
                }
            }
        }
        System.out.println(dist[end]);
    }
}
