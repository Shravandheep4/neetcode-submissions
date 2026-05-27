class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ASCII_VALUE_START = 97

        group = {}

        for word in strs:

            key = [0] * 26
            
            for letter in word:
                index = ord(letter) - ASCII_VALUE_START
                key[index] = key[index] + 1

            key = tuple(key)

            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]

        return group.values()

        





        