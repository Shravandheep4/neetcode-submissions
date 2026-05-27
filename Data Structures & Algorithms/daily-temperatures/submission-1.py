from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = deque()
        results = []

        l = 0
        r = l + 1

        while l < len(temperatures):

            current_temp = temperatures[l]
            next_temp = temperatures[r] if r < len(temperatures) else 0

            stack.append(next_temp)

            if next_temp > current_temp:
                days = len(stack)
                stack = []

                results.append(days)

                l += 1
                r = l + 1

            else:
                r += 1

            if r >= len(temperatures):
                results.append(0)
                l += 1
                r = l + 1

                stack = []

        return results
                



        