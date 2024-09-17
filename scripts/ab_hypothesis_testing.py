# scripts/ab_hypothesis_testing.py

import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind

def load_data(path):
    # Utility function to load data from a CSV file
    df = pd.read_csv(path)
    return df

def chi_square_test(df, col1, col2):
    # Perform Chi-Square Test
    cross_tab = pd.crosstab(df[col1], df[col2])
    chi2, p_value, _, _ = chi2_contingency(cross_tab)
    
    if p_value < 0.05:
        return f'Reject the Null Hypothesis: Significant association between {col1} and {col2}.'
    else:
        return f'Fail to Reject the Null Hypothesis: No significant association between {col1} and {col2}.'

def t_test(df, group_col, value_col, group_a, group_b):
    # Perform T-Test
    group_a_vals = df[df[group_col] == group_a][value_col]
    group_b_vals = df[df[group_col] == group_b][value_col]
    t_stat, p_value = ttest_ind(group_a_vals, group_b_vals)
    
    if p_value < 0.05:
        return f'Reject the Null Hypothesis: Significant difference in {value_col} between {group_a} and {group_b}.'
    else:
        return f'Fail to Reject the Null Hypothesis: No significant difference in {value_col} between {group_a} and {group_b}.'

# Example usage
if __name__ == "__main__":
    df = load_data('../data/my_data.csv')
    
    # Example: Chi-Square Test (Risk differences across provinces)
    print(chi_square_test(df, 'Province', 'StatutoryRiskType'))
    
    # Example: T-Test (Margin differences between zip codes)
    print(t_test(df, 'ZipCode', 'TotalPremium', 'Zip_A', 'Zip_B'))
