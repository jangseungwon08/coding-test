import java.util.*;
class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] dp = new int[n+1][m+1];
        dp[1][1] = 1;
        for(int[] puddle: puddles){
            int r = puddle[1];
            int c = puddle[0];
            dp[r][c] = -1;
        }
        
        for(int i = 1; i<=n; i++){
            for(int j = 1; j<=m; j++){
                if(i == 1 && j == 1) continue;
                
                if(dp[i][j] == -1){
                    dp[i][j] = 0;
                    continue;
                }
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007;
            }
        }
        return dp[n][m];
    }
}