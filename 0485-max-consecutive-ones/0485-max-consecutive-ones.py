class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums) 
        length = 0 
        maxi = 0
        for i in range(n) : 
            if nums[i] == 1 :
                length += 1 
            else : 
                length = 0 
            maxi = max(maxi,length)
        return maxi
        