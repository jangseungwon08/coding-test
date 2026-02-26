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
//        간선에 대한 가중치 없고 DFS(백트래킹)을 이용한 완전탐색은 만약 노드가 0, 100_000이면 시간초과?
//        BFS를 이용한 완전 탐색
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        subin = Integer.parseInt(st.nextToken());
        bro = Integer.parseInt(st.nextToken());
        bfs(subin);
        System.out.println(count[bro]);
    }
    static void bfs(int start){
        Queue<Integer> q = new ArrayDeque<>();
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
            for(int i = 0; i< 3; i++){
//                더하거나 뺀 값이 0 이상 10만 이하이면
                if(way[i] >= 0 && way[i] <=100_000){
//                    조건을 어떻게 줘야되지? -> count배열이랑 isVisited배열을 두개 둬서 비교
                    if(!isVisited[way[i]]){
                       if(i == 0) {
                           isVisited[way[i]] = true;
                           count[way[i]] = count[current];
                           q.offer(way[i]);
                       }
                       else {
                           isVisited[way[i]] = true;
                           count[way[i]] = count[current] +1;
                           q.offer(way[i]);
                       }
                    }
                }
              }
          }
      }
  }