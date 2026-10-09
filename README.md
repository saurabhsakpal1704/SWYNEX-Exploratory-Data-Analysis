# SWYNEX Exploratory Data Analysis

## Task 2 — Exploratory Data Analysis

This repository is a complete submission template for **SWYNEX Task 2: Exploratory Data Analysis** using the prepared **UCI Adult Census Income** dataset from Task 1.

### Objective

- Inspect the prepared dataset
- Verify data quality
- Perform descriptive statistics
- Analyze numerical and categorical variables
- Study the income target distribution
- Create visualizations
- Identify at least five insights that can influence a machine-learning model or decision

## Project structure

```text
SWYNEX-Exploratory-Data-Analysis/
├── data/
│   └── processed/
│       └── adult_cleaned.csv        <-- put your Task 1 file here
├── notebooks/
│   └── SWYNEX_Exploratory_Data_Analysis.ipynb
├── reports/
│   └── EDA_Insights.md
├── visuals/
├── src/
│   └── eda_analysis.py
├── .gitignore
├── requirements.txt
└── README.md
```

## How to run

### 1. Create environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 2. Install packages

```bash
pip install -r requirements.txt
```

### 3. Add the Task 1 dataset

Copy your cleaned file into:

```text
data/processed/adult_cleaned.csv
```

### 4. Run the notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/SWYNEX_Exploratory_Data_Analysis.ipynb
```

Run all cells from top to bottom.

## Important

The notebook automatically detects common Adult dataset column names and normalizes names such as:

- `age`
- `education`
- `occupation`
- `workclass`
- `hours-per-week`
- `capital-gain`
- `income`

If your Task 1 preprocessing renamed a column, the notebook attempts to detect the equivalent column automatically.

## Deliverables

The notebook creates:

- data-quality summary
- descriptive statistics
- target distribution
- age analysis
- education vs income analysis
- working-hours analysis
- occupation analysis
- capital-gain analysis
- correlation heatmap
- outlier/skewness analysis
- automatic five-plus insight candidates
- PNG visualizations

## Technologies

Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter.

## Author

Saurabh Sakpal

## Internship

SWYNEX Technologies — Data Science Internship
