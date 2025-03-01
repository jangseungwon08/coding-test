import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        /*
        int[] chess = {1, 1, 2, 2, 2, 8};
        int[] ans = new int[6];
        String[] str = br.readLine().split(" ");
        for(int i = 0; i< str.length;i++){
            int n = Integer.parseInt(str[i]);
            ans[i] = chess[i] - n;
        }
        for(int i = 0; i< ans.length;i++){
            System.out.print(ans[i] + " ");
        }
         */
        int king = 1;
        int queen = 1;
        int look = 2;
        int bishop = 2;
        int knight = 2;
        int pawn = 8;

        StringTokenizer st = new StringTokenizer(br.readLine());
        king = king - Integer.parseInt(st.nextToken());
        queen = queen - Integer.parseInt(st.nextToken());
        look = look - Integer.parseInt(st.nextToken());
        bishop = bishop - Integer.parseInt(st.nextToken());
        knight = knight - Integer.parseInt(st.nextToken());
        pawn = pawn - Integer.parseInt(st.nextToken());

        System.out.print(king + " ");
        System.out.print(queen + " ");
        System.out.print(look + " ");
        System.out.print(bishop + " ");
        System.out.print(knight + " ");
        System.out.print(pawn + " ");
    }
    }