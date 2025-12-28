<!-- Banner -->
![Banner](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=NumPy%20Crash%20Notes&fontSize=40&fontAlignY=35&desc=Hands-on%20NumPy%20cheatsheet%20with%20runnable%20cells&descAlignY=55&descAlign=50)

# NumPy Crash Notes

Compact, no-fluff NumPy reference backed by an executable notebook. Learn array creation, reshaping, indexing, vectorized math, and broadcasting by running the code yourself.

## At a glance
- Notebook first: everything lives in [src/code.ipynb](src/code.ipynb)
- Focused coverage: array creation, shape ops, slicing, boolean/fancy indexing, vectorization, math/stats helpers, broadcasting
- Copy-paste ready cells plus short explanations
- Lightweight setup: just Python, NumPy, and Jupyter
- Audience: folks who already know Python basics and want practical NumPy patterns fast

## Tech stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

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
- Arrays: literals plus helpers (`zeros`, `ones`, `eye`, `arange`, `linspace`, `random`)
- Shape and dtype: `shape`, `ndim`, `size`, `dtype`, reshape/flatten/transpose
- Indexing: row/column slices, boolean masks, fancy indexing
- Vectorization: elementwise arithmetic/comparisons; avoid Python loops
- Math and stats: `sum`, `mean`, `min`, `max`, `std`, `sqrt`, `log`, axis semantics
- Broadcasting: align mismatched shapes for arithmetic

## Examples you can reuse
- Create sample data quickly: `np.arange`, `np.linspace`, random generators
- Clean reshaping: `reshape`, `ravel`, `transpose`, `expand_dims`, `squeeze`
- Filter and pick: boolean masks, multi-axis slices, integer index arrays
- Fast math: vectorized arithmetic plus `sum/mean/std` by axis
- Broadcast smartly: add vectors to matrices or scale batches without loops

## Notebook map
- Section 1: what NumPy is and why vectorization beats Python loops
- Section 2: creating arrays and essential constructors
- Section 3: shapes, dtypes, and memory basics
- Section 4: slicing, boolean, and fancy indexing
- Section 5: vectorized math and comparisons
- Section 6: math/stat helpers with axis control
- Section 7: broadcasting patterns that unlock most use cases

## Tips for smooth runs
- Execute cells sequentially so shared arrays exist when referenced
- If outputs look stale, restart the kernel and rerun all cells
- Stick to vectorized operations; they are usually faster and clearer than Python loops
- Prefer `axis` over manual loops for reductions (mean/sum/std)
- When shapes do not align, print `arr.shape` early to spot broadcasting issues

## Contributing
Suggestions or improvements welcome—feel free to open an issue or PR.

<!-- Footer -->
![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer)