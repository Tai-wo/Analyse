def generate_python_code(file_path: str):

    code = f"""
import pandas as pd

df = pd.read_csv('{file_path}')

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.fillna(method='ffill')

print(df.head())
"""

    return code