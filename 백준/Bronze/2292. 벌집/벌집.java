import java.io.*;
import java.util.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int room = 1;
        int count = 1;
        while(N > room){
            room = room + (6*count);
            count++;
        }
        System.out.print(count);
    }
    }