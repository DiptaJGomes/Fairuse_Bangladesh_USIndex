import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# Load the dataset
df = pd.read_csv('fair_use_cases.csv')

# Display the first few rows and dataset info for exploratory analysis
print(df.head())
print(df.info())
print(df.describe())

# Compare fair use outcomes across jurisdictions
plt.figure(figsize=(10, 6))
sns.countplot(x='court', hue='fair_use_found', data=df)
plt.title('Fair Use Outcomes by Jurisdiction')
plt.xlabel('Court')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.legend(title='Fair Use Found')
plt.show()

# Test for significant differences in fair use outcomes across jurisdictions
court_outcome_table = pd.crosstab(df['court'], df['fair_use_found'])
chi2, p_value, dof, expected = chi2_contingency(court_outcome_table)
print(f'Chi-square statistic: {chi2:.2f}')
print(f'P-value: {p_value:.4f}')
if p_value < 0.05:
    print('There is a significant difference in fair use outcomes across jurisdictions.')
else:
    print('There is no significant difference in fair use outcomes across jurisdictions.')

# Compare fair use outcomes across time periods
df['time_period'] = pd.cut(df['year'], bins=[-1, 1990, 2000, 2010, 2020, 2030], labels=['1980s', '1990s', '2000s', '2010s', '2020s'])
plt.figure(figsize=(10, 6))
sns.countplot(x='time_period', hue='fair_use_found', data=df)
plt.title('Fair Use Outcomes by Time Period')
plt.xlabel('Time Period')
plt.ylabel('Count')
plt.legend(title='Fair Use Found')
plt.show()

# Test for significant differences in fair use outcomes across time periods
time_period_outcome_table = pd.crosstab(df['time_period'], df['fair_use_found'])
chi2, p_value, dof, expected = chi2_contingency(time_period_outcome_table)
print(f'Chi-square statistic: {chi2:.2f}')
print(f'P-value: {p_value:.4f}')
if p_value < 0.05:
    print('There is a significant difference in fair use outcomes across time periods.')
else:
    print('There is no significant difference in fair use outcomes across time periods.')

# Compare fair use outcomes across categories
plt.figure(figsize=(10, 6))
sns.countplot(x='categories', hue='fair_use_found', data=df)
plt.title('Fair Use Outcomes by Copyrighted Work Type')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.legend(title='Fair Use Found')
plt.show()

# Test for significant differences in fair use outcomes across categories
category_outcome_table = pd.crosstab(df['categories'], df['fair_use_found'])
chi2, p_value, dof, expected = chi2_contingency(category_outcome_table)
print(f'Chi-square statistic: {chi2:.2f}')
print(f'P-value: {p_value:.4f}')
if p_value < 0.05:
    print('There is a significant difference in fair use outcomes across categories.')
else:
    print('There is no significant difference in fair use outcomes across categories.')
