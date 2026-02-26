import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;

public class Main {
    static boolean[] isVisited = new boolean[100001];
    static int subin, bro;
    static int[] count;
    public static void main(String[] args) throws IOException {
//        DFS(백트래킹)을 이용한 완전탐색은 만약 노드가 0, 100_000이면 시간초과?
//        BFS를 이용한 완전 탐색
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        subin = Integer.parseInt(st.nextToken());
        bro = Integer.parseInt(st.nextToken());
        bfs(subin);
        System.out.println(count[bro]);
    }
    static void bfs(int start){
        Deque<Integer> q = new ArrayDeque<>();
        q.offer(start);
        count = new int[100_001];
        isVisited[start] = true;
        int[] way = new int[3];
        while(!q.isEmpty()){
//            세 갈래가 필요하기 때문에 3개의 배열을 저장하는 way변수
            int current = q.poll();
            if(current == bro){
                break;
            }
            way[0] = current*2;
            way[1] = current-1;
            way[2] = current+1;
//            *2일때 우선순위 1
            if(way[0] >= 0 && way[0] <=100_000 && !isVisited[way[0]]){
                q.addFirst(way[0]);
                isVisited[way[0]] = true;
                count[way[0]] = count[current];
            }
//            -1일때 우선순위 2
            if(way[1] >= 0 && way[1] <=100_000 && !isVisited[way[1]]){
                q.addLast(way[1]);
                isVisited[way[1]] = true;
                count[way[1]] = count[current] + 1;
            }
            if(way[2] >= 0 && way[2] <=100_000 && !isVisited[way[2]]){
                q.addLast(way[2]);
                isVisited[way[2]] = true;
                count[way[2]] = count[current] + 1;
            }
        }
    }
    }