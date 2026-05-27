class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash_map = {}

        if len(s) != len(t):
            return False

        for c in s:
            hash_map[c] = hash_map.get(c, 0) + 1

        for c in t:

            if c not in hash_map:
                return False

            hash_map[c] = hash_map[c] - 1

            if hash_map[c] == 0:
                hash_map.pop(c)

        print(hash_map)

        return len(hash_map.values()) == 0

            


        


        




        