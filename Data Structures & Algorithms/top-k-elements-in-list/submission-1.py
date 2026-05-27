class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}

        result = []

        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        for i in range(k):

            max_val = -1001
            drop_index = None

            for key, val in counter.items():

                if val > max_val:
                    max_val = val
                    drop_index = key

            counter.pop(drop_index)
            result.append(drop_index)
        
        return result



            







        

        