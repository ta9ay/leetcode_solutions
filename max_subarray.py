class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_current =  max_total = nums[0]
        i = 1
        while i<=len(nums)-1:
            max_current = max(nums[i],nums[i]+max_current)
            if max_current > max_total:
                max_total = max_current
            i+=1
                
        return max_total
        