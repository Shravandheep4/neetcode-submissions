import math

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        
        for i in range(k):

            largest_number = nums[i]
            swap_index = i

            for j in range(i + 1, len(nums)):

                number = nums[j]

                if number > largest_number:
                    largest_number = number
                    swap_index = j

            temp = nums[i]
            nums[i] = nums[swap_index]
            nums[swap_index] = temp

        return nums[k - 1]
                
            


                

        