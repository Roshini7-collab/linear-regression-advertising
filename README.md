# Linear Regression Advertising Analysis

## 📌 Overview
This project implements a **modular and installable Python package** for linear regression analysis using an advertising dataset.  
The goal is to demonstrate **reproducible research practices**, clean software structure, and proper evaluation workflows.

The project is suitable for:
- Statistics and data science learners
- Research-oriented machine learning workflows
- GitHub portfolio demonstration

---

## 📂 Project Structure

linear_regression_advertising/
│
├── linear_regression/ # Core Python package
│ ├── data_loader.py
│ ├── model.py
│ ├── evaluation.py
│ ├── visualization.py
│ └── init.py
│
├── scripts/
│ └── run_regression.py # End-to-end pipeline script
│
├── notebooks/
│ └── LinearRegression.ipynb
│
├── data/
│ └── advertising.csv
│
├── setup.py
├── requirements.txt
└── README.md

---

## 📊 Dataset
The dataset contains advertising expenditure and corresponding sales:

- **TV**: TV advertising budget
- **Radio**: Radio advertising budget
- **Newspaper**: Newspaper advertising budget
- **Sales**: Product sales

---

## ⚙️ Installation

Clone the repository and install the package in editable mode:

pip install -e .

## How to Run

Execute the full regression pipeline using:

python scripts/run_regression.py


This will:

**Load the dataset**

**Train a linear regression model**

**Evaluate performance using RMSE and R²**

## Example Output
{'MSE': 2.90, 'RMSE': 1.70, 'R2': 0.91}

### Author

Roshini Priya C H
MSc Statistics | Research-oriented Machine Learning