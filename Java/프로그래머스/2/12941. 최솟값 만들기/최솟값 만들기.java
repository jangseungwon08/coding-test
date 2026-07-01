import java.util.*;
class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        Arrays.sort(A);
        int[] reverseB = Arrays.stream(B)
            .boxed()
            .sorted((a,b) -> b -a )
            .mapToInt(Integer::intValue)
            .toArray();
        for(int i = 0 ; i < A.length; i++){
            answer += A[i] * reverseB[i];
        }
        
        return answer;
    }
}