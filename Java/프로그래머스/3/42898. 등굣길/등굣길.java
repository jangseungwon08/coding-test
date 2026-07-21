import java.util.*;
class Solution {
    static int[][] grid;
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        grid = new int[n+1][m+1];
        grid[1][1] = 1;
        for(int i = 0; i< puddles.length; i++){
            int c = puddles[i][0];
            int r = puddles[i][1];
            grid[r][c] = -1;
        }
        for(int i = 1; i<= n; i++){
            for(int j = 1; j<=m; j++){
//                 초기값 패스
                if(i == 1 && j == 1) continue;
//                 웅덩이가 있으면 grid[i][j] 0으로바꾸고 continue;
                if(grid[i][j] == -1){
                    grid[i][j] = 0;
                    continue;
                }
//                 왼쪽값 + 위쪽 값 더하기 -> 왼쪽에서 오는 경우 + 위쪽에서 오는 경우
                grid[i][j] = (grid[i-1][j] + grid[i][j-1]) % 1000000007;
            }
        }
        return grid[n][m];
    }
}