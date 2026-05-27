class Solution:

    def encode(self, strs: List[str]) -> str:


        if strs == []:
            return '\t'

        encoded_string = '\t'.join(strs)
        
        return encoded_string

    def decode(self, s: str) -> List[str]:

        if s == '\t':
            return []

        decoded_list = s.split('\t')
        return decoded_list

