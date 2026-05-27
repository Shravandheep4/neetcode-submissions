class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # form a vector of size 26 that counts the occurance of an alphabet
        # Two words having the same set of alphabets()

        grouped_hash_map = defaultdict(list)
        
        for word in strs:

            vector = [0 for x in range(26)]

            for x in word:
                bit = ord('z') - ord(x)
                vector[bit] = vector[bit] + 1

            vector = tuple(vector)
            grouped_hash_map[vector].append(word)

        return [x for x in grouped_hash_map.values()]
    
    