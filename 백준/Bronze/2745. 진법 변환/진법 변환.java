import java.io.*;
import java.util.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String str = st.nextToken();
        int num = Integer.parseInt(st.nextToken());
        int sum = 0;
        int idx = 0;
        for(int i = str.length()-1; i>= 0;i --){
            char c = str.charAt(i);
            if('A' <= c && c <= 'Z'){
                sum += (c-'A' + 10) * Math.pow(num,idx);
                idx++;
            }
            else{
                sum += (c-'0') * Math.pow(num,idx);
                idx++;
            }
        }
        System.out.println(sum);
    }
    }