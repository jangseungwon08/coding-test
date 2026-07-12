import java.util.*;

class Solution {
     public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;

        boolean[][] adjList = new boolean[n+1][n+1];
        for(int[] wire: wires){
            int u = wire[0];
            int v = wire[1];
            adjList[u][v] = true;
            adjList[v][u] = true;
        }

        for(int[] wire: wires){
            int u = wire[0];
            int v = wire[1];
            adjList[u][v] = false;
            adjList[v][u] = false;
            boolean[] isVisited = new boolean[n+1];
            isVisited[u] =  true;
            int count = dfs(n, u, adjList, isVisited);
            int dif =  Math.abs(count - (n-count));
            answer = Math.min(dif, answer);
            adjList[u][v] = true;
            adjList[v][u] = true;
        }
        return answer;
    }
    public int dfs(int n, int start, boolean[][]graph, boolean[] isVisited){
        int count = 1;
        for(int i = 1; i<= n; i++){
            if(graph[start][i] && !isVisited[i]){
                isVisited[i] = true;
                count += dfs(n, i, graph, isVisited);
            }
        }
        return count;
    }
}