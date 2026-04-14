class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        r=[0]*n
        left=0
        right=n-1
        for i in range(n-1,-1,-1):
            if abs(nums[left])>=abs(nums[right]) :
                r[n-1]=nums[left]**2
                n=n-1
                left=left+1
            else:
                r[n-1]=nums[right]**2
                n=n-1
                right=right-1
        return r

