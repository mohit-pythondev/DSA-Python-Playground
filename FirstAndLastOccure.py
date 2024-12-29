class Solution(object):
    def firstOccurence(self, nums, target):
        try:
            start =0
            end = len(nums) - 1
            ans = -1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    ans = mid
                    end = mid - 1
                if  nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return ans            
        except:
            return -1
    
    def lastOccurence(self, nums, target):
        try:
            start = 0
            end = len(nums) - 1
            ans = -1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    ans = mid
                    start = mid + 1 
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return ans           
        except:
            return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.firstOccurence(nums,target),self.lastOccurence(nums,target)]

new = Solution()
print(new.searchRange([5,7,7,8,8,10],8))