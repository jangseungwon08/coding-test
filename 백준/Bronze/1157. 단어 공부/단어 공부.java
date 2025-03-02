import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr= new int[26];
        int max = -1;
        char c = '?';
        String str = br.readLine();
        for(int i = 0; i< str.length();i++){
            char ch = str.charAt(i);
            arr[Character.toLowerCase(ch) - 97]++;
        }
        for(int i = 0; i < arr.length; i++){
            if(arr[i] > max){
                max = arr[i];
                c = (char)(i+65);
            }
            else if(arr[i] == max) {
                c = '?';
            }
        }
        System.out.println(c);
    }
    }