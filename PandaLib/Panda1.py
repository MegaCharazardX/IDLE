import pandas as pd
import numpy as np

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Print the DataFrame
print(df)
dfxl_path = "Trial.xlsx"
df.to_excel(dfxl_path)

