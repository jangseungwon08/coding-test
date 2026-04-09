class Solution {
    public int solution(int n) {
        int answer = 0;
        int nextN = n;
//         비트 수 세기
        int nCount = Integer.bitCount(n);
        while(true){
//             조건 1
            nextN++;
//             조건 2
            int nextNCount = Integer.bitCount(nextN);
            if(nextNCount == nCount) break;   
        }
        return nextN;
    }
}