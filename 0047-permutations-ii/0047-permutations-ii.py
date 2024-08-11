class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations 
        perm=permutations(nums)
        set_a=set(perm)
        list_a=list(set_a)
        return list_a
       