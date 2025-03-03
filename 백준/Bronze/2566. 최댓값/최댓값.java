import java.io.*;
import java.util.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        int max = -1;
        int row = 0;
        int col = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int i = 0; i < 9 ; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j< 9; j++){
                int num = Integer.parseInt(st.nextToken());
                if(num > max){
                    max = num;
                    row = i+1;
                    col = j+1;
                }
            }
        }
        System.out.println(max);
        System.out.print(row + " " + col);
    }
    }