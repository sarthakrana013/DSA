class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a,b,c=0,1,1
        n=len(nums)
        while(c<n):
            if(nums[a]==nums[c]):
                c=c+1
                continue
            
            else:
                b=b+1
                a=a+1
                nums[a]=nums[c]
                c=c+1
        
        return b