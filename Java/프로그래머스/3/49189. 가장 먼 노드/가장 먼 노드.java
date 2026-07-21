import java.util.*;

class Solution {
    static List<List<Integer>> adjList = new ArrayList<>();
    static boolean[] isVisited;
    static int[] nodeCount;
    static int maxCount = 0;
    public int solution(int n, int[][] edge) {
        int answer = 0;
        for(int i = 0; i<= n; i++){
            adjList.add(new ArrayList<>());
        }
        isVisited = new boolean[n+1];
        nodeCount = new int[n+1];
        for(int i = 0; i< edge.length; i++){
            int from = edge[i][0];
            int to = edge[i][1];
            adjList.get(from).add(to);
            adjList.get(to).add(from);
        }
        bfs(1);
        for(int i = 1; i<= n; i++){
            if(maxCount == nodeCount[i]) answer++;
        }
        return answer;
    }
    static void bfs(int start){
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(start);
        isVisited[start] = true;
        while(!q.isEmpty()){
            int now = q.poll();
            List<Integer> nextNodeList = adjList.get(now);
            for(int i = 0; i< nextNodeList.size(); i++){
                int next = nextNodeList.get(i);
//                 방문하지 않은 곳
                if(!isVisited[next]){
                    q.offer(next);
                    isVisited[next] = true;
                    nodeCount[next] = nodeCount[now] + 1;
                    maxCount = Math.max(nodeCount[now]+1, maxCount);
                }
            }
        }
    }
}