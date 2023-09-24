import math

class Matrix:
    # constant start
    A = [
        [2, -2],
        [3, -5]
    ]
    B = [
        [-2, 0],
        [0, 3]
    ]
    C = [
        [-1, 2, 0],
        [2, 0, 3]
    ]
    E = [
        [2, -1],
        [math.pi, math.log10(2)],
        [-2, 3]
    ]
    F = [
        [1, 2, 3],
        [2, 3, 4],
        [3, 5, 7]
    ]
    I = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    # constant end

    # methods
    # 矩陣加法
    def add(a, b):
        rowLen = len(a)
        columnLen = len(a[0])
        result = []
        for rowIndex in range(rowLen):
            temp = []
            for columnIndex in range(columnLen):
                temp.append(a[rowIndex][columnIndex]+b[rowIndex][columnIndex])
            result.append(temp)
        return result

    # 矩陣減法
    def subtract(a, b):
        rowLen = len(a)
        columnLen = len(a[0])
        result = []
        for rowIndex in range(rowLen):
            temp = []
            for columnIndex in range(columnLen):
                temp.append(a[rowIndex][columnIndex]-b[rowIndex][columnIndex])
            result.append(temp)
        return result

    # 矩陣旋轉
    def transpose(a):
        rowLen = len(a)
        columnLen = len(a[0])
        result = []
        for columnIndex in range(columnLen):
            temp = []
            for rowIndex in range(rowLen):
                temp.append(a[rowIndex][columnIndex])
            result.append(temp)
        return result

    # 矩陣相乘
    def multiply(a, b):
        aMatrixRowLen = len(a)
        aMatrixColumnLen = len(a[0])
        bMatrixColumnLen = len(b[0])
        result = []
        for rowIndex in range(aMatrixRowLen):
            temp = []
            for columnIndex in range(bMatrixColumnLen):
                tempSum = 0
                for i in range(aMatrixColumnLen):
                    tempSum += a[rowIndex][i]*b[i][columnIndex]
                temp.append(tempSum)
            result.append(temp)
        return result

    # 矩陣乘數字
    def scale(a, c):
        result = []
        for row in a:
            temp = []
            for cell in row:
                temp.append(cell*c)
            result.append(temp)
        return result
            

    # 矩陣倒數 2*2
    def inverses(a):
        det = a[0][0]*a[1][1]-a[0][1]*a[1][0]
        ans = [
            [a[1][1],-a[0][1]],
            [-a[1][0],a[0][0]]
        ]
        ans = Matrix.scale(ans,1/det)
        return ans
    
    # 是否為對角矩陣
    def isDiagonal(a):
        rowLen = len(a)
        columnLen = len(a[0])
        for columnIndex in range(columnLen):
            for rowIndex in range(rowLen):
                if(rowIndex == columnIndex):
                    continue
                if(a[rowIndex][columnIndex] != 0):
                    return False
        return True
    
    # 是否為對稱矩陣
    def isSymmetric(a):
        return a == Matrix.transpose(a)
    
    # 列印矩陣
    def printMatrix(a):
        for row in a:
            print(row)

def printHeader(title):
    print("="*20,title)

def printFooter():
    print("="*20)

def questionA():
    printHeader("Question A")

    # A+3B
    ansA1 = Matrix.add(
        Matrix.A,
        Matrix.scale(Matrix.B, 3)
    )
    print("A+3B:")
    Matrix.printMatrix(ansA1)
    print()

    # C-2B*E^T
    temp = Matrix.multiply(
        Matrix.scale(Matrix.B, 2),
        Matrix.transpose(Matrix.E)
    )
    ansA2 = Matrix.subtract(Matrix.C, temp)
    print("C-2B*E^t:")
    Matrix.printMatrix(ansA2)
    print()

    # A^T
    ansA3 = Matrix.transpose(Matrix.A)
    print("A^T:")
    Matrix.printMatrix(ansA3)

    printFooter()
    print()

