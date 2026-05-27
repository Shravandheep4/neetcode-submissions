class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)

        # Idea:
        # You can have two arrays, 
        # One that computes the product of the left sub array
        # And another that computes the product of the right sub array

        left_subarray = []
        right_subarray = []


        # O(n)
        product = 1
        for i in range(length):
            left_subarray.insert(i, product)
            product = nums[i] * product

        # O(n)
        product = 1
        for i in range(length -1, -1, -1):
            right_subarray.insert(length - i + 1, product)
            product = nums[i] * product
        right_subarray = right_subarray[::-1]

        array = []
        for i in range(length):
            value = left_subarray[i] * right_subarray[i]
            array.append(value)

        return array



        return left_subarray


            





        
        