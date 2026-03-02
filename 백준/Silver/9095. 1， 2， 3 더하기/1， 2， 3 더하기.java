import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static int count;
    static int[] nums = {1,2,3};
    static int[] target;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(int i = 0; i< t; i++){
            n = Integer.parseInt(br.readLine());
            count = 0;
//            1개 뽑는 경우 2개 뽑는 경우 3개 뽑는 경우
            for(int j = 1; j<=n; j++){
//                target는 뽑는 경우의 수 배열
                target = new int[j];
                permutations(0);
            }
            System.out.println(count);
        }
    }
    static void permutations(int numCount){
//        target길이만큼 다 뽑았으면
        if(numCount == target.length){
         int sum = 0;
         for(int i = 0; i< target.length;i++){
             sum += target[i];
         }
         if(sum == n){
             count++;
         }
             return;
        }
//        target numCount번째 idx에 num값 하나 저장
        for(int i = 0; i < nums.length; i++){
            target[numCount] = nums[i];
//            한개 뽑았으니 numCount 1 증가
            permutations(numCount+1);
        }
    }
}