class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i,j = 0 ,0
        while(i < n and j < n) : 
            if(nums[i]!=nums[j]) : 
                nums[i+1] = nums[j] 
                i+=1
            else : 
                j+=1
            
        return i+1 
            
        