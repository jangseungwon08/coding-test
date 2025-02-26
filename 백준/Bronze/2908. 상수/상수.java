import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        String str1 = st.nextToken();
        String str2 = st.nextToken();
        int num1 = Integer.parseInt(new StringBuffer(str1).reverse().toString());
        int num2 = Integer.parseInt(new StringBuffer(str2).reverse().toString());
        if(num1 > num2){
            System.out.println(num1);
        }
        else{
            System.out.println(num2);
        }
    }
    }