<h1 align="center"> Data and Information Analysis</h1>

<details> <summary><h2> 📚 Table of Contents</h2></summary>

- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Implementation Details](#-implementation-details)
  - [Data Normalization](#1--data-normalization)
  - [Outlier Detection](#2--outlier-detection)
  - [K-means Clustering](#3--k-means-clustering)
- [Installation & Usage](#%EF%B8%8F-installation--usage)
- [Learning Outcomes](#-learning-outcomes)
- [Project Information](#-project-information)
- [Contact](#-contact)

</details>

<!-- --- -->

<!-- <details> <summary><h2> 📘 Overview</h2></summary> -->

## 📘 Overview
Implementation of three core data analysis techniques **from scratch** in Python (without scikit-learn):
- **Normalization** — Three methods for scaling data
- **Outlier Detection** — Statistical threshold-based identification  
- **K-Means Clustering** — Manual implementation on Iris dataset

This project demonstrates both algorithmic understanding and practical Python implementation skills.


<!-- > **Project for Data and Information Analysis course**   -->
<!-- > Amirmehdi Zarrinnezhad   -->
<!-- > Amirkabir University of Technology (Tehran Polytechnic)   -->

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/) [![Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange.svg)](https://jupyter.org/) [![License](https://img.shields.io/badge/License-Educational-lightgrey.svg)](#license)

<!-- </details> -->

<!-- --- -->

<!-- <details> <summary><h2> 📂 Project Structure</h2></summary> -->
## 📂 Project Structure

```
Data-and-Information-Analysis-Course/
│
├── Normalizations/
│   └── Normalization.py           # Decimal scaling, Min-Max, and Standard Deviation normalization
│
├── Box Plot/
│   └── box_plot.py                # Outlier detection using ±2σ and ±3σ thresholds
│
├── K-means/
│   ├── iris_data.csv              # Iris dataset for clustering
│   └── k_means.ipynb              # Manual implementation of K-Means algorithm
│
├── Project Description.pdf        # Official course project description
└── Amirmehdi Zarrinnezhad._9731087.pdf  # Final report submission
```
<!-- </details> -->

<!-- --- -->

<!-- <details> <summary><h2> 🔬 Implementation Details</h2></summary> -->
## 🔬 Implementation Details
### 1- Data Normalization
**Goal:** Transform the dataset into comparable scales using different normalization techniques.

**Dataset:** `X = {-5.0, 23.0, 17.6, 7.23, 1.11}`

Three methods implemented:

| Method | Formula | Result Range |
|--------|---------|--------------|
| **Decimal Scaling** | `x' = x / 10^j` | `[-1, 1]` |
| **Min-Max** | `(x - min) / (max - min)` | `[0, 1]` |
| **Z-Score** | `(x - μ) / σ` | Mean=0, Std=1 |

**Example Output:**
```python
Input: [-5.0, 23.0, 17.6, 7.23, 1.11]

Decimal Scaling:    [-0.05, 0.23, 0.176, 0.0723, 0.0111]
Min-Max [0,1]:      [0.0, 1.0, 0.8071, 0.4381, 0.2182]
Z-score:            [-1.2359, 1.5891, 1.0745, 0.0746, -0.5023]
```

📄 **File:** `Normalizations/Normalization.py`

---

### 2- Outlier Detection
**Goal:** Identify and analyze outliers in the dataset using statistical thresholds.

**Dataset:** `C = {3, 1, 0, 2, 7, 3, 6, 4, 2, 0, 0, 10, 15, 6}`

**Methods**
- Computes mean and standard deviation
- Applies multiple thresholds: **±2σ**, **±2.7σ**, **±3σ**
- Includes alternative IQR method (commented)
- Identify upper and lower bounds

**Output:**
- Threshold values and bounds for each sigma level
- List of detected outliers
- Statistical summary (mean, standard deviation)
- box plot visualization

📄 **File:** `Box Plot/box_plot.py`

---

### 3- K-Means Clustering

**Goal:** Implement the **K-Means clustering algorithm** manually to classify data points based on similarity.

**Dataset:** `iris_data.csv` (Iris Flower Dataset)
- **Samples:** 150 iris flowers
- **Features:** Sepal length, Sepal width, Petal length, Petal width (4 features)
- **Classes:** Iris-setosa, Iris-versicolor, Iris-virginica (3 species)

**Algorithm:**

  Random initialization → 2. Calculate centroids → 3. Reassign points → 4. Repeat until convergence

1. **Initialization:** Randomly assign each data point to one of K clusters
2. **Calculate Centroids:** Compute the mean position of all points in each cluster
3. **Reassignment:** Assign each point to the nearest centroid (Euclidean distance)
4. **Convergence Check:** Repeat steps 2-3 until cluster assignments no longer change
5. **Visualization:** Plot clustering results using various feature combinations

**Output:**
- Final cluster centroids
- Number of iterations until convergence
- Visual representation of clustered data
- Comparison with true Iris labels (for validation)

📄 **File:** `K-means/k_means.ipynb`

<!-- </details> -->

<!-- --- -->

<!-- <details> <summary><h2> ⚙️ Installation & Usage</h2></summary> -->


## ⚙️ Installation & Usage

```bash

# Clone the repository
git clone https://github.com/zamirmehdi/Data-and-Information-Analysis-Course.git
cd Data-and-Information-Analysis-Course

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install pandas numpy matplotlib jupyter

# Run implementations
python Normalizations/Normalization.py
python "Box Plot/box_plot.py"
jupyter notebook K-means/k_means.ipynb
```

**Requirements:** Python 3.x, pandas, numpy, matplotlib, jupyter

<!-- </details> -->

<!-- --- -->

<!-- <details> <summary><h2> 🎓 Learning Outcomes</h2></summary> -->
## 🎓 Learning Outcomes

- Statistical analysis (mean, variance, outlier detection)
- Data preprocessing techniques (normalization, scaling)
- Unsupervised learning (K-Means clustering)
- Algorithm implementation from mathematical concepts
- Data visualization with matplotlib
- Working with real datasets (Iris, CSV handling)

<!-- </details> -->

<!-- --- -->

## 📄 Project Information

- **Author**: Amirmehdi Zarrinnezhad
- **Course**: Data and Information Analysis 
- **University**: Amirkabir University of Technology (Tehran Polytechnic) - Fall 2022
<!-- - **Semester**: Fall 2022 -->
<!-- - **Project Link**: [https://github.com/zamirmehdi/Data-and-Information-Analysis-Course](https://github.com/zamirmehdi/Data-and-Information-Analysis-Course) -->

<!--
**Educational License** — Free for learning and academic purposes with attribution.

```
Amirmehdi Zarrinnezhad
Data and Information Analysis Course
Amirkabir University of Technology (Tehran Polytechnic)
``` -->
<!-- © 2024 Amirmehdi Zarrinnezhad — All Rights Reserved. -->

<!-- --- -->

## 📧 Contact

Questions and Collaborations? Please feel free to open an issue or reach out via email or GitHub!  
**📧 Email:** amzarrinnezhad@gmail.com  
**🌐 GitHub:** [@zamirmehdi](https://github.com/zamirmehdi) 

<!-- --- -->

<p align="right">(<a href="#top">back to top</a>)</p>

<div align="center">
⭐ If you found this project helpful, please consider giving it a star! ⭐  
*Amirmehdi Zarrinnezhad*
</div>

