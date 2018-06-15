#!/usr/bin/env python
import pandas as pd

# columns:
# Name,Position Title,Department,Employee Annual Salary
df = pd.read_csv(
    "../DATA/city-of-chicago-salaries.csv"
)

print(df.memory_usage(deep=True))
print()

df = pd.read_csv(
    "../DATA/city-of-chicago-salaries.csv",
    dtype={"Position Title": "category", "Department": "category"}
)
print(df.memory_usage(deep=True))
print()

print(df.head())
print()

#TODO: convert Name column to two separate colummns and set to category

