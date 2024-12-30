class Solution(object):
    def find_pivot_binary_search(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = self.find_pivot_binary_search(nums)
        if target >= nums[pivot] and target <= nums[-1]:
            left, right = pivot, len(nums) - 1
        else:
            left, right = 0, pivot - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
