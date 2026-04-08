class Solution {
    public String solution(String s) {
        String[] res = s.split(" ");
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for(int i = 0; i< res.length; i++){
            int num = Integer.parseInt(res[i]);
            max = Math.max(max, num);
            min = Math.min(min, num);
        }
        String answer = "";
        answer += min + " ";
        answer += max;
        return answer;
    }
}