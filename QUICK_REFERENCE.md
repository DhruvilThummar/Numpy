# 🎯 NumPy Quick Reference (The Cheat Sheet!)

> Forget memorizing! Just copy-paste what you need 👇

---

## 🗂️ Find What You Need

| 🔍 Looking for... | 🎯 Go here |
|---------|-------------|
| Making arrays from scratch | [Array Creation](#-array-creation) |
| Checking size, shape, type | [Array Properties](#-array-properties) |
| Getting specific elements | [Indexing & Slicing](#-indexing--slicing) |
| Math stuff (+, -, *, /) | [Math Operations](#-math-operations) |
| Sum, average, min, max | [Aggregation](#-aggregation) |
| Reshape, transpose, flip | [Shape Manipulation](#-shape-manipulation) |
| Putting arrays together | [Combining Arrays](#-combining-arrays) |
| Working with NaN (missing values) | [NaN Handling](#-nan-handling) |
| Linear algebra stuff | [Matrix Operations](#-matrix-operations) |

---

## 🏗️ Array Creation

**Just want an array? Pick your flavor:**

```python
# From a list
np.array([1, 2, 3])

# Full of zeros or ones
np.zeros(5)                  # [0. 0. 0. 0. 0.]
np.ones((2, 3))              # All 1's, shape 2×3

# Counting up (like range())
np.arange(10)                # 0, 1, 2, ... 9
np.arange(2, 10, 2)          # 2, 4, 6, 8

# Evenly spaced numbers
np.linspace(0, 1, 5)         # 5 numbers between 0-1

# Special matrices
np.eye(3)                    # Identity matrix (1's on diagonal)
np.diag([1, 2, 3])           # Diagonal matrix

# Random stuff
np.random.rand(2, 3)         # Random decimals 0-1
np.random.randint(0, 10, 5)  # Random integers 0-10
np.random.normal(0, 1, 100)  # Normal distribution

# Fill with same value
np.full((2, 2), 7)           # All 7's in 2×2 array
```

---

## 📊 Array Properties

**What's inside your array?**

```python
arr.shape          # (rows, columns) - like "3×5"
arr.ndim           # How many dimensions? 1D, 2D, 3D, etc
arr.size           # Total number of elements
arr.dtype          # Data type: int64, float32, etc
arr.itemsize       # Bytes per item
arr.nbytes         # Total memory used

# Quick checks
len(arr)           # Length (rows only)
arr.T              # Transpose (flip rows ↔ columns)
```

---

## 🎯 Indexing & Slicing

**Grabbing specific pieces from your array:**

```python
# Single element
arr[0]             # First element
arr[-1]            # Last element
arr[2]             # Element at index 2

# Slicing (get a range)
arr[1:3]           # Elements 1 and 2 (NOT 3)
arr[0:5:2]         # Elements 0, 2, 4 (every 2nd)
arr[::2]           # Every 2nd element from start to end

# 2D arrays (rows and columns)
arr[0, 0]          # Row 0, Column 0
arr[0, :]          # Entire row 0
arr[:, 1]          # Entire column 1
arr[1:3, 0:2]      # Rows 1-2, Columns 0-1

# Smart filtering
arr[arr > 5]       # All elements greater than 5
arr[arr % 2 == 0]  # All even numbers

# Pick specific positions
arr[[0, 2, 4]]     # Elements at positions 0, 2, 4
```

---

## ➕ Math Operations

**Do math on your whole array at once!**

```python
# Basic arithmetic (works on ALL elements)
arr + 5            # Add 5 to everything
arr - 10           # Subtract 10
arr * 2            # Multiply by 2
arr / 2            # Divide by 2
arr ** 2           # Square everything

# Powers and roots
np.sqrt(arr)       # Square root
np.exp(arr)        # e raised to power
np.log(arr)        # Natural logarithm
np.abs(arr)        # Absolute value

# Trigonometry
np.sin(arr)        # Sine
np.cos(arr)        # Cosine
np.tan(arr)        # Tangent

# Useful tricks
arr.mean()         # Average
arr.max()          # Biggest number
arr.min()          # Smallest number
arr - arr.mean()   # Center the data (subtract average)
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

**Make your code FAST:**

```python
# ✅ FAST - Vectorized (use these!)
result = arr + 1
result = np.sum(arr, axis=0)
result = arr[arr > 5]

# ❌ SLOW - Python loops (avoid!)
result = np.array([x + 1 for x in arr])
result = sum([x for x in arr])

# Memory tricks
arr = arr.astype(np.float32)   # Smaller than float64
arr_copy = arr.copy()          # Independent array
result = np.empty((1000, 1000))  # Pre-allocate
```

---

## 🎓 Common Gotchas

| 💥 Problem | ✅ Fix |
|----------|--------|
| Shape mismatch | Print `arr.shape` first! |
| Accidentally modify copy | Use `.copy()` | 
| Slow loops | Use vectorized operations |
| Floating point bugs | Use `np.allclose()` not `==` |
| Memory bloat | Use `float32` instead of `float64` |
| Views vs copies | Remember `.copy()` makes independent copy |

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

### Need more details? 
**[← Go Back to README](README.md)** | **[→ Full Tutorial](src/code.ipynb)**

</div>
