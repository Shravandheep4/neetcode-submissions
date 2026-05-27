import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = dict()
        heap = []


        # Get the value and it's corresponding count
        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        # Push the values along with the count to a max heap
        for v,c in counter.items():
            heapq.heappush(heap, (-c, v))
        
        # Keep popping elements from heap K times
        values = []

        while k:
            count, key = heapq.heappop(heap)
            values.append(key)
            k -= 1

        return values
            




        