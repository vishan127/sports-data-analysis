import pandas as pd

# Sample dataset
data = {
    'Player': ['LeBron James', 'Kevin Durant', 'Stephen Curry'],
    'Points Per Game': [27.2, 26.5, 24.3]
}

df = pd.DataFrame(data)

# Print stats
print(df)
