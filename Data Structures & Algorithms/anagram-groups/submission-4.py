class Solution:

    def customhash(self, value):
        ASCII_VALUE_START = 97
        key = [0] * 26

        for v in value:
            index = ord(v) - ASCII_VALUE_START
            key[index] = key[index] + 1

        key = tuple(key)

        return key

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}

        for word in strs:

            hashedword = self.customhash(word)

            if hashedword in group:
                group[hashedword].append(word)
            else:
                group[hashedword] = [word]

        return list(group.values())

        





        