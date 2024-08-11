class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        n = len(nums)
        for  i in range(n) :
            if nums[i] == val :
                pass 
            else :
                nums[k] = nums[i] 
                k = k+1   
        return k

