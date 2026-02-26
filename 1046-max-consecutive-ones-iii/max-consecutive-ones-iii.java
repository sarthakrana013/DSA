
        class Solution {
    public int longestOnes(int[] nums, int k) {
        
        int i = 0 , j = 0 , n = nums.length , ans = 0 , currSum = 0 ;

        // Edge Case
        int Zero = 0 ;
        for(int a = 0 ; a < nums.length ; a++)
        {
            if(nums[a] == 0) Zero++ ;
        }
        if(Zero < k) return nums.length ;
        while(j < n)
        {
            currSum += nums[j] ;
            if(j-i+1 - currSum > k)
            {
                currSum -= nums[i] ;
                i++ ;
            }
            else if(j-i+1 - currSum == k)
            {
                ans = Math.max(j-i+1,ans) ;
            }
            j++ ;

        }
        return ans ;
    }
}
    