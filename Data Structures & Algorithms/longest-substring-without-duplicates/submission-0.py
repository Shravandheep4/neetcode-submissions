class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        
        hash_map = {}
        
        max_length = 0
        length = 0

        while r < len(s):

            starting_character = s[l]
            current_character = s[r]

            if current_character in hash_map:
                l += 1
                length -= 1
                hash_map.pop(starting_character)

            else:
                r += 1
                length += 1
                hash_map[current_character] = 1

            max_length = max(length, max_length)

        return max_length
            

            

            

