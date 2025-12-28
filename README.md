<!-- Banner -->
![Banner](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=NumPy%20Crash%20Notes&fontSize=40&fontAlignY=35&desc=Hands-on%20NumPy%20cheatsheet%20with%20runnable%20cells&descAlignY=55&descAlign=50)

# NumPy Crash Notes

Compact, no-fluff NumPy reference backed by an executable notebook. Learn array creation, reshaping, indexing, vectorized math, and broadcasting by running the code yourself.

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
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

## Why this guide?

- **Notebook first**: everything lives in [src/code.ipynb](src/code.ipynb) — no walls of text
- **23 focused sections**: array creation, shape ops, slicing, boolean/fancy indexing, vectorization, math/stats helpers, broadcasting, save/load, views vs copies, NaN handling, linear algebra, and performance tips
- **Copy-paste ready**: runnable cells with short explanations
- **Lightweight setup**: just Python, NumPy, and Jupyter
- **Target audience**: folks who already know Python basics and want practical NumPy patterns fast

## Tech stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

## Prerequisites
- **Python 3.7+** (3.8+ recommended)
- Basic Python knowledge: lists, loops, functions
- Familiarity with command line (for installation)
- No prior NumPy experience needed

## Quick start
1) (Optional) Create a virtual environment
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
2) Install tools
    ```bash
    pip install numpy jupyter
    ```
3) Open and run the notebook
    - VS Code: open [src/code.ipynb](src/code.ipynb) and run cells top-to-bottom
    - CLI: `python -m jupyter notebook src/code.ipynb`
4) Quick sanity check inside Python REPL
    ```python
    import numpy as np
    np.arange(6).reshape(2, 3)
    ```

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

## Tips for smooth runs
- Execute cells sequentially so shared arrays exist when referenced
- If outputs look stale, restart the kernel and rerun all cells
- Stick to vectorized operations; they are usually faster and clearer than Python loops
- Prefer `axis` over manual loops for reductions (mean/sum/std)
- When shapes do not align, print `arr.shape` early to spot broadcasting issues
- Use `.copy()` explicitly when you need independent arrays (avoid view bugs)
- Set `np.random.seed()` for reproducible random data
- Profile with small slices first; then scale up

## Project structure
```
/workspaces/Numpy/
├── README.md                # This file - complete guide and reference
└── src/
    ├── code.ipynb          # Main notebook with 23 sections (start here!)
    ├── tmp_array.npy       # Example binary save output (auto-generated)
    └── tmp_array.csv       # Example CSV save output (auto-generated)
```

**Note**: The `.npy` and `.csv` files are created when you run the save/load section of the notebook.

## Resources

### Official documentation
- [NumPy official docs](https://numpy.org/doc/stable/) - comprehensive reference
- [NumPy quickstart tutorial](https://numpy.org/doc/stable/user/quickstart.html) - official beginner guide
- [NumPy for MATLAB users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html) - migration guide

### Further learning
- [NumPy illustrated guide](https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d) - visual explanations
- [From Python to NumPy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/) - free online book
- [SciPy lecture notes](https://scipy-lectures.org/) - NumPy + scientific Python ecosystem

### Next steps after this guide
- **pandas**: DataFrames for tabular data (builds on NumPy)
- **Matplotlib/Seaborn**: visualization with NumPy arrays
- **SciPy**: scientific computing (optimization, signal processing, etc.)
- **scikit-learn**: machine learning (uses NumPy arrays internally)

## Contributing

Contributions are welcome! Here's how you can help:
- **Report issues**: Found a bug or typo? Open an issue
- **Suggest improvements**: Ideas for new sections or examples? Let us know
- **Submit PRs**: Code fixes or enhancements are appreciated
- **Share feedback**: What worked? What didn't? Your input helps improve the guide

## License

This project is open source and available for educational use. Feel free to use, modify, and share with attribution.

<!-- Footer -->
![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer)