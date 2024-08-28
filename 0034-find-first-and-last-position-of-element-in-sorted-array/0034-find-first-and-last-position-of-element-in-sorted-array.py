class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstPosition = -1 
        lastPosition = -1 
        for i in range(len(nums)) :
            if nums[i] == target and firstPosition == -1:
                firstPosition = i 
                lastPosition = i 
            elif nums[i] == target :
                lastPosition = i 
        return firstPosition , lastPosition

        