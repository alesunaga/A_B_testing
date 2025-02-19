# A/B Testing Analysis of Marketing Campaign

# Import necessary libraries
import pandas as pd  # For data manipulation
import numpy as np   # For numerical operations (not used extensively here, but good practice)
from scipy.stats import chi2_contingency  # For Chi-squared test
from scipy.stats import binom_test  # For Binomial test
# codecademylib3 -  Note: The purpose of this library is unclear.  If it's a custom library,
#                  please include it in the repository or explain its functionality.  If it's
#                  not necessary, consider removing it.

# Read the data from the 'clicks.csv' file into a pandas DataFrame
abdata = pd.read_csv('clicks.csv')

# 1. Inspect the data: Print the first few rows to understand its structure
print(abdata.head())

# 2. Create a contingency table to summarize the relationship between 'group' and 'is_purchase'
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)

# 3. Perform a Chi-squared test to check for association between 'group' and 'is_purchase'
chi2, pval, dof, expected = chi2_contingency(Xtab)
print(f"Chi-squared p-value: {pval}")  # Print the p-value

# 4. Calculate the total number of visits (users)
num_visits = len(abdata.user_id)
print(f"Total visits: {num_visits}")

# 5. Calculate the number of sales needed to reach a revenue target of $1000 for each price point
#    ($0.99, $1.99, $4.99)
num_sales_needed_099 = 1000 / 0.99
num_sales_needed_199 = 1000 / 1.99
num_sales_needed_499 = 1000 / 4.99

# 6. Calculate the proportion of sales needed relative to the total number of visits
p_sales_needed_099 = num_sales_needed_099 / num_visits
p_sales_needed_199 = num_sales_needed_199 / num_visits
p_sales_needed_499 = num_sales_needed_499 / num_visits

# 7. Calculate the actual number of purchases and sample size for each group
samp_size_099 = len(abdata[abdata['group'] == 'A'])
samp_size_199 = len(abdata[abdata['group'] == 'B'])
samp_size_499 = len(abdata[abdata['group'] == 'C'])

sales_099 = len(abdata[(abdata['group'] == 'A') & (abdata['is_purchase'] == 'Yes')])
sales_199 = len(abdata[(abdata['group'] == 'B') & (abdata['is_purchase'] == 'Yes')])
sales_499 = len(abdata[(abdata['group'] == 'C') & (abdata['is_purchase'] == 'Yes')])

print(f"Sales in group C ($4.99): {sales_499}") # More descriptive output

# 8. Perform binomial tests to compare observed purchase rates with target rates
pvalueA = binom_test(x=sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater')
print(f"Binomial test p-value for group A: {pvalueA}")

pvalueB = binom_test(x=sales_199, n=samp_size_199, p=p_sales_needed_199, alternative='greater')
print(f"Binomial test p-value for group B: {pvalueB}")

pvalueC = binom_test(x=sales_499, n=samp_size_499, p=p_sales_needed_499, alternative='greater')
print(f"Binomial test p-value for group C: {pvalueC}")


# Potential Improvements (as mentioned before):
# - More descriptive variable names (e.g., sales_group_a instead of sales_099)
# - More detailed comments explaining the business context and the meaning of the results
# - A function to perform the binomial test for each group to avoid code duplication
# - Data visualization to make the results easier to interpret
# - Explicitly state the null and alternative hypotheses for each test.
