class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n 
        for i in range((n-k)//2) : 
            temp = nums[i] 
            nums[i] = nums[n-k-i-1]
            nums[n-k-i-1] = temp
        low = n-k 
        high = n-1 
        while(low<high) : 
            temp = nums[low] 
            nums[low] = nums[high]
            nums[high] = temp   
            low+= 1
            high -= 1
       
        low = 0 
        high = n-1 
        while(low<high) : 
            temp = nums[low] 
            nums[low] = nums[high]
            nums[high] = temp   
            low+= 1
            high -= 1
    
       
        
                
                


        

                
                


        
        