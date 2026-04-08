import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class Point{
        int r;
        int c;
        public Point(int r, int c){
            this.r = r;
            this.c = c;
        }
    }
    static int n, k;
    static int maxOfMinDist = Integer.MAX_VALUE;
    static Point[] points;
    static boolean[] isVisited;
    static Point[] choose;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        if(n==k) {
            System.out.println("0");
            return;
        }
        points = new Point[n];
        isVisited = new boolean[n];
        choose = new Point[k];
        for(int i = 0; i< n; i++){
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            points[i] = new Point(r,c);
        }
        combinations(0);
        System.out.println(maxOfMinDist);
    }
    static void combinations(int depth){
        if(depth == k){
            int maxDist = calculateMin();
            if(maxDist < maxOfMinDist) maxOfMinDist = maxDist;
            return;
        }
        for(int i = 0; i< n; i++){
            if(!isVisited[i]){
                isVisited[i] = true;
                choose[depth] = points[i];
                combinations(depth+1);
                isVisited[i] = false;
            }
        }
    }

    static int calculateMin(){
        int maxDist = Integer.MIN_VALUE;
//        대피소로 지정되지 않은 좌표
        for(int i = 0; i< n; i++){
            if(!isVisited[i]){
                Point p1 = points[i];
                int nearDist = Integer.MAX_VALUE;
                for(int j= 0; j< k; j++){
                    Point p2 = choose[j];
                    nearDist = Math.min(nearDist, Math.abs(p1.c-p2.c) + Math.abs(p1.r-p2.r));
                }
                maxDist = Math.max(maxDist, nearDist);
            }
        }
        return maxDist;
    }
}