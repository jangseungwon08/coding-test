import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static class Node{
        int r;
        int c;
        int cutCount;
        int dir;
        int moves;
        public Node(int r, int c, int cutCount, int dir, int moves){
            this.r = r;
            this.c = c;
            this.cutCount = cutCount;
            this.dir = dir;
            this.moves = moves;
        }
    }
    static char[][] arr;
    static boolean[][][][] isVisited;
    static int[] dr = new int[] {-1,0,1,0};
    static int[] dc = new int[] {0,1,0,-1};
    static int n, k;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(int tc = 1; tc<= t; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());
            arr = new char[n][n];
//            벨 수 있는 나무 수, 바라보는 방향
            isVisited = new boolean[n][n][k + 1][4];
            int[] startPoint = new int[2];
            int[] endPoint = new int[2];
            for (int i = 0; i < n; i++) {
                String s = br.readLine();
                for (int j = 0; j < n; j++) {
                    arr[i][j] = s.charAt(j);
                    if (arr[i][j] == 'X') {
                        startPoint[0] = i;
                        startPoint[1] = j;
                    } else if (arr[i][j] == 'Y') {
                        endPoint[0] = i;
                        endPoint[1] = j;
                    }
                }
            }
            int count = bfs(startPoint, endPoint);
            System.out.println("#" + tc + " " + count);
        }
    }
    static int bfs(int[] startPoint, int[] endPoint){
        Queue<Node> q = new ArrayDeque<>();
        q.offer(new Node(startPoint[0],startPoint[1],0, 0,0));
        isVisited[startPoint[0]][startPoint[1]][0][0] = true;
        while(!q.isEmpty()) {
            Node curr = q.poll();
            if(arr[curr.r][curr.c] == 'Y') return curr.moves;
            int nr = curr.r + dr[curr.dir];
            int nc = curr.c + dc[curr.dir];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
//                바라보는 공간이 빈 공간일 때
                if (arr[nr][nc] == 'G' || arr[nr][nc] == 'X' || arr[nr][nc] == 'Y') {
                    if (!isVisited[nr][nc][curr.cutCount][curr.dir]) {
                        isVisited[nr][nc][curr.cutCount][curr.dir] = true;
                        q.offer(new Node(nr, nc, curr.cutCount, curr.dir, curr.moves + 1));
                    }
                } else if (arr[nr][nc] == 'T') {
                    if (curr.cutCount < k && !isVisited[nr][nc][curr.cutCount + 1][curr.dir]) {
                        isVisited[nr][nc][curr.cutCount + 1][curr.dir] = true;
                        q.offer(new Node(nr, nc, curr.cutCount + 1, curr.dir, curr.moves + 1));
                    }
                }
            }
            int rightDir = (curr.dir + 1) % 4; // 0->1, 1->2, 2->3, 3->0
            if (!isVisited[curr.r][curr.c][curr.cutCount][rightDir]) {
                isVisited[curr.r][curr.c][curr.cutCount][rightDir] = true;
                q.offer(new Node(curr.r, curr.c, curr.cutCount, rightDir, curr.moves + 1));
            }

            // 4. 좌회전 (제자리에서 방향만 90도 좌회전, 이동 횟수 + 1)
            int leftDir = (curr.dir + 3) % 4; // 0->3, 1->0, 2->1, 3->2
            if (!isVisited[curr.r][curr.c][curr.cutCount][leftDir]) {
                isVisited[curr.r][curr.c][curr.cutCount][leftDir] = true;
                q.offer(new Node(curr.r, curr.c, curr.cutCount, leftDir, curr.moves + 1));
            }
        }
        return -1;
    }
}