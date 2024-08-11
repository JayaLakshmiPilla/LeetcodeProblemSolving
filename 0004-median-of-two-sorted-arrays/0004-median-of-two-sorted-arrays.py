class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_list=nums1+nums2 
        merge_list.sort()
        l=len(merge_list)
        if l%2!=0 :
            median=float(merge_list[(l//2)])
            return median
        elif l%2==0 :
            median=float((merge_list[l//2]+merge_list[(l//2)-1])/2)
            return median
        

