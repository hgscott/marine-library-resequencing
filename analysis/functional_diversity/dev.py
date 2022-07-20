# How to make a matrix from multiple lists
import pandas as pd

A = ['I', 'love', 'flowers']
B = ['I', 'want', 'flowers']
C = ['I', 'love', 'butterflies']

# Make an empty pandas dataframe
df = pd.DataFrame()

# Add A
# Make a column for A
df['A'] = []
for element in A:
    if element in df.index:
        print("idk")
    # else:


# Test
print(df)
