import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = dict()

        for i in nums:
            counter[i] = counter.get(i, 0) + 1


        values = []

        while k:

            max_count = -1
            key = None

            for v,c in counter.items():
                
                if c > max_count:
                    max_count = c
                    key = v
            
            values.append(key)
            counter.pop(key)
            
            k -= 1

        return values
            




        