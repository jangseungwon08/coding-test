import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        int[] arr = new int[26];
        Arrays.fill(arr,-1);
        for(int i =0; i< S.length();i++) {
            char ch = S.charAt(i);
            if(arr[ch -97] == -1) {
                arr[ch - 97] = i;
            }
        }
        for(int j = 0; j< arr.length; j++){
            System.out.print(arr[j] + " ");
        }
    }
    }