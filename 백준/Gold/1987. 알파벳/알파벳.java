
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int r, c, maxCount;
    static char[][] arr;
    static boolean[] isVisited;
    //    상우하좌
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        arr = new char[r][c];
        isVisited = new boolean[26];
        for (int i = 0; i < r; i++) {
            String s = br.readLine();
            for (int j = 0; j < c; j++) {
                arr[i][j] = s.charAt(j);
            }
        }
        isVisited[arr[0][0] - 'A'] = true;
        backTrack(0, 0, 1);
        System.out.println(maxCount);
    }

    static void backTrack(int row, int col, int cnt) {
        if (cnt > maxCount) {
            maxCount = cnt;
        }
        for (int i = 0; i < 4; i++) {
            int nr = row + dr[i];
            int nc = col + dc[i];
            if (nr >= 0 && nr < r && nc >= 0 && nc < c) {
//                현재까지 지나온 칸의 알파벳과 달라야됨
                if (!isVisited[arr[nr][nc] - 'A']) {
                    isVisited[arr[nr][nc] - 'A'] = true;
                    backTrack(nr, nc, cnt + 1);
//                    들어갔다 나온 값 다시 remove해줘야지 다음 탐색 방해 x
                    isVisited[arr[nr][nc] - 'A'] = false;
                }
            }
        }
    }
}