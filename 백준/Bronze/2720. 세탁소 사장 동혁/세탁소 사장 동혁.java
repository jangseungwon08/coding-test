import java.io.*;
import java.util.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int [][] arr = new int[T][4];
        for(int i = 0; i< T; i++) {
            int num = Integer.parseInt(br.readLine());
            int Quarter = num / 25;
            num %= 25;
            int Dime = num / 10;
            num %= 10;
            int Nickel = num / 5;
            num %= 5;
            int Penny = num;
            System.out.print(Quarter + " " + Dime + " " + Nickel + " " + Penny + " ");
            System.out.println();
        }
    }
    }