# hw1 說明文件
[toc]
## 宣告矩陣常數
把題目中的矩陣常數宣告在class Matrix裡面。
```python
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
```
## 宣告矩陣方法
### 矩陣加法
```python
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
```
兩層for遍歷所有元素，並把a陣列及b陣列中位置一樣的元素做相加。
### 矩陣減法
```python
# 矩陣加法
def add(a, b):
    rowLen = len(a)
    columnLen = len(a[0])
    result = []
    for rowIndex in range(rowLen):
        temp = []
        for columnIndex in range(columnLen):
            temp.append(a[rowIndex][columnIndex]-b[rowIndex][columnIndex])
        result.append(temp)
    return result
```
兩層for遍歷所有元素，並把a陣列及b陣列中位置一樣的元素做相減。
### 矩陣旋轉
```python
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
```
遍歷矩陣a的每一列，然後遍歷每一行，將對應位置的元素進行轉置。
### 矩陣相乘
```python
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
```
計算兩個矩陣的乘積。
### 矩陣乘數字
```python
# 矩陣乘數字
def scale(a, c):
    result = []
    for row in a:
        temp = []
        for cell in row:
            temp.append(cell*c)
        result.append(temp)
    return result
```
遍歷所有元素，並乘上c。
### 矩陣倒數 2*2
```python
# 矩陣倒數 2*2
def inverses(a):
    det = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    ans = [
        [a[1][1],-a[0][1]],
        [-a[1][0],a[0][0]]
    ]
    ans = Matrix.scale(ans,1/det)
    return ans
```
把a~11~和a~22~交換位置，a~12~和a~21~加上負號，算出行列式(det)後，呼叫Matrix.scale()乘上1/det。
### 是否為對角矩陣
```python
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
```
遍歷所有元素，當元素不在對角線上時，檢查是否不為0。
### 是否為對稱矩陣
```python
# 是否為對稱矩陣
def isSymmetric(a):
    return a == Matrix.transpose(a)
```
比較a矩陣及a^t^內容是否相等來判斷是否對稱。
### 列印矩陣
```python
# 列印矩陣
def printMatrix(a):
    for row in a:
        print(row)
```
列印所有row，特別不列印二維陣列的外層括號。
## 其他額外function
```python
def printHeader(title):
    print("="*20,title)   
```
在print答案前印出header，用於分割不同題目。
```python
def printFooter():
    print("="*20) 
```
在print答案後印出footer，用於分割不同題目。

## 程式說明
main()為程式進入點，main()中分別呼叫QuestionA()\~QuestionF()，對應題目上不同的小題。進入QuestionA()\~QuestionF()時，會先呼叫printHeader()為題目開始做分割，中間進行運算並輸出結果後，最後呼叫printFooter()為題目結束做分割。中間的運算是呼叫上面說明的矩陣方法組合出題目的式子。