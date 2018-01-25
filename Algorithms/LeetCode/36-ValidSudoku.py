'''
Question 36. Valid Sudoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''

'''
Resources : 
    1.https://discuss.leetcode.com/topic/20016/1-7-lines-python-4-solutions
'''

'''
Solution : 
    1. Brute Force : 
        - Time Complexity : O(row^2 * col^2 * max(row,col))
    2. HashMap : 
        - Time Complexity : O(row * col)
'''
def isValidSudoku_1(self, board):
    seen = []
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c != '.':
                seen += [(c, j), (i, c), (i / 3, j / 3, c)]

    print(seen)
    return len(seen) == len(set(seen))

def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    from collections import defaultdict
    row_vals = defaultdict(set)
    col_vals = defaultdict(set)
    quad_vals = defaultdict(set)

    for row in xrange(len(board)):
        for col in xrange(len(board[0])):
            char = board[row][col]
            if char == '.':
                continue

            quad = (row / 3) * 3 + (col / 3)

            if char in row_vals[row] or char in col_vals[col] or char in quad_vals[quad]:
                return False

            row_vals[row].add(char)
            col_vals[col].add(char)
            quad_vals[quad].add(char)

    return True