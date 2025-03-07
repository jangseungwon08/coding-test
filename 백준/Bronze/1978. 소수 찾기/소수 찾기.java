import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int count = 0;
        while(st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());
            if (isPrime(num)) {
                count++;
            }
        }
        System.out.print(count);
    }

    private static boolean isPrime(int num){
        if(num < 2) return false;
        for(int i = 2; i<=Math.sqrt(num); i++){
            if(num % i == 0) return false;
        }
        return true;
    }
}
