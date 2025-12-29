<!-- Banner -->
![Banner](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=NumPy%20Crash%20Notes&fontSize=40&fontAlignY=35&desc=Hands-on%20NumPy%20cheatsheet%20with%20runnable%20cells&descAlignY=55&descAlign=50)

# 📊 NumPy Crash Notes

<div align="center">

**The fastest way to master NumPy** — Learn by doing with 38 interactive, copy-paste-ready code examples

[![Full Tutorial](https://img.shields.io/badge/📖_OPEN_TUTORIAL-0078D4?style=for-the-badge&logo=jupyter&logoColor=white)](src/code.ipynb)
[![Quick Reference](https://img.shields.io/badge/⚡_QUICK_GUIDE-28A745?style=for-the-badge&logo=markdown&logoColor=white)](QUICK_REFERENCE.md)

</div>

---

## 🎯 What is This?

A **compact, hands-on guide** to NumPy that cuts through the noise. No fluff, no 600+ function memorization — just the **essential 20% that gets you 80% of the work done**.

### ✨ The Problem We Solve
- NumPy has 600+ functions but you only need ~50
- Most tutorials are bloated textbooks
- Learning examples don't match real-world patterns
- You want to learn by *running code*, not reading theory

### ✅ Our Solution
- **38 interactive sections** with runnable Jupyter cells
- **Copy-paste ready** code (production patterns included)
- **Plain English** explanations + visual outputs
- **15 minutes to get started**, 2-4 hours to master

---

## 🚀 Quick Start (3 steps)

### 1️⃣ Install
```bash
# Create virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: venv\Scripts\activate

# Install NumPy & Jupyter
pip install numpy jupyter
```

### 2️⃣ Open & Run
```bash
# Option A: VS Code (Recommended)
# Just click on src/code.ipynb and run cells with Shift+Enter

# Option B: Jupyter CLI
jupyter notebook src/code.ipynb
```

### 3️⃣ Verify
```python
import numpy as np
result = np.arange(6).reshape(2, 3)
print(result)
# Output: [[0 1 2]
#          [3 4 5]]
```

✅ **You're ready!** Now start with the first cell in [src/code.ipynb](src/code.ipynb)

---

## 📚 What You'll Learn

### Fundamentals (Sections 1-10)
✔️ Installing NumPy & basic imports  
✔️ Creating arrays (from lists, zeros, ones, ranges, random)  
✔️ Understanding shape, dimensions, and data types  
✔️ Indexing and slicing (1D, 2D, boolean indexing)  
✔️ Vectorized operations (why NumPy is fast)  

### Core Skills (Sections 11-20)
✔️ Math & statistics (`sum`, `mean`, `std`, `min`, `max`)  
✔️ Broadcasting (aligning shapes automatically)  
✔️ Combining & splitting arrays  
✔️ Sorting & finding unique values  
✔️ Real-world workflow example (standardizing data)  

### Advanced Topics (Sections 21-38)
✔️ Saving & loading arrays  
✔️ Performance optimization  
✔️ Views vs copies (memory management)  
✔️ Handling missing values (NaN)  
✔️ Linear algebra (matrix operations, eigenvalues)  
✔️ NumPy vs pandas (when to use which)  
✔️ Debugging shape errors  
✔️ Data type precision & performance  

---

## 🎨 How This Works

Each section includes:
1. **Clear explanation** — No jargon, just straightforward language
2. **Runnable code** — Copy-paste and execute immediately
3. **Visual output** — See results printed in the notebook
4. **Real use cases** — Patterns you'll actually use

**Example from the notebook:**
```python
# Creating arrays (Section 2)
arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)      # (5,)
print(arr.dtype)      # int64
print(arr.mean())     # 3.0

# Broadcasting (Section 7)
result = arr + 10     # Add 10 to every element
print(result)         # [11 12 13 14 15]

# Vectorization (Section 5)
fast = arr * 2        # ⚡ Fast (NumPy way)
slow = [x * 2 for x in arr]  # ❌ Slow (Python way)
```

---

## ⭐ Why Choose This Guide?

| Feature | Benefit |
|---------|---------|
| **38 interactive sections** | Complete curriculum from basics to advanced |
| **Notebook-first** | Learn by running code, not reading walls of text |
| **Copy-paste ready** | Every example is production-tested |
| **No prerequisites** | Just basic Python (no NumPy experience needed) |
| **15-min setup** | Install and start learning in minutes |
| **Quick reference** | Companion guide for fast lookups after learning |
| **Real patterns** | Code examples used in actual data science work |
| **Offline capable** | Download and run locally (no cloud needed) |

---

## 📁 Project Structure

```
/workspaces/Numpy/
├── README.md                      # 👈 You are here
├── QUICK_REFERENCE.md             # ⚡ Cheatsheet for quick lookups
├── .venv/                         # 🐍 Python virtual environment
└── src/
    ├── code.ipynb                 # 🎓 38 interactive lessons (START HERE!)
    └── .ipynb_checkpoints/        # Jupyter checkpoint files (auto-generated)
```

**Start here:** Open [src/code.ipynb](src/code.ipynb) in Jupyter or VS Code

---

## 💡 Common Use Cases

**"I need to create a matrix"**  
→ [Section 2: Array Creation](src/code.ipynb)

**"How do I reshape/flatten arrays?"**  
→ [QUICK_REFERENCE.md - Shape Manipulation](QUICK_REFERENCE.md)

**"What's the difference between views and copies?"**  
→ [Section 23: Views vs Copies](src/code.ipynb)

**"How do I handle missing values (NaN)?"**  
→ [Section 24: NaN Handling](src/code.ipynb)

**"How do I do matrix multiplication?"**  
→ [Section 25: Matrix Operations](src/code.ipynb)

---

## ❓ FAQ

<details>
<summary><b>Q: Do I need prior NumPy experience?</b></summary>
No! Just basic Python knowledge (lists, loops, functions). We start from zero.
</details>

<details>
<summary><b>Q: Can I use this offline?</b></summary>
Yes! Clone the repo, install Python & Jupyter locally, and you're good to go.
</details>

<details>
<summary><b>Q: How long does it take?</b></summary>
2-4 hours depending on your pace. You can do sections in any order (though sequential is best).
</details>

<details>
<summary><b>Q: Are the code examples production-ready?</b></summary>
Yes! The patterns shown are used in real data science and machine learning projects.
</details>

<details>
<summary><b>Q: Can I use this as a reference?</b></summary>
Absolutely! That's why we have [QUICK_REFERENCE.md](QUICK_REFERENCE.md) — bookmark it for quick lookups.
</details>

<details>
<summary><b>Q: Can I contribute?</b></summary>
Yes! See the [Contributing](#-contributing) section below.
</details>

---

## 🔗 Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

</div>

- **Python 3.7+** (3.8+ recommended for best performance)
- **NumPy** (latest version)
- **Jupyter** (for interactive notebooks)

---

## 📖 Additional Resources

### Official Documentation
- [NumPy Official Docs](https://numpy.org/doc/stable/) — Complete API reference
- [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html) — Official beginner guide
- [NumPy for MATLAB Users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html) — If you know MATLAB

### Learning Resources
- [NumPy Illustrated Guide](https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d) — Visual explanations
- [From Python to NumPy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/) — Free online book
- [SciPy Lecture Notes](https://scipy-lectures.org/) — NumPy + scientific Python

### Next Steps After NumPy
- **pandas** — DataFrames for tabular data (built on NumPy)
- **Matplotlib/Seaborn** — Data visualization with NumPy arrays
- **SciPy** — Scientific computing (signals, optimization, stats)
- **scikit-learn** — Machine learning (uses NumPy internally)
- **TensorFlow/PyTorch** — Deep learning (NumPy-like arrays)

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

- 🐛 **Found a bug?** [Open an issue](../../issues) with details
- 💡 **Have an idea?** [Start a discussion](../../discussions)
- 📝 **Want to contribute?** Fork and submit a PR
- 📢 **Share feedback** — Help us improve!

---

## 📄 License

This project is open source and available for educational use. Feel free to use, modify, and share with attribution.

---

<div align="center">

## 🎓 Ready to Master NumPy?

### Click below to start your learning journey!

[![🎓 OPEN FULL TUTORIAL](https://img.shields.io/badge/🎓_OPEN_FULL_TUTORIAL-0078D4?style=for-the-badge&logo=jupyter&logoColor=white)](src/code.ipynb)

[![⚡ QUICK_REFERENCE](https://img.shields.io/badge/⚡_QUICK_REFERENCE-28A745?style=for-the-badge&logo=markdown&logoColor=white)](QUICK_REFERENCE.md)

---

![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-green?style=for-the-badge)
![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge)
![Community Driven](https://img.shields.io/badge/Community-Driven-orange?style=for-the-badge)

**Happy Learning! 🚀**

</div>

<!-- Footer -->
![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer)
