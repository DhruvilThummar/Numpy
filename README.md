<!-- Banner -->
![Banner](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=NumPy%20Crash%20Notes&fontSize=40&fontAlignY=35&desc=Hands-on%20NumPy%20cheatsheet%20with%20runnable%20cells&descAlignY=55&descAlign=50)

# NumPy Crash Notes

Compact, no-fluff NumPy reference backed by an executable notebook. Learn array creation, reshaping, indexing, vectorized math, and broadcasting by running the code yourself.

## 🔗 Quick Navigation

<div align="center">

[![Full Tutorial](https://img.shields.io/badge/📖_FULL_TUTORIAL-blue?style=for-the-badge&logo=jupyter&logoColor=white)](src/code.ipynb)
[![Quick Reference](https://img.shields.io/badge/⚡_QUICK_REFERENCE-green?style=for-the-badge&logo=markdown&logoColor=white)](QUICK_REFERENCE.md)

</div>

---

## Table of Contents
- [Why this guide?](#why-this-guide)
- [Tech stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Quick start](#quick-start)
- [What you will learn](#what-you-will-learn)
- [Notebook map](#notebook-map-23-sections)
- [Examples you can reuse](#examples-you-can-reuse)
- [Tips for smooth runs](#tips-for-smooth-runs)
- [Project structure](#project-structure)
- [Feature highlights](#-feature-highlights)
- [Resources](#resources)
- [FAQ](#-quick-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## Why this guide?

✨ **The Problem**: NumPy can feel overwhelming with 600+ functions.

✅ **The Solution**: We focus on the **20% that matters 80%** of the time.

**What makes this different:**
- **Notebook first** - Everything lives in executable cells, not walls of text
- **35+ comprehensive sections** - 1D/2D/3D arrays, indexing, slicing, shape ops, broadcasting, linear algebra, and more
- **Copy-paste ready** - Every code snippet runs immediately and is production-tested
- **Plain language** - Functions explained with analogies and visual outputs, no jargon
- **Lightweight setup** - Just Python, NumPy, and Jupyter (15 minutes to start)
- **For Python developers** - Assumes Python basics; teaches practical NumPy patterns fast

---

## Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

</div>

---

## Prerequisites

- **Python 3.7+** (3.8+ recommended)
- ✅ Basic Python knowledge (lists, loops, functions)
- ✅ Familiarity with command line (for installation)
- ✅ A code editor (VS Code, PyCharm, etc.)
- ❌ **NO prior NumPy experience needed** - we start from zero!

---

## Quick Start

### 1️⃣ Install (if needed)
```bash
# Optional: Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install numpy jupyter
```

### 2️⃣ Start Learning
**Option A - VS Code (Recommended)**
- Open folder in VS Code
- Click on [src/code.ipynb](src/code.ipynb)
- Run cells from top to bottom (Shift+Enter)

**Option B - Jupyter CLI**
```bash
python -m jupyter notebook src/code.ipynb
```

### 3️⃣ Verify Installation
```python
import numpy as np
result = np.arange(6).reshape(2, 3)
print(result)
# Output:
# [[0 1 2]
#  [3 4 5]]
```

✅ If that works, you're ready to learn!

---

## What you will learn

### Core fundamentals
- **Arrays**: literals plus helpers (`zeros`, `ones`, `eye`, `arange`, `linspace`, `random`)
- **Shape and dtype**: `shape`, `ndim`, `size`, `dtype`, reshape/flatten/transpose/squeeze
- **Indexing**: row/column slices, boolean masks, fancy indexing
- **Vectorization**: elementwise arithmetic/comparisons; avoid Python loops

### Math and operations
- **Math and stats**: `sum`, `mean`, `min`, `max`, `std`, `sqrt`, `log`, axis semantics
- **Broadcasting**: align mismatched shapes for arithmetic
- **Conditional ops**: `where`, `clip`, `select` for element-wise logic
- **Matrix operations**: matmul (`@`), dot product, transpose, inverse, eigenvalues, norms

### Advanced workflows
- **Combine & split**: `concatenate`, `vstack`, `hstack`, `split`
- **Sorting & uniques**: `sort`, `argsort`, `unique` with counts
- **Save & load**: binary (`.npy`) and text (CSV) persistence
- **NaN handling**: `nanmean`, `nansum`, `isnan`, `nan_to_num`
- **Views vs copies**: understand memory sharing to avoid silent bugs
- **Performance**: timing comparisons, dtype choices, memory footprint

---

## Notebook map (23 sections)

| Section | Topic | Key takeaway |
|---------|-------|--------------|
| 1️⃣ | What NumPy is | Vectorization beats Python loops |
| 2️⃣ | Creating arrays | `array()`, `zeros`, `ones`, `eye`, `arange`, `linspace`, `random` |
| 3️⃣ | Shape, type, memory | `shape`, `ndim`, `size`, `dtype`, `reshape`, `flatten`, `T` |
| 4️⃣ | Indexing & slicing | Row/column access, boolean indexing, fancy indexing |
| 5️⃣ | Vectorized operations | Comparisons and why NumPy exists |
| 6️⃣ | Math & stats helpers | `sum`, `mean`, `min`, `max`, `std`, `sqrt`, `log` |
| 7️⃣ | Broadcasting | Add vectors to matrices, align shapes automatically |
| 8️⃣ | Combine & split | `concatenate`, `vstack`, `hstack`, `split` |
| 9️⃣ | Sorting & uniques | `sort`, `argsort`, `unique` with counts |
| 🔟 | Column standardization | Real workflow example with axis operations |
| 1️⃣1️⃣ | Save & load | `.npy` binary format and CSV text format |
| 1️⃣2️⃣ | Performance checklist | Avoid loops, preallocate, use axis arguments |
| 1️⃣3️⃣ | Views vs copies | Shared memory gotchas and when to `.copy()` |
| 1️⃣4️⃣ | NaN-aware stats | `nanmean`, `nansum`, `isnan`, `nan_to_num` |
| 1️⃣5️⃣ | Matrix operations | `@`, `dot`, `T`, `inv`, `eigvals`, `norm` |
| 1️⃣6️⃣ | NumPy vs pandas | When to use which library |
| 1️⃣7️⃣ | Debugging shape errors | Broadcasting failures and fixes with `None` |
| 1️⃣8️⃣ | Dtype & precision | Type upcasting and precision gotchas |
| 1️⃣9️⃣ | Performance timing | NumPy vs pure Python speed comparison |
| 2️⃣0️⃣ | Quick recap | Summary and next steps |
| 2️⃣1️⃣ | Conditional ops | `where`, `clip`, `select` for element-wise logic |
| 2️⃣2️⃣ | Reshape cheat sheet | `reshape`, `ravel`, `flatten`, `newaxis`, `squeeze` |
| 2️⃣3️⃣ | Memory footprint | Check array sizes with different dtypes |

---

## Examples you can reuse
- Create sample data quickly: `np.arange`, `np.linspace`, random generators
- Clean reshaping: `reshape`, `ravel`, `transpose`, `expand_dims`, `squeeze`
- Filter and pick: boolean masks, multi-axis slices, integer index arrays
- Fast math: vectorized arithmetic plus `sum/mean/std` by axis
- Broadcast smartly: add vectors to matrices or scale batches without loops
- Persist arrays: save to `.npy` (binary, preserves dtype) or CSV (human-readable)
- Conditional logic: `np.where(condition, true_val, false_val)` replaces if-else loops
- Standardize data: `(data - data.mean(axis=0)) / data.std(axis=0)` by column
- Reproducibility: `np.random.seed(42)` before random operations

---

## Tips for smooth runs
- Execute cells sequentially so shared arrays exist when referenced
- If outputs look stale, restart the kernel and rerun all cells
- Stick to vectorized operations; they are usually faster and clearer than Python loops
- Prefer `axis` over manual loops for reductions (mean/sum/std)
- When shapes do not align, print `arr.shape` early to spot broadcasting issues
- Use `.copy()` explicitly when you need independent arrays (avoid view bugs)
- Set `np.random.seed()` for reproducible random data
- Profile with small slices first; then scale up

---

## Project Structure
```
/workspaces/Numpy/
├── README.md                      # 📖 Main guide (you are here!)
├── QUICK_REFERENCE.md             # ⚡ Fast lookup cheatsheet
└── src/
    ├── code.ipynb                 # 🎓 35+ interactive lessons (start here!)
    ├── tmp_array.npy              # 💾 Example binary output (auto-generated)
    └── tmp_array.csv              # 📊 Example CSV output (auto-generated)
```

**Note**: The `.npy` and `.csv` files are created when you run the save/load section of the notebook.

---

## 🎯 Feature Highlights

| Feature | Benefit |
|---------|---------|
| 📌 **35+ Interactive Sections** | Comprehensive coverage from basics to advanced |
| 🏃 **Copy-Paste Ready Code** | All examples are executable and reusable |
| 📝 **Quick Reference Guide** | Fast lookup without reading full explanations |
| 💡 **Real-World Examples** | Practical patterns you can use immediately |
| ⚡ **Performance Tips** | Optimize your NumPy code for speed |
| 🧪 **Hands-On Learning** | Learn by running code, not just reading |

---

## Resources

### 📖 Official Documentation
- [NumPy Official Docs](https://numpy.org/doc/stable/) - Complete API reference
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html) - Official beginner guide  
- [NumPy for MATLAB Users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html) - If you know MATLAB

### 🎨 Visual Learning
- [NumPy Illustrated Guide](https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d) - Visual explanations
- [From Python to NumPy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/) - Free online book with visuals
- [SciPy Lecture Notes](https://scipy-lectures.org/) - NumPy + scientific ecosystem

### 🚀 Next Steps After NumPy
Once you've mastered NumPy, explore:
- **pandas** - Tabular data & DataFrames (built on NumPy)
- **Matplotlib/Seaborn** - Data visualization with NumPy arrays
- **SciPy** - Scientific computing (optimization, signals, etc.)
- **scikit-learn** - Machine learning with NumPy foundations
- **TensorFlow/PyTorch** - Deep learning (uses NumPy-like arrays)

---

## 📚 Quick FAQ

**Q: Do I need prior NumPy experience?**  
A: No! Just basic Python knowledge (lists, loops, functions).

**Q: Can I run this offline?**  
A: Yes! Install Python, NumPy, and Jupyter locally.

**Q: How long does it take to complete?**  
A: 2-4 hours depending on your pace and practice time.

**Q: Are the code examples production-ready?**  
A: Yes! The patterns shown are used in real production code.

**Q: Can I use this as a reference after learning?**  
A: Absolutely! That's why we have the Quick Reference guide.

**Q: Is this guide affiliated with NumPy?**  
A: No, it's a community educational resource for learning NumPy.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:
- **🐛 Report Issues**: Found a bug or typo? [Open an issue](../../issues)
- **💡 Suggest Improvements**: Ideas for new sections? Let us know
- **📝 Submit PRs**: Code fixes and enhancements appreciated
- **📢 Share Feedback**: Your input helps improve the guide

---

## 📄 License

This project is open source and available for educational use. Feel free to use, modify, and share with attribution.

---

<div align="center">

## 🚀 Ready to Master NumPy?

### Start Your Journey Now!

[![🎓 OPEN FULL TUTORIAL](https://img.shields.io/badge/🎓_OPEN_FULL_TUTORIAL-0078D4?style=for-the-badge&logo=jupyter&logoColor=white&logoWidth=20)](src/code.ipynb)

[![⚡ QUICK REFERENCE](https://img.shields.io/badge/⚡_QUICK_REFERENCE_GUIDE-28A745?style=for-the-badge&logo=markdown&logoColor=white&logoWidth=20)](QUICK_REFERENCE.md)

---

![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-green?style=for-the-badge)
![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge)

</div>

<!-- Footer -->
![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer)
