import java.util.*;

class Solution {
    static class Node{
        int to;
        int weigth;
        Node(int to, int weigth){
            this.to = to;
            this.weigth = weigth;
        }
    }

    static List<List<Node>> adjList = new ArrayList<>();
    public int solution(int n, int s, int a, int b, int[][] fares) {
        long answer = Long.MAX_VALUE;
        for(int i = 0; i<= n; i++){
            adjList.add(new ArrayList<>());
        }
        for(int i = 0; i< fares.length; i++){
            int from = fares[i][0];
            int to = fares[i][1];
            int cost = fares[i][2];
            adjList.get(from).add(new Node(to, cost));
            adjList.get(to).add(new Node(from, cost));
        }
        int[] distanceS = dijkstra(s,n);
        int[] distanceA = dijkstra(a,n);
        int[] distanceB = dijkstra(b,n);
//      각각의 출발 지점에서 가장 작은 간선 가중치를 가진 노드가 가장 좋은 효율
        for(int i = 1; i<= n; i++){
            answer = Math.min(answer, distanceS[i] + distanceA[i] + distanceB[i]);
        }
        return (int) answer;
    }

    public static int[] dijkstra(int start, int n){
        int[] distance = new int[n+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        PriorityQueue<Node> pq = new PriorityQueue<>((n1,n2) -> Integer.compare(n1.weigth, n2.weigth));
        pq.offer(new Node(start, 0));
        distance[start] = 0;
        while(!pq.isEmpty()){
            Node current = pq.poll();
            List<Node> nextNodeList = adjList.get(current.to);
            for(Node next: nextNodeList){
//                 다음 가야되는 거리보다 더 작은 값이 있다면
                if(distance[next.to] > distance[current.to] + next.weigth){
                    distance[next.to] = distance[current.to] + next.weigth;
                    pq.offer(new Node(next.to, distance[current.to] + next.weigth));
                }
            }
        }
        return distance;
    }

}