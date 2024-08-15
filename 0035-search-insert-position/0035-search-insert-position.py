class Solution:
    def binarySearch(self,low,high,nums,target,value) : 
        if low > high :
            return value
        else :
            mid = (low + high)//2
        
            if nums[mid] == target :
                return mid 
            elif nums[mid] < target :
                return self.binarySearch(mid+1,high,nums,target,value)
            elif nums[mid] > target :
                if mid < value :
                    value = mid
                    return self.binarySearch(low,mid-1,nums,target,value)

    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        value = n
        ans = self.binarySearch(0,n-1,nums,target,value)
        return ans

    
           