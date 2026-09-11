import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int getAllPocketmons = nums.length / 2;
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i< nums.length; i++){
            set.add(nums[i]);
        }
        return set.size() > getAllPocketmons ? getAllPocketmons : set.size();
    }
}