def questionB():
    printHeader("Question B")

    # M = A*B
    matrixM = Matrix.multiply(Matrix.A, Matrix.B)
    # N = B*A
    matrixN = Matrix.multiply(Matrix.B, Matrix.A)

    print("Matrix M:")
    Matrix.printMatrix(matrixM)
    print()
    print("Matrix N:")
    Matrix.printMatrix(matrixN)
    print()
    print("Matrix M is not equal to Matrix N.")

    printFooter()
    print()

def questionC():
    printHeader("Question C")

    # P = C^T*B^T
    matrixP = Matrix.multiply(
        Matrix.transpose(Matrix.C),
        Matrix.transpose(Matrix.B),
    )
    # Q = (B*C)^T
    matrixQ = Matrix.transpose(
        Matrix.multiply(Matrix.B, Matrix.C)
    )

    print("Matrix P:")
    Matrix.printMatrix(matrixP)
    print()
    print("Matrix Q:")
    Matrix.printMatrix(matrixQ)
    print()
    print("Matrix P is equal to Matrix Q.")

    printFooter()
    print()

def questionD():
    printHeader("Question D")

    print("Matrix A^-1:")
    # A^-1
    Matrix.printMatrix(Matrix.inverses(Matrix.A))
    print()
    print("Matrix B^-1:")
    # B^-1
    Matrix.printMatrix(Matrix.inverses(Matrix.B))

    printFooter()
    print()

def questionE():
    printHeader("Question E")

    # Matrix A
    print("Matrix A:")
    Matrix.printMatrix(Matrix.A)
    if Matrix.isDiagonal(Matrix.A):
        print("Matrix A is diagonal.")
    else:
        print("Matrix A is not diagonal.")
    print()

    # Matrix B
    print("Matrix B:")
    Matrix.printMatrix(Matrix.B)
    if Matrix.isDiagonal(Matrix.B):
        print("Matrix B is diagonal.")
    else:
        print("Matrix B is not diagonal.")
    print()

    # Matrix F
    print("Matrix F:")
    Matrix.printMatrix(Matrix.F)
    if Matrix.isDiagonal(Matrix.F):
        print("Matrix F is diagonal.")
    else:
        print("Matrix F is not diagonal.")
    print()

    # Matrix I
    print("Matrix I:")
    Matrix.printMatrix(Matrix.I)
    if Matrix.isDiagonal(Matrix.I):
        print("Matrix I is diagonal.")
    else:
        print("Matrix I is not diagonal.")

    printFooter()
    print()

def questionF():
    printHeader("Question F")

    # Matrix A
    print("Matrix A:")
    Matrix.printMatrix(Matrix.A)
    if Matrix.isSymmetric(Matrix.A):
        print("Matrix A is symmetric.")
    else:
        print("Matrix A is not symmetric.")
    print()

    # Matrix B
    print("Matrix B:")
    Matrix.printMatrix(Matrix.B)
    if Matrix.isSymmetric(Matrix.B):
        print("Matrix B is symmetric.")
    else:
        print("Matrix B is not symmetric.")
    print()

    # Matrix F
    print("Matrix F:")
    Matrix.printMatrix(Matrix.F)
    if Matrix.isSymmetric(Matrix.F):
        print("Matrix F is symmetric.")
    else:
        print("Matrix F is not symmetric.")
    print()
    
    # Matrix I
    print("Matrix I:")
    Matrix.printMatrix(Matrix.I)
    if Matrix.isSymmetric(Matrix.B):
        print("Matrix I is symmetric.")
    else:
        print("Matrix I is not symmetric.")

    printFooter()

def main():
    # 問題A
    questionA()
    # 問題B
    questionB()
    # 問題C
    questionC()
    # 問題D
    questionD()
    # 問題E
    questionE()
    # 問題F
    questionF()

main()