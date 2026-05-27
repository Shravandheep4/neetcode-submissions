class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash_map = {}

        if len(s) != len(t):
            return False

        for i in s:
            hash_map[i] = hash_map.get(i, 0) + 1

        for i in t:
            hash_map[i] = hash_map.get(i, 0) - 1

        return not any(hash_map.values())
