def find_pivot_binary_search(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid

    return left

nums = [4, 5, 6, 7, 0, 1, 2]
pivot_index = find_pivot_binary_search(nums)
print("Pivot Index:", pivot_index)