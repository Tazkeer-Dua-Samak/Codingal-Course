import numpy as np
import pandas as pd

data = {
    'Id': [1,2,3,4],
    'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'Role': ['CEO', np.nan, np.nan, np.nan],
    'Salary': [100, 200, np.nan, np.nan]
}

df = pd.DataFrame(data)

print("\nOriginal Data Frame: \n")
print(df)

print("\nFirst two rows: \n")
print(df.head(2))

print("\nLast two rows: \n")
print(df.tail(2))

print("\nTotal number of NULL values: \n")
print(df.isnull().sum().sum())

print("\nData Frame info: \n")
print(df.info())

df_drop_rows = df.dropna()
print("Data Frame after dropping NULL rows: \n")
print(df_drop_rows)

df_drop_columns = df.dropna(axis=1)
print("Data Frame after dropping NULL columns: \n")
print(df_drop_columns)

df_salary_filled = df.copy()
df_salary_filled['Salary'].fillna(300, inplace = True)
print("Data Frame after filling NULL Salary with 300: \n")
print(df_salary_filled)

df_role_filled = df_salary_filled.copy()
df_role_filled['Role'].fillna('CEO', inplace = True)
print("Data Frame after filling NULL Role with CEO: \n")
print(df_role_filled)