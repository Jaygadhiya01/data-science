# Lecture 1 – NumPy Basics  

##  Learning Objectives  

-  Understand what NumPy is and why it is important.  
-  Differentiate between Python lists and NumPy arrays.  
-  Create and manipulate NumPy arrays.  
-  Perform basic operations with NumPy.  
-  Explore array attributes (shape, size, dtype).  

---

## 1. What is NumPy?  

**NumPy = Numerical Python**  
     
- A Python library used for **numerical & scientific computing**.  
- Provides **multi-dimensional array objects** and tools to work with them.  

###  Why NumPy?  
- Faster than Python lists.  
- Uses less memory.  
- Provides vectorization (operations without loops).  
- Supports mathematical, logical, and statistical operations.  
- Foundation for **Data Science, Machine Learning, Deep Learning, Scientific Research**.  

---

## 2. Difference: Python List vs NumPy Array  

| Feature     | Python List         | NumPy Array            |
|-------------|---------------------|-------------------------|
| Data Type   | Can store mixed data| Stores data of same type|
| Speed       | Slower              | Much faster             |
| Memory      | Takes more memory   | Takes less memory       |
| Operations  | Requires loops      | Vectorized operations   |

---

## 3. Importing NumPy  

```python
import numpy as np
```

---

## 4. Creating NumPy Arrays  

### From Python List  
```python
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

### Multi-Dimensional Arrays  
```python
arr2d = np.array([[1,2,3], [4,5,6]])
arr3d = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
```

---

## 5. Array Attributes  

```python
print(arr.ndim)   # Dimension of array
print(arr.shape)  # Rows & columns
print(arr.size)   # Total elements
print(arr.dtype)  # Data type
```

---

## 6. Special Arrays  

```python
np.zeros(5)         # Array of zeros
np.ones((2,3))      # Array of ones
np.arange(1, 10, 2) # Array from 1 to 9 with step 2
np.linspace(0, 1, 5)# 5 values between 0 and 1
np.eye(3)           # Identity matrix (3x3)
```

---

## 7. Basic Operations  

```python
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print(a + b)  # Element-wise addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a ** 2) # Power
```

---

## 8. Indexing & Slicing  

### 1D Array  
```python
arr = np.array([10,20,30,40,50])

print(arr[0])     # First element
print(arr[-1])    # Last element
print(arr[1:4])   # Slice from index 1 to 3
print(arr[:3])    # First 3 elements
print(arr[::2])   # Every 2nd element
```

### 2D Array  
```python
arr2d = np.array([[1,2,3], [4,5,6]])

print(arr2d[0,1])   # Element at row 0, col 1 → 2
print(arr2d[:,1])   # All rows, column 1 → [2,5]
print(arr2d[1,:])   # Entire row 1 → [4,5,6]
```

---

## 9. Useful Functions  

```python
arr = np.array([1,2,3,4,5])

print(np.min(arr))   # Minimum
print(np.max(arr))   # Maximum
print(np.sum(arr))   # Sum
print(np.mean(arr))  # Average
print(np.std(arr))   # Standard deviation
```
