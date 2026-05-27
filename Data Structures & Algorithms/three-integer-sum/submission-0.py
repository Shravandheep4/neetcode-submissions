class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        results = set()

        for i in range(len(nums)):

            memory = set()

            for j in range(i + 1, len(nums)):

                value = nums[i] + nums[j]

                if -value in memory:
                    triplet = sorted([nums[i], nums[j], -value])
                    triplet = tuple(triplet)

                    if triplet not in results:
                        results.add(triplet)

                memory.add(nums[j])


        return [list(x) for x in results]

               
        