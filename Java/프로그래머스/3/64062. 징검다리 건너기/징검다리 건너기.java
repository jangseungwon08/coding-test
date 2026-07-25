class Solution {
    public int solution(int[] stones, int k) {
        int answer = 0;
        int left = 1;
        int right = 200000000;
        
        while(left <= right){
            int mid = (left + right) / 2;
            if(!canCross(stones, k, mid)){
                right = mid -1;
            }
            else {
                answer = mid;
                left = mid + 1;
            }
        }
        return answer;
    }
    static boolean canCross(int[] stones, int k, int mid){
//        연속으로 0이되는값이 k보다 크면 false
        int zeroCount = 0;
        for(int stone: stones){
//             음수면 건널 수 없다는 뜻
            if(stone - mid < 0){
                zeroCount++;
//                 스톤의 zero카운트가 k보다 크면 건널 수 없으므로 false
                if(zeroCount >= k){
                    return false;
                }
            }
//             돌이 깨지지 않았으면 zeroCount 다시 0(연속으로 k칸 이상 깨져야됨)
            else{
                zeroCount = 0;
            }
        }
        return true;
    }
}