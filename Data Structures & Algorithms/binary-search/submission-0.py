class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2
            element = nums[mid]

            if target > element:
                l = mid + 1
            elif target < element:
                r = mid - 1
            else:
                return mid

        return -1


