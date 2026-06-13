# NayePankh Foundation - Data Analytics Internship Project 🕊️

This project provides a complete, end-to-end Data Analytics pipeline and dashboard tailored for the NayePankh Foundation. It is designed to demonstrate full-stack data proficiency for an internship application.

## 🚀 Setup & Execution Instructions

### 1. Install Dependencies
Make sure you have Python installed. Install the required libraries using pip:
```bash
pip install -r requirements.txt
```

### 2. Generate the Mock Dataset
Run the data generation script. This creates a realistic, 12-month mock dataset reflecting social media engagement and website metrics.
```bash
python generate_data.py
```
*(This will generate `data/nayepankh_data_12_months.csv`)*

### 3. Exploratory Data Analysis & Visualizations
Execute this script to print EDA statistics, calculate correlation matrices, and output high-quality visualizations into the `output_plots/` folder.
```bash
python analysis.py
```

### 4. Interactive Dashboard
Launch the interactive web dashboard powered by Streamlit and Plotly.
```bash
streamlit run dashboard.py
```
*(A browser window will open automatically, allowing you to filter data and view KPIs).*

### 5. Generate Automated Report
Run this script to automatically compile key insights and output a Markdown report for the latest month's performance, suitable for emailing to NGO leadership.
```bash
python report_generator.py
```

## 📂 Project Structure
- `generate_data.py`: Script using Pandas & NumPy to simulate non-profit metrics.
- `analysis.py`: Performs EDA and outputs Matplotlib/Seaborn charts.
- `dashboard.py`: A Streamlit app containing interactive KPI metrics and Plotly charts.
- `report_generator.py`: Generates automated monthly markdown reports.
- `requirements.txt`: Python package dependencies.
