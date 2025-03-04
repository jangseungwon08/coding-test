import java.io.*;
import java.util.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int point = 2;
        int increase = 1;
        for(int i = 0; i< N; i++){
            point += increase;
            increase *= 2;
        }
        System.out.print((int)Math.pow(point,2));
    }
    }