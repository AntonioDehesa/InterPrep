"""
Wrtie an algorith such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""
def zeroMatrix(matrix):
    for row in range(len(matrix)):
        for element in range(len(matrix[row])):
            if matrix[row][element] == 0:
                for i in range(len(matrix)):
                    matrix[i][element] = 0
                for i in range(len(matrix[0])):
                    matrix[row][i] = 0
                return matrix

if __name__ == "__main__":
    matrix = [[1,2,3,4]
            ,[5,6,0,8]
            ,[9,10,11,12]]
    result = zeroMatrix(matrix)
    for row in result:
        print(row)