# Insurance_Industry_Analytics-and-Predictive-modeling

#Overview
#This project involves exploratory data analysis (EDA), A/B hypothesis testing, and statistical modeling of an insurance dataset. The goal is to extract insights about premium and claim trends, evaluate geographical and demographic differences, and build predictive models to help improve decision-making in the insurance industry.

Key Features
Data Summarization: Provides descriptive statistics, data structure review, and missing values assessment.
Exploratory Data Analysis (EDA): Univariate and multivariate analysis including histograms, scatter plots, and correlation matrices.
A/B Hypothesis Testing: Statistical tests (Chi-squared, t-tests) to evaluate key hypotheses such as risk and profit differences across various segments.
Statistical Modeling: Linear Regression, Random Forest, and XGBoost models for predicting Total Premium and Total Claims.
Model Interpretability: Feature importance analysis using SHAP/LIME to understand which factors contribute most to predictions.
Project Structure
lua
Copy code
|-- app/
|   |-- main.py                    # Streamlit app (if applicable)
|-- notebooks/
|   |-- exploratory_analysis.ipynb  # Jupyter notebook for EDA
|-- scripts/
|   |-- data_summarization.py       # Data summarization script
|   |-- ab_hypothesis_testing.py    # A/B hypothesis testing script
|   |-- statistical_modeling.py     # Statistical modeling script
|   |-- utils.py                    # Utility functions
|-- tests/
|   |-- test_ab_testing.py          # Unit tests for hypothesis testing
|   |-- test_modeling.py            # Unit tests for model evaluation
|-- data/
|   |-- your_data.csv               # Dataset
|-- README.md
|-- requirements.txt                # Python dependencies
How to Run
Clone this repository.
Install required dependencies using:
Copy code
pip install -r requirements.txt
Run the individual scripts for data summarization, A/B hypothesis testing, and statistical modeling by navigating to the scripts folder:
bash
Copy code
python scripts/data_summarization.py
python scripts/ab_hypothesis_testing.py
python scripts/statistical_modeling.py
Contributions
Feel free to contribute by creating issues or submitting pull requests.

