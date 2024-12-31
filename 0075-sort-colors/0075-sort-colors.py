class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_arr = [0]*3
        for i in nums :
            count_arr[i] += 1 
        j=0 
        l =0
        for i in count_arr :
            for k in range(i) :
                nums[l] = j  
                l= l+1 
            j += 1
        return nums


        