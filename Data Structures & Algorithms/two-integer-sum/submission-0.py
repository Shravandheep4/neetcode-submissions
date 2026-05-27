class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i in range(len(nums)):

            value = nums[i]
            complement = target - value

            index_2 = hash_map.get(complement)

            if index_2 is not None:
                return [index_2, i]
            
            hash_map[value] = i

        print(hash_map)
        
        return []