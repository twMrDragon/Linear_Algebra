class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __mul__(self, other):
        n = len(self.coefficients)
        m = len(other.coefficients)
        temp = [0]*(n+m-1)
        for i in range(n):
            for j in range(m):
                temp[i+j] += self.coefficients[i]*other.coefficients[j]
        return Polynomial(temp)

    def __sub__(self, other):
        n = len(self.coefficients)
        m = len(other.coefficients)
        temp = [0]*max(n, m)
        for i in range(n):
            temp[i] = self.coefficients[i]
        for i in range(m):
            temp[i] -= other.coefficients[i]
        return Polynomial(temp)

    def getRoots(self):
        d = self.coefficients[1]**2-4*self.coefficients[2]*self.coefficients[0]
        root1 = (-self.coefficients[1]+d**0.5)/(2*self.coefficients[2])
        root2 = (-self.coefficients[1]-d**0.5)/(2*self.coefficients[2])

        return [root1, root2]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def getEigenvalues(self):
        det = Polynomial([self.matrix[0][0], -1]) * \
            Polynomial([self.matrix[1][1], -1]) - \
            Polynomial([self.matrix[0][1]*self.matrix[1][0]])
        return det.getRoots()

    def getEigenVectors(self, eigenvalue):
        if self.matrix[1][0] == 0 and self.matrix[0][1] == 0:
            return [Matrix([[1], [0]]), Matrix([[0], [1]])]

        tempMatrix = [row.copy() for row in self.matrix]
        tempMatrix[0][0] -= eigenvalue
        tempMatrix[1][1] -= eigenvalue

        scale = tempMatrix[0][0]/tempMatrix[1][0]
        tempMatrix[1][0] -= scale*tempMatrix[0][0]
        tempMatrix[1][1] -= scale*tempMatrix[0][1]

        scale = 1/tempMatrix[0][0]
        tempMatrix[0][0] *= scale
        tempMatrix[0][1] *= scale

        return [Matrix([[-tempMatrix[0][1]], [1]])]

    def __str__(self):
        result = ""
        for row in self.matrix:
            for cell in row:
                result += (str(cell)+" ")
            result += "\n"
        return result[:-1]


def main():
    A = Matrix([[1, 6], [5, 2]])
    B = Matrix([[1, 2], [4, 3]])
    C = Matrix([[7, 2], [-4, 1]])
    X = Matrix([[2, 1], [-1, 1]])
    Z = Matrix([[0, 0], [0, 0]])

    matrixName = ["A", "B", "C", "X", "Z"]
    matries = [A, B, C, X, Z]

    for name, matrix in zip(matrixName, matries):
        print("="*10, f"Matrix {name}", "="*10)
        eigenvalues = matrix.getEigenvalues()
        for eigenvalue in eigenvalues:
            print(f"Eigenvalue: {eigenvalue}")
            eigenvectors = matrix.getEigenVectors(eigenvalue)
            for index, eigenvector in enumerate(eigenvectors):
                print(f"Vecotr {index+1}")
                print(eigenvector)
            print()


main()
