class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_sequence = 0

        # Get the keys

        counter = dict()
        for i in nums:
            counter[i] = 1

        for i in nums:

            sequence = 0

            while True:
                sequence += 1

                if not counter.get(i + 1):
                    break

                i += 1
                
            max_sequence = max(sequence, max_sequence)

        return max_sequence





        