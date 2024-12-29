class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int 
        """
        if nums:
            start, end = 0, len(nums) - 1
            while start < end:
                mid = start + (end - start) // 2
                if nums[mid] < nums[mid + 1]:
                    start = mid + 1
                else:
                    end = mid
            return start
        return -1
