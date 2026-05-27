class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashset = {}

        for num in nums:

            is_present = hashset.get(num, False)

            if is_present:
                return True

            hashset[num] = 1
        
        return False