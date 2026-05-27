class Solution:

    @staticmethod
    def check_consistency(array):
        array = [x for x in array if x.isnumeric()]
        return len(array) == len(set(array))

    @staticmethod
    def get_subbox_values(board, subbox : tuple):

        r = subbox[0] * 3
        c = subbox[1] * 3

        values = []

        for i in range(r, r + 3):
            for j in range(c, c + 3):
                values.append(board[i][j])

        return values

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check row consistency
        for r in range(len(board)):

            values = [board[r][c] for c in range(len(board))]
            is_consistent = self.check_consistency(values)

            if not is_consistent:
                return False

        # Check column consistency
        for c in range(len(board)):
            values = [board[r][c] for r in range(len(board))]

            is_consistent = self.check_consistency(values)

            if not is_consistent:
                return False


        # Check subbox consistency

        for i in [0, 1, 2]:
            for j in [0, 1, 2]:

                values = self.get_subbox_values(board, (i,j))
                is_consistent = self.check_consistency(values)

                if not is_consistent:
                    return False

        return True
        