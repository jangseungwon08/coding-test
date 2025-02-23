import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] str = br.readLine().split(" ");
        double[] arr = new double[N];
        double max = 0, sum = 0;
        for(int i = 0; i< N; i++){
            double m = Double.parseDouble(str[i]);
            arr[i] = m;
            if (m > max){
                max = m;
            }
        }
        for(int i = 0; i< N;i++){
            arr[i] = (arr[i]/max) * 100;
            sum += arr[i];
        }
        System.out.println(sum/N);
    }
    }