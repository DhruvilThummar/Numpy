<div align="center">

![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

# 🎯 NumPy Quick Reference

### ⚡ The Ultimate Cheat Sheet ⚡
**Forget memorizing, just copy-paste what you need!**

[![Back to README](https://img.shields.io/badge/←_Back_to_README-667EEA?style=for-the-badge&logoColor=white)](README.md)
[![Full Tutorial](https://img.shields.io/badge/📖_Full_Tutorial-764BA2?style=for-the-badge&logoColor=white)](src/code.ipynb)
[![GitHub](https://img.shields.io/badge/⭐_Star_on_GitHub-181717?style=for-the-badge&logo=github)](https://github.com/DhruvilThummar/Numpy)

</div>

---

## 🗂️ Find What You Need

<div align="center">

| 🔍 **Looking for...** | 🎯 **Jump to Section** | ⚡ **Quick Action** |
|:---------------------|:----------------------|:-------------------|
| Making arrays from scratch | [🏗️ Array Creation](#-array-creation) | `np.array([1,2,3])` |
| Checking size, shape, type | [📊 Array Properties](#-array-properties) | `arr.shape` |
| Getting specific elements | [🎯 Indexing & Slicing](#-indexing--slicing) | `arr[0:5]` |
| Math stuff (+, -, *, /) | [➕ Math Operations](#-math-operations) | `arr + 5` |
| Sum, average, min, max | [📈 Aggregation](#-aggregation) | `np.mean(arr)` |
| Reshape, transpose, flip | [🔄 Shape Manipulation](#-shape-manipulation) | `arr.reshape(2,3)` |
| Putting arrays together | [🔗 Combining Arrays](#-combining-arrays) | `np.vstack([a,b])` |
| Working with missing values | [🚫 NaN Handling](#-nan-handling) | `np.nanmean(arr)` |
| Linear algebra stuff | [🧮 Matrix Operations](#-matrix-operations) | `arr @ other` |

</div>

---

## 🏗️ Array Creation

> **🎨 Just want an array? Pick your flavor!**

<details open>
<summary><b>📦 From Lists & Sequences</b></summary>

```python
# From a list
np.array([1, 2, 3])

# 2D array from nested lists
np.array([[1, 2], [3, 4]])
```
</details>

<details open>
<summary><b>🔢 Zeros, Ones & Filled Arrays</b></summary>

```python
# Full of zeros or ones
np.zeros(5)                  # [0. 0. 0. 0. 0.]
np.ones((2, 3))              # All 1's, shape 2×3
np.full((2, 2), 7)           # All 7's in 2×2 array
```
</details>

<details open>
<summary><b>🔢 Sequential & Evenly Spaced</b></summary>

```python
# Counting up (like range())
np.arange(10)                # 0, 1, 2, ... 9
np.arange(2, 10, 2)          # 2, 4, 6, 8

# Evenly spaced numbers
np.linspace(0, 1, 5)         # 5 numbers between 0-1
```
</details>

<details open>
<summary><b>🎲 Random Arrays</b></summary>

```python
np.random.rand(2, 3)         # Random decimals 0-1
np.random.randint(0, 10, 5)  # Random integers 0-10
np.random.normal(0, 1, 100)  # Normal distribution (mean=0, std=1)
np.random.choice([1,2,3], 5) # Random selection
```
</details>

<details open>
<summary><b>🎯 Special Matrices</b></summary>

```python
np.eye(3)                    # Identity matrix (1's on diagonal)
np.diag([1, 2, 3])           # Diagonal matrix
np.tri(3)                    # Lower triangular matrix
```
</details>

---

## 📊 Array Properties

> **🔍 What's inside your array?**

### 📐 **Shape & Dimensions**
```python
arr.shape          # (rows, columns) - like "3×5"
arr.ndim           # How many dimensions? 1D, 2D, 3D, etc
arr.size           # Total number of elements
len(arr)           # Length (rows only)
```

### 🧬 **Data Type & Memory**
```python
arr.dtype          # Data type: int64, float32, etc
arr.itemsize       # Bytes per item
arr.nbytes         # Total memory used = size × itemsize
```

### ⚡ **Quick Transformations**
```python
arr.T              # Transpose (flip rows ↔ columns)
arr.flat           # 1D iterator over array
```

---

## 🎯 Indexing & Slicing

> **✂️ Grabbing specific pieces from your array**

### 🎪 **Single Elements**
```python
arr[0]             # First element
arr[-1]            # Last element
arr[2]             # Element at index 2
```

### 🔪 **Slicing (Ranges)**
```python
arr[1:3]           # Elements 1 and 2 (NOT 3)
arr[0:5:2]         # Elements 0, 2, 4 (every 2nd)
arr[::2]           # Every 2nd element from start to end
arr[::-1]          # Reverse the array
```

### 🎛️ **2D Arrays (Rows & Columns)**
```python
arr[0, 0]          # Row 0, Column 0
arr[0, :]          # Entire row 0
arr[:, 1]          # Entire column 1
arr[1:3, 0:2]      # Rows 1-2, Columns 0-1
```

### 🎭 **Boolean Indexing (Smart Filtering)**
```python
arr[arr > 5]       # All elements greater than 5
arr[arr % 2 == 0]  # All even numbers
arr[(arr > 5) & (arr < 10)]  # Multiple conditions
```

### 🎯 **Fancy Indexing**
```python
arr[[0, 2, 4]]     # Elements at positions 0, 2, 4
arr[[True, False, True]]  # Boolean array
```

---

## ➕ Math Operations

> **🧮 Do math on your whole array at once! (Vectorized = FAST!)**

### 🔢 **Basic Arithmetic**
```python
arr + 5            # Add 5 to everything
arr - 10           # Subtract 10 from everything
arr * 2            # Multiply everything by 2
arr / 2            # Divide everything by 2
arr ** 2           # Square everything
arr % 3            # Modulo (remainder)
arr // 2           # Floor division
```

### 📐 **Powers & Roots**
```python
np.sqrt(arr)       # Square root
np.cbrt(arr)       # Cube root
np.power(arr, 3)   # Raise to power
np.exp(arr)        # e^x (exponential)
np.log(arr)        # Natural logarithm (ln)
np.log10(arr)      # Base-10 logarithm
```

### 🌊 **Trigonometry**
```python
np.sin(arr)        # Sine
np.cos(arr)        # Cosine
np.tan(arr)        # Tangent
np.arcsin(arr)     # Inverse sine
```

### 🎯 **Absolute & Rounding**
```python
np.abs(arr)        # Absolute value
np.round(arr, 2)   # Round to 2 decimals
np.floor(arr)      # Round down
np.ceil(arr)       # Round up
```

### 💡 **Useful Tricks**
```python
arr - arr.mean()   # Center the data (subtract average)
(arr - arr.min()) / (arr.max() - arr.min())  # Normalize to 0-1
```

---

## 📈 Aggregation

**Combine all numbers into one (or a few):**

```python
# The basics
np.sum(arr)        # Add everything up
np.mean(arr)       # Average
np.median(arr)     # Middle value
np.std(arr)        # How spread out?
np.var(arr)        # Variance (spread squared)
np.min(arr)        # Smallest
np.max(arr)        # Biggest

# Find positions
np.argmin(arr)     # Position of smallest
np.argmax(arr)     # Position of biggest

# By row or column
arr.sum(axis=0)    # Sum down (columns)
arr.sum(axis=1)    # Sum across (rows)

# Counting stuff
np.count_nonzero(arr)      # How many non-zero values?
np.unique(arr)             # List unique values
```

---

## 🔄 Shape Manipulation

**Reorganize your data:**

```python
# Change shape
arr.reshape(2, 3)          # Reshape to 2 rows, 3 cols
arr.reshape(-1)            # Flatten to 1D (auto-calc)
arr.ravel()                # Flatten to 1D
arr.flatten()              # Flatten (makes a copy)

# Flip and rotate
arr.T or arr.transpose()   # Flip diagonally
np.rot90(arr)              # Rotate 90 degrees

# Add dimensions
arr[:, np.newaxis]         # Add column dimension
arr[np.newaxis, :]         # Add row dimension
np.expand_dims(arr, axis=0)

# Remove size-1 dimensions
arr.squeeze()              # Remove 1-sized dimensions
```

---

## 🔗 Combining Arrays

**Mash two arrays together:**

```python
# Stack vertically (one on top of other)
np.vstack([arr1, arr2])    # Vertical stack
np.concatenate([arr1, arr2], axis=0)

# Stack horizontally (side by side)
np.hstack([arr1, arr2])    # Horizontal stack
np.concatenate([arr1, arr2], axis=1)

# Stack by depth
np.dstack([arr1, arr2])    # Depth stack

# Generic combine
np.concatenate([arr1, arr2])  # Default: stack vertically
```

---

## 🎭 Broadcasting

**Let NumPy figure out the math:**

```python
# This "just works"
arr + 5                    # Add 5 to every element
(3, 4) + (4,)             # Broadcasts to (3, 4) ✅
(3, 1) + (1, 4)           # Broadcasts to (3, 4) ✅

# When shapes don't fit, use newaxis
arr[:, np.newaxis] + other_arr
```

---

## 🚫 NaN Handling

**Deal with missing values:**

```python
# Detect NaN
np.isnan(arr)              # True where NaN, False elsewhere
np.any(np.isnan(arr))      # Is there ANY NaN?

# Ignore NaN in calculations
np.nanmean(arr)            # Average (skip NaN)
np.nansum(arr)             # Sum (skip NaN)
np.nanstd(arr)             # Std dev (skip NaN)
np.nanmin(arr)             # Min (skip NaN)
np.nanmax(arr)             # Max (skip NaN)

# Replace NaN
np.nan_to_num(arr)         # Replace NaN with 0
arr[np.isnan(arr)] = 0     # Manual replacement

# Filter out NaN
arr[~np.isnan(arr)]        # Keep only non-NaN values
```

---

## 🔀 Sorting & Finding

**Organize your data:**

```python
# Sort
np.sort(arr)               # Sorted copy
arr.sort()                 # Sort in place

# Find positions
np.argsort(arr)            # Positions that would sort it
np.argmax(arr)             # Position of max
np.argmin(arr)             # Position of min

# Unique values
np.unique(arr)             # Unique values only
np.unique(arr, return_counts=True)  # With counts

# Search
np.where(arr > 5)          # Positions where True
np.searchsorted(arr, 7)    # Where to insert 7
```

---

## 🎯 Conditional Operations

**If this, then that:**

```python
# Where (if-then-else)
np.where(condition, true_value, false_value)

# Example: Replace negative with 0
np.where(arr < 0, 0, arr)

# Clamp values (min-max)
np.clip(arr, min=0, max=10)    # Keep between 0-10

# Multiple conditions
np.select([cond1, cond2], [val1, val2], default=0)
```

---

## 🧮 Matrix Operations

**Linear algebra stuff:**

```python
# Matrix multiply
arr @ other_arr             # Matrix multiply (modern)
np.dot(arr, other_arr)      # Matrix multiply (classic)
np.matmul(arr, other_arr)   # Matrix multiply (explicit)

# Transpose
arr.T                       # Flip diagonally

# Inverse & determinant
np.linalg.inv(arr)          # Matrix inverse
np.linalg.det(arr)          # Determinant

# Eigenvalues & eigenvectors
np.linalg.eigvals(arr)      # Eigenvalues only
evals, evecs = np.linalg.eig(arr)  # Both

# Norms
np.linalg.norm(arr)         # Magnitude
```

---

## 💾 Saving & Loading

**Persist your hard work:**

```python
# Binary (fast, preserves dtype)
np.save('file.npy', arr)            # Save
arr = np.load('file.npy')           # Load

# CSV (human-readable)
np.savetxt('file.csv', arr, delimiter=',')
arr = np.loadtxt('file.csv', delimiter=',')

# Multiple arrays
np.savez('data.npz', a=arr1, b=arr2)
data = np.load('data.npz')
arr1 = data['a']
arr2 = data['b']
```

---

## ⚡ Performance Tips

> **🚀 Make your code BLAZINGLY FAST!**

### ✅ **FAST - Vectorized Operations (USE THESE!)**
```python
result = arr + 1               # ⚡ 100x faster than loops
result = np.sum(arr, axis=0)   # ⚡ Built-in C optimization
result = arr[arr > 5]          # ⚡ Boolean indexing
result = arr * arr             # ⚡ Element-wise operations
```

### ❌ **SLOW - Python Loops (AVOID!)**
```python
result = np.array([x + 1 for x in arr])  # ❌ 100x slower!
result = sum([x for x in arr])            # ❌ Very slow
for i in range(len(arr)):                 # ❌ Don't loop!
    arr[i] = arr[i] + 1
```

### 💾 **Memory Optimization**
```python
# Use smaller data types
arr = arr.astype(np.float32)   # Half the size of float64
arr = arr.astype(np.int16)     # Smaller than int64

# Pre-allocate arrays
result = np.empty((1000, 1000))  # Faster than append
result = np.zeros((1000, 1000))  # Initialize with zeros

# Copy when needed
arr_copy = arr.copy()          # Independent array
view = arr[:]                  # Shared memory (faster)
```

### 🎯 **Speed Comparison**
| Operation | Python Loop | NumPy Vectorized | Speedup |
|-----------|-------------|------------------|----------|
| Add 1 to 1M elements | ~100ms | ~1ms | **100x** |
| Sum 1M elements | ~80ms | ~0.5ms | **160x** |
| Matrix multiply | ~10s | ~50ms | **200x** |

---

## 🎓 Common Gotchas

> **⚠️ Avoid these common mistakes!**

<div align="center">

| 💥 **Problem** | ✅ **Solution** | 📝 **Example** |
|:--------------|:---------------|:---------------|
| Shape mismatch | Print `arr.shape` first! | `print(arr.shape)` |
| Accidentally modify original | Use `.copy()` | `new_arr = arr.copy()` |
| Slow Python loops | Use vectorized operations | `arr + 1` not `[x+1 for x in arr]` |
| Floating point comparison | Use `np.allclose()` not `==` | `np.allclose(a, b)` |
| Memory bloat | Use `float32` instead of `float64` | `arr.astype(np.float32)` |
| Views vs copies confusion | Remember `.copy()` creates independent array | `view = arr[:]` vs `copy = arr.copy()` |
| Integer division issues | Use floats or `np.true_divide()` | `arr / 2.0` or `np.true_divide(arr, 2)` |
| Out of bounds indexing | Check array length first | `if i < len(arr): arr[i]` |

</div>

---

## 🔢 Data Types Quickie

```python
np.int8, np.int16, np.int32, np.int64          # Integers (different sizes)
np.uint8, np.uint16, np.uint32, np.uint64      # Unsigned (positive only)
np.float16, np.float32, np.float64              # Decimals (different precision)
np.complex64, np.complex128                     # Complex numbers
np.bool_                                        # True/False
```

---

<div align="center">

## 🎉 That's It! You're Now a NumPy Pro!

### 📚 **Next Steps**

[![← Go Back to README](https://img.shields.io/badge/←_Go_Back_to_README-667EEA?style=for-the-badge)](README.md)
[![→ Full Tutorial](https://img.shields.io/badge/→_Full_Tutorial-764BA2?style=for-the-badge)](src/code.ipynb)
[![⭐ Star on GitHub](https://img.shields.io/badge/⭐_Star_on_GitHub-181717?style=for-the-badge&logo=github)](https://github.com/DhruvilThummar/Numpy)

---

### 💡 **Quick Tips to Remember**

```python
# The 3 Golden Rules of NumPy:
1. Always use vectorized operations (avoid Python loops!)
2. Check array.shape before operating
3. Use .copy() when you don't want to modify the original
```

---

**Made with ❤️ for the NumPy community**

*Happy Array Computing! 🚀*

</div>
