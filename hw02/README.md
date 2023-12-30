# hw2 說明文件

- 矩陣類別
    - 取得 eigenvalue
    - 取得 eigenvector
- 多項式類別
    - 取得根
- 程式說明
    - 主要流程
    - 最終輸出結果

## 矩陣類別

### 取得 eigenvalue

在計算 eigenvalues 時，矩陣行列式會是多項式。建立完多項式後呼叫取的根的方法即可獲 eigenvalue。(計算只考慮 2\*2 矩陣)

```python
def getEigenvalues(self):
        det = Polynomial([self.matrix[0][0], -1]) * \
            Polynomial([self.matrix[1][1], -1]) - \
            Polynomial([self.matrix[0][1]*self.matrix[1][0]])
        return det.getRoots()
```

### 取得 eigenvector

傳入 eigenvalue 後，直接計算列消去的結果。特殊情況發生在非對角都為 0 時，參考[這篇](https://people.math.harvard.edu/~knill/teaching/math21b2004/exhibits/2dmatrices/index.html)文章。(計算只考慮 2*2 矩陣)

```python
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
```

## 多項式類別

### 取得根

使用公式解取得根。(計算只考慮最高二次多項式)
```python
def getRoots(self):
        d = self.coefficients[1]**2-4*self.coefficients[2]*self.coefficients[0]
        root1 = (-self.coefficients[1]+d**0.5)/(2*self.coefficients[2])
        root2 = (-self.coefficients[1]-d**0.5)/(2*self.coefficients[2])

        return [root1, root2]
```

## 程式說明

### 主要流程
宣告出 A、B、C、X 和 Z 矩陣後，對所有矩陣求 eigenvalues 和對應的 eigenvecotrs；在用比較清楚的方式印出來。
```python
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
```
### 最終輸出結果
```
========== Matrix A ==========
Eigenvalue: 7.0
Vecotr 1
1.0 
1 

Eigenvalue: -4.0
Vecotr 1
-1.2000000000000002 
1 

========== Matrix B ==========
Eigenvalue: 5.0
Vecotr 1
0.5 
1 

Eigenvalue: -1.0
Vecotr 1
-1.0 
1 

========== Matrix C ==========
Eigenvalue: 5.0
Vecotr 1
-1.0 
1 

Eigenvalue: 3.0
Vecotr 1
-0.5 
1 

========== Matrix X ==========
Eigenvalue: (1.5+0.8660254037844386j)     
Vecotr 1
(-0.5000000000000001-0.8660254037844387j) 
1 

Eigenvalue: (1.5-0.8660254037844386j)     
Vecotr 1
(-0.5000000000000001+0.8660254037844387j) 
1 

========== Matrix Z ==========
Eigenvalue: 0.0
Vecotr 1
1 
0 
Vecotr 2
0 
1 

Eigenvalue: 0.0
Vecotr 1
1
0
Vecotr 2
0
1
```
