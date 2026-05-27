class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = None

        if strs != []:
            encoded_string = '__'.join(strs)

        print(encoded_string)


        return encoded_string

    def decode(self, s: str) -> List[str]:

        decoded_list = []

        if s is not None:
            decoded_list = s.split('__')

        return decoded_list
