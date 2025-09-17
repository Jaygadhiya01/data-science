NumPy Methods – Notes
q-1what is numpy ?
NumPy is a fundamental Python library for numerical computing. Its name stands for Numerical Python. It’s widely used in data science, machine learning, scientific computing, and engineering because it makes working with large datasets and mathematical operations fast and easy.


Q-2Why not just Python lists?
NumPy arrays take less memory
Faster operations
Lots of built-in mathematical functions


1. Array Creation

np.array() → Create array from list/tuple.
np.zeros(shape) → Array of zeros.
np.ones(shape) → Array of ones.
np.empty(shape) → Uninitialized array.
np.full(shape, value) → Array filled with given value.
np.arange(start, stop, step) → Range array.
np.linspace(start, stop, num) → Evenly spaced numbers.
np.logspace(start, stop, num) → Logarithmically spaced numbers.
np.identity(n) / np.eye(n, m) → Identity matrix.
np.random.rand() / np.random.randn() → Random arrays.
np.random.randint(low, high, size) → Random integers.

2. Array Inspection

arr.shape → Dimensions.
arr.ndim → Number of dimensions.
arr.size → Total elements.
arr.dtype → Data type.
arr.itemsize → Bytes per element.

3. Array Manipulation

np.reshape(arr, newshape) → Reshape array.
arr.flatten() → Flatten to 1D.
np.ravel(arr) → Flatten (view if possible).
np.transpose(arr) / arr.T → Transpose.
np.concatenate([a, b], axis=0) → Join arrays.
np.stack() / np.vstack() / np.hstack() → Stack arrays.
np.split(arr, sections) → Split into sub-arrays.
np.expand_dims(arr, axis) → Add dimension.
np.squeeze(arr) → Remove dimensions of size 1.

4. Indexing & Slicing

Standard Python slicing arr[1:5].
Boolean indexing arr[arr > 5].
Fancy indexing arr[[1, 3, 5]].

5. Mathematical Operations

Arithmetic: +, -, *, /, //, %, **.
np.add(), np.subtract(), np.multiply(), np.divide().
np.exp(), np.log(), np.log10().
np.sqrt(), np.power().
Trigonometry: np.sin(), np.cos(), np.tan(), np.arcsin(), etc.
Rounding: np.round(), np.floor(), np.ceil().

6. Statistics & Aggregations

np.sum(arr) → Sum.
np.mean(arr) → Mean.
np.median(arr) → Median.
np.std(arr) → Standard deviation.
np.var(arr) → Variance.
np.min(arr) / np.max(arr).
np.argmin(arr) / np.argmax(arr).
np.percentile(arr, q).
np.corrcoef(arr) → Correlation.

7. Linear Algebra

np.dot(a, b) → Dot product.
np.matmul(a, b) → Matrix multiplication.
np.linalg.inv(a) → Inverse.
np.linalg.det(a) → Determinant.
np.linalg.eig(a) → Eigenvalues & eigenvectors.
np.linalg.norm(a) → Norm.
np.linalg.solve(a, b) → Solve linear equations.

8. Sorting & Searching

np.sort(arr) → Sorted copy.
arr.sort() → Sort in-place.
np.argsort(arr) → Indices of sorted array.
np.unique(arr) → Unique values.
np.where(condition) → Indices meeting condition.
np.nonzero(arr) → Indices of non-zeros.

9. Random Module

np.random.seed(n) → Fix randomness.
np.random.rand(dims) → Uniform [0,1).
np.random.randn(dims) → Normal distribution.
np.random.randint(low, high, size).
np.random.choice(arr, size) → Random sample.
np.random.shuffle(arr) → Shuffle in-place.

10. File I/O

np.loadtxt(filename) → Load text file.
np.genfromtxt(filename) → Load with missing values.
np.savetxt(filename, arr) → Save to text.
np.save(filename, arr) → Save as .npy.
np.load(filename) → Load .npy.
np.savez(filename, a=arr1, b=arr2) → Save multiple arrays.