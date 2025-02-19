# A/B Testing Analysis of Marketing Campaign

This repository contains a Python script for analyzing the results of an A/B test for a marketing campaign. The goal is to determine if different pricing strategies (represented by groups A, B, and C) have a statistically significant impact on purchase rates.

## Project Overview

The script reads data from a `clicks.csv` file, which presumably contains information about user interactions with different versions of a marketing campaign.  It then performs statistical analysis to compare the purchase rates across the different groups.

## Code Description

The script is structured as follows:

1. **Import Libraries:** Imports necessary libraries for data manipulation (pandas, numpy), statistical analysis (scipy.stats), and potentially custom libraries (codecademylib3 - though its specific use isn't clear from this snippet).

2. **Load Data:** Reads the data from `clicks.csv` into a pandas DataFrame called `abdata`.

3. **Data Inspection:** Prints the first few rows of the DataFrame to get an initial overview of the data.

4. **Contingency Table:** Creates a contingency table (`Xtab`) to summarize the relationship between the `group` (A, B, or C) and `is_purchase` (Yes/No). This table is crucial for the Chi-squared test.

5. **Chi-squared Test:** Performs a Chi-squared test of independence to determine if there's a statistically significant association between the pricing group and purchase behavior.  The p-value is printed to assess significance.

6. **Calculate Number of Visits:** Calculates the total number of user visits.

7. **Calculate Sales Needed:** Calculates the number of sales needed to achieve a certain revenue target (1000) for each price point ($0.99, $1.99, $4.99).

8. **Calculate Sales Proportion:** Calculates the proportion of sales needed relative to the total number of visits. This represents the target purchase rate for each group.

9. **Calculate Purchases and Sample Sizes for each Group:** Determines the actual number of purchases and sample size for each group.

10. **Binomial Tests:** Performs binomial tests to compare the observed purchase rates in each group with the target purchase rates calculated earlier. The `alternative = 'greater'` argument indicates that the tests are one-sided, checking if the observed purchase rates are *greater* than the target rates. The p-values for each test are printed.

## Running the Code

1.  Make sure you have the necessary libraries installed. You can install them using pip:
    ```bash
    pip install pandas numpy scipy
    ```
    If you're using `codecademylib3`, ensure it is available in your environment. If it's a custom library, include it in your project.

2.  Place the `clicks.csv` file in the same directory as the Python script.

3.  Run the script:
    ```bash
    python your_script_name.py
    ```

## Interpretation of Results

The script outputs several values:

*   **Contingency Table:** Shows the distribution of purchases across different groups.
*   **Chi-squared p-value:** Indicates whether there's a statistically significant association between group and purchase behavior. A small p-value (typically less than 0.05) suggests a significant association.
*   **Binomial test p-values:** For each group, these p-values indicate whether the observed purchase rate is significantly greater than the target rate.  Again, a small p-value suggests that the observed rate is significantly higher.

By analyzing these outputs, you can draw conclusions about the effectiveness of the different pricing strategies.

## Potential Improvements

*   **Clearer Variable Names:**  More descriptive variable names (e.g., `sales_group_a` instead of `sales_099`) would improve readability.
*   **Comments:** Adding more comments explaining the logic behind each step would be beneficial.
*   **Function for Binomial Test:** Encapsulating the binomial test logic in a function would make the code more modular and reusable.
*   **Visualization:** Creating visualizations (e.g., bar charts) of the purchase rates would make it easier to understand the results.
*   **Hypothesis Testing Framework:** Explicitly stating the null and alternative hypotheses for each test would make the analysis more rigorous.
*   **Handling of `codecademylib3`:** Clarify the purpose and usage of this library.  If it's not essential, remove it.

This documentation should help you get your code onto GitHub. Remember to replace `"your_script_name.py"` with the actual name of your file.  You can also expand on this documentation with more details about your specific campaign and the context of the A/B test.
