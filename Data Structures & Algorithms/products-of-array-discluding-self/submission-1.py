class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = nums.copy()
        suffix = nums.copy()

        # Get the prefix O(N)
        for i in range(len(prefix)):

            if i == 0 : continue
            prefix[i] = prefix[i] * prefix[i-1]
            
        # Get the suffix O(N)
        for i in range(len(suffix) -1, -1, -1):

            if i == len(suffix) -1 : continue
            suffix[i] = suffix[i] * suffix[i+1]

        # Mutiply and change the initial array O(N)

        for i in range(len(nums)):
            if i == 0 :
                nums[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                nums[i] = prefix[i-1]
            else:
                nums[i] = prefix[i-1] * suffix[i + 1]

        return nums