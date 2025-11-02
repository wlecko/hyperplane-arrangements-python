# hyperplane-arrangements-python
Educational project for modeling and visualizing hyperplane arrangements in 1D, 2D, and 3D using Python
# Hyperplane Arrangements Visualization

This project models and visualizes how a system of *n* hyperplanes divides a *d*-dimensional space (for d = 1, 2, or 3).  
It combines **mathematical analysis** with **computational modeling** to verify the general formula for the maximum number of regions formed by hyperplanes in general position:

![formula](https://latex.codecogs.com/png.image?\dpi{150}\color{white}R(n,d)=\sum_{k=0}^{d}\binom{n}{k})

---

## 🎯 Project Objective

The goal of this project is to connect **theoretical combinatorial geometry** with **practical programming** by:

- Demonstrating how hyperplanes partition one-, two-, and three-dimensional space;
- Verifying the correctness of the analytical formula for R(n, d) through computational modeling;
- Creating an educational and interactive visualization tool written in Python.

This project was developed as part of an **individual research project at the HSE Lyceum (2025)**.

---

## 🧮 Mathematical Background

In combinatorial geometry, a central question is:  
> *How many distinct regions are created when n hyperplanes divide a d-dimensional space?*

Examples:
- **1D:** n points divide a line into *n + 1* segments.  
- **2D:** n lines divide the plane into *1 + n + n(n − 1)/2* regions.  
- **3D:** n planes divide space into *1 + n + n(n − 1)/2 + n(n − 1)(n − 2)/6* regions.  

The general case follows the **Zaslavsky formula** shown above, which can also be approximated as:

This formula provides the maximum possible number of regions, assuming the hyperplanes are in general position — that is, no two are parallel and no three (or more) intersect along the same line.

---

## 🧠 How the Program Works

After launch, the program asks the user to select:
1. The **dimension** of the space (1, 2, or 3);
2. The **number of hyperplanes (n)**.

Then it:
- Generates hyperplanes in general position;
- Builds a 1D, 2D, or 3D visualization using **Matplotlib**;
- Calculates the number of regions using the theoretical formula;
- Displays both the visual model and the computed value.

---

## 💻 Usage

### Requirements
Python 3.8 or higher and the following libraries:
```bash
pip install numpy matplotlib
```
Run the program
```bash
python main.py
```
When prompted:
```bash
Enter the space dimension (1, 2 or 3): 2
Enter the number of hyperplanes: 4
```
---

## 🧩 Key Features

- **Multi-dimensional modeling:** supports 1D (points), 2D (lines), and 3D (planes).  
- **Mathematical precision:** automatically computes the number of regions using the exact combinatorial formula *R(n, d) = Σₖ C(n, k)*.  
- **General position handling:** ensures all generated hyperplanes are non-parallel and properly intersecting.  
- **Interactive visualization:** renders real-time geometric configurations using Matplotlib with clear and aesthetic design.  
- **Educational clarity:** the code and outputs are fully documented for students learning geometry, combinatorics, or computer graphics.  
- **Cross-disciplinary relevance:** applicable in fields such as data classification, computational geometry, and mathematical visualization.

---

## 🌐 Repository and Accessibility

The complete source code, example outputs, and setup instructions are publicly available at:  
👉 [https://github.com/wlecko/hyperplane-arrangements-python](https://github.com/wlecko/hyperplane-arrangements-python)

This repository includes:
- A ready-to-run **Python script** (`main.py`) for direct execution
- Clear documentation (`README.md`) explaining the theory and algorithmic logic.

All materials are open access and may be reused for **educational and non-commercial research purposes** with proper citation.

---

## 🧾 License

This project is distributed under the terms of the **MIT License**.  
You are free to use, modify, and share the code for both educational and scientific goals, provided that the original author is acknowledged.  
For detailed conditions, see the [LICENSE](LICENSE) file in this repository.

---

## 👤 Author Information

**Author:** Alex S 
**Affiliation:** Faculty of Informatics, Mathematics and Engineering  
**Institution:** HSE Lyceum, Moscow (2025)  
📧 **Contact:** [fordota2gaming@gmail.com]

---

## 📚 Citation and Academic Reference

If you use this repository or reference its ideas, please include the following citation:

> Alex S (2025). *Hyperplane Arrangements Visualization: Modeling Space Partitioning by n Hyperplanes.*  
> Individual Research Project, HSE Lyceum, Moscow.  
> Available at: [https://github.com/wlecko/hyperplane-arrangements-python](https://github.com/wlecko/hyperplane-arrangements-python)

---

## 💬 Acknowledgments

This project was completed as part of the **Individual Research Program (IRP)** at the HSE Lyceum under the supervision of faculty mentors.  
The author expresses gratitude to the Lyceum’s mathematics and computer science departments for their support in developing this interdisciplinary research that bridges **mathematical theory**, **computational experimentation**, and **educational visualization**.

