class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = []
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        while k:
            
            max_value = -999999
            top_k = None

            for key, val in counter.items():
                if val > max_value:
                    max_value = val
                    top_k = key

            result.append(top_k)
            counter.pop(top_k)
            k -= 1
        
        return result