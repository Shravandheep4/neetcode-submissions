class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for idx, val in enumerate(nums):

            required_number = target - val

            if required_number in hashmap:
                return [hashmap[required_number], idx]

            hashmap[val] = idx
        
        return None
        