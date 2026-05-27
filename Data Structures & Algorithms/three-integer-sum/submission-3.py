class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        # We're sorting to ensure that we don't take the same element
        # as our first element and look for the other to which will
        # lead to duplicates
        nums = sorted(nums) # O(nlogn)

        results = set()
        previous_number = None

        for i in range(len(nums) - 2):

            if nums[i] == previous_number:
                continue

            memory = set()
            for j in range(i + 1, len(nums)):

                value = nums[i] + nums[j]

                if -value in memory:
                    triplet = [nums[i], nums[j], -value]
                    triplet = tuple(triplet)

                    if triplet not in results:
                        results.add(triplet)

                memory.add(nums[j])

            previous_number = nums[i]

        return [list(x) for x in results]

               
        