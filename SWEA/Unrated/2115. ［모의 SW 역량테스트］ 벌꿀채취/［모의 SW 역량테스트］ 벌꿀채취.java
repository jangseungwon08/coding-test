import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static int[][] arr;
    static boolean[][] isVisited;
    static int n,m,c;
    static int maxVal;
    static int honey1,honey2;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(int tc = 1; tc <= t; tc++){
            StringTokenizer st = new StringTokenizer(br.readLine());
             n = Integer.parseInt(st.nextToken());
             m = Integer.parseInt(st.nextToken());
             c = Integer.parseInt(st.nextToken());
            arr = new int[n][n];
            maxVal = 0;
            isVisited = new boolean[n][n];
            for(int i = 0; i< n; i++){
                st = new StringTokenizer(br.readLine());
                for(int j = 0; j< n; j++){
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            List<Integer> visited = new ArrayList<>();
            backTracking(0,visited);
            System.out.println("#" + tc + " "  + maxVal);
        }
    }
    static void backTracking(int depth, List<Integer> visited){
//        조합 조건 => m개의 연속된 벌통 2개 뽑았으면 조합 실행
        if(depth == 2){
            List<Integer> subList1 = visited.subList(0,m);
            honey1 = 0;
            combinations(subList1, 0, 0,0);
            int pro1 = honey1;

            List<Integer> subList2 = visited.subList(m,m*2);
            honey1 = 0;
            combinations(subList2, 0, 0,0);
            int pro2 = honey1;
            if(pro1 + pro2 > maxVal){
                maxVal = pro1 + pro2;
            }
            return;
        }
        for(int i = 0; i< n; i++){
            for(int j = 0; j<= n-m; j++){
                boolean canSelect = true;
                for(int k = 0; k < m; k++){
                    if (isVisited[i][j + k]) {
                        canSelect = false;
                        break;
                    }
                }
//                뽑았으면
                if(canSelect) {
//                    통쨰로 visited배열에 담아주기
                    for (int k = 0; k < m; k++) {
                        isVisited[i][j + k] = true;
                        visited.add(arr[i][j + k]);
                    }
                    backTracking(depth + 1, visited);
                    for (int k = 0; k < m; k++) {
                        isVisited[i][j + k] = false;
                        visited.remove(visited.size() - 1);
                    }
                }
            }
        }
    }
//    뽑은 것들 중에서 부분집합
    static void combinations(List<Integer> visited, int depth, int val, int profit){
        if(profit > c) return;
//        다 뽑았으면
        if(depth == visited.size()){
            if(honey1 < val){
                honey1 = val;
            }
            return;
        }
//        뽑는 경우 / 안뽑는 경우
        combinations(visited, depth+1,val + (visited.get(depth) * visited.get(depth)), profit + visited.get(depth));
        combinations(visited, depth+1, val, profit);
    }
}
