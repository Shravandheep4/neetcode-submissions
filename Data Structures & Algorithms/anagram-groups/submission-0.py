class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_of_hashmaps = {}

        for s in strs:

            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord('a')] += 1

            key = tuple(char_count)

            if hash_of_hashmaps.get(key):
                hash_of_hashmaps[key].append(s)
            else:
                hash_of_hashmaps[key] = [s]

        result = []
        for k,v in hash_of_hashmaps.items():
            result.append(v)

        return result
        
        



        
        