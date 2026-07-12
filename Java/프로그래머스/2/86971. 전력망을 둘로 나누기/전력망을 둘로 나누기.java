import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        boolean[][] graph = new boolean[n+1][n+1];
//         연결리스트 만들어서 true면 연결되어있다고 한다.
        for(int i = 0; i < wires.length; i++){
            int[] wire = wires[i];
            int u = wire[0];
            int v = wire[1];
            graph[u][v] = true;
            graph[v][u] = true;
        }
//      한개씩 끊어봄 -> 후 BFS
        for(int i = 0; i< wires.length; i++){
            int[] wire = wires[i];
            int u = wire[0];
            int v = wire[1];
            graph[u][v] = false;
            graph[v][u] = false;
            int count = bfs(n, u, graph);
            int diff = Math.abs(count - (n-count));
            answer = Math.min(answer, diff);
            graph[u][v] = true;
            graph[v][u] = true;
        }
        
        return answer;
    }
    static int bfs(int n, int start, boolean[][] graph){
        Queue<Integer> q = new ArrayDeque<>();
        boolean[] isVisited = new boolean[n+1];
        int count = 1;
        
        q.offer(start);
        isVisited[start] = true;
        while(!q.isEmpty()){
            int curr = q.poll();
            for(int i = 1; i<= n; i++){
//                 해당 노드와 연결되어있고 방문하지 않으면 연결된 것으로 판점
                if(graph[curr][i] && !isVisited[i]){
                    q.offer(i);
                    isVisited[i] = true;
                    count++;
                }
            }
        }
        return count;
    }
    
}