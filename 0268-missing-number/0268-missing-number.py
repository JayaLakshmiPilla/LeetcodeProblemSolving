class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        sum_1 = n*(n+1)/2
        sum_2 = sum(nums)
        return int(sum_1-sum_2)
        