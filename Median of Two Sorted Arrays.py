class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1 
        for i in nums2:
            nums.append(i)
        nums.sort()
        i = len(nums)
        if i%2==0:
            return ((nums[int(i/2)]+nums[int((i/2)-1)])/2)  
        else:
            return nums[int(i/2)]
        
        
#solution-2
import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1+nums2
        nums3.sort()
        median = np.median(nums3)
        return median
