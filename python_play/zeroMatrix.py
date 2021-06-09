import unittest

def zero_matrix(matrix):
    nRows = len(matrix)
    mCols = len(matrix[0])
    rows = []
    cols = []
    for r in range(nRows):
        for c in range(mCols):
            if matrix[r][c] == 0:
                rows.append(r)
                cols.append(c)
    
    for row in rows:
        markRowZero(matrix,row)
    for col in cols:
        markColumnZero(matrix,col)

    return matrix

def markRowZero(mat,row):
    for i in range(len(mat)):
        mat[row][i] = 0    

def markColumnZero(mat,col):
    for i in range(len(mat[0])):
        mat[i][col] = 0
    

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()







   


