class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers) 
        i,j=0,n-1
        while(i<j):
            su=numbers[i]+numbers[j]  
            if(su>target):
                j-=1
            elif(su<target):
                i+=1
            else: 
                return[i+1,j+1]