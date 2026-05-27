class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:

            number_sum = numbers[l] + numbers[r]

            if number_sum > target:
                r -= 1
            elif number_sum < target:
                l += 1
            else:
                return l + 1 , r + 1
        
        return l,r


        