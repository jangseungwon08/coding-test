import org.w3c.dom.ls.LSOutput;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class Node{
        int v;
        int weight;
        Node(int v , int weight){
            this.v = v;
            this.weight = weight;
        }
    }
    static  List<List<Node>> graph;
    static int n, e;
    static int node1,node2;
    static int[] distance;
    static int[] distanceV1;
    static int[] distanceV2;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        graph = new ArrayList<>();
//        n은 정점의 개수, e는 간선의 개수
        n = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        distance = new int[n+1];
        distanceV1 = new int[n+1];
        distanceV2 = new int[n+1];
        Arrays.fill(distance, 1000000000);
        Arrays.fill(distanceV1, 1000000000);
        Arrays.fill(distanceV2, 1000000000);
        for(int i = 0; i<= n ; i++){
            graph.add(new ArrayList<>());
        }
        for(int i = 0; i< e; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph.get(start).add(new Node(end, weight));
            graph.get(end).add(new Node(start, weight));
        }
        st = new StringTokenizer(br.readLine());
//        반드시 거쳐야하는 노드
         node1 = Integer.parseInt(st.nextToken());
         node2 = Integer.parseInt(st.nextToken());
         distance[1] = 0;
         distanceV1[node1] = 0;
         distanceV2[node2] = 0;
         dijkstra(new Node(1, 0), distance);
         dijkstra(new Node(node1, 0), distanceV1);
         dijkstra(new Node(node2, 0), distanceV2);
//         node1을 먼저 거쳐서 가는 것과 node2를 먼저 거쳐서 가는 것
//        1 -> node1 -> node2 -> n;
        int pathA = distance[node1] + distanceV1[node2] + distanceV2[n];
        int pathB = distance[node2] + distanceV2[node1] + distanceV1[n];
        if(distance[node1] >= 1000000000 || distanceV1[node2] >= 1000000000 || distanceV2[n] >= 1000000000) pathA = 1000000000;
        if(distance[node2] >= 1000000000 || distanceV2[node1] >= 1000000000 || distanceV1[n] >= 1000000000) pathB = 1000000000;
        int ans = Math.min(pathA, pathB);
        System.out.println(ans >= 1000000000? -1 : ans);
    }

    static void dijkstra(Node start, int[] distance){
        PriorityQueue<Node> pq = new PriorityQueue<>((o1,o2) -> Integer.compare(o1.weight, o2.weight));
        pq.offer(start);
        while(!pq.isEmpty()){
            Node current = pq.poll();
            List<Node> nextNodeList = graph.get(current.v);
            for(Node nextNode : nextNodeList){
//                    다음 노드 최단거리의 최단거리가  현재 노드 weight + 지금 까지 최단거리보다 크면
                    if(distance[nextNode.v] > distance[current.v] + nextNode.weight){
                        distance[nextNode.v] = distance[current.v] + nextNode.weight;
                        pq.offer(new Node(nextNode.v, distance[nextNode.v]));
                    }
                }
            }
        }
    }
