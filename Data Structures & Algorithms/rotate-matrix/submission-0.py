class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        rows, columns = len(matrix), len(matrix[0])
        
        # Transpose
        for i in range(rows):
            for j in range(i, columns):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        # Reverse
        for i in range(rows):
            matrix[i] = matrix[i][::-1]

        return matrix