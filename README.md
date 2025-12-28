<!-- Banner -->
![Banner](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=NumPy%20Crash%20Notes&fontSize=40&fontAlignY=35&desc=Hands-on%20NumPy%20cheatsheet%20with%20runnable%20cells&descAlignY=55&descAlign=50)

# NumPy Crash Notes

Compact, no-fluff NumPy reference backed by an executable notebook. Learn array creation, reshaping, indexing, vectorized math, and broadcasting by running the code yourself.

## At a glance
- Notebook first: everything lives in [src/code.ipynb](src/code.ipynb)
- Focused coverage: array creation, shape ops, slicing, boolean/fancy indexing, vectorization, math/stats helpers, broadcasting
- Copy-paste ready cells plus short explanations
- Lightweight setup: just Python, NumPy, and Jupyter

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

## Notebook map
- Arrays: literals plus helpers (`zeros`, `ones`, `eye`, `arange`, `linspace`, `random`)
- Shape and dtype: `shape`, `ndim`, `size`, `dtype`, reshape/flatten/transpose
- Indexing: row/column slices, boolean masks, fancy indexing
- Vectorization: elementwise arithmetic/comparisons; avoid Python loops
- Math and stats: `sum`, `mean`, `min`, `max`, `std`, `sqrt`, `log`, axis semantics
- Broadcasting: align mismatched shapes for arithmetic

## Usage patterns (grab-and-go)
- Create sample data quickly: `np.arange`, `np.linspace`, random generators
- Clean reshaping: `reshape`, `ravel`, `transpose`, `expand_dims`, `squeeze`
- Filter and pick: boolean masks, multi-axis slices, integer index arrays
- Fast math: vectorized arithmetic plus `sum/mean/std` by axis
- Broadcast smartly: add vectors to matrices or scale batches without loops

## Tips for smooth runs
- Execute cells sequentially so shared arrays exist when referenced
- If outputs look stale, restart the kernel and rerun all cells
- Stick to vectorized operations; they are usually faster and clearer than Python loops

## Contributing
Suggestions or improvements welcome—feel free to open an issue or PR.

<!-- Footer -->
![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer)