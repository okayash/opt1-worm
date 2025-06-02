import pandas as pd

df = pd.DataFrame.from_csv(
    "male_full_edgelist.csv",
)

print(len(set([row.strip() for row in df.Target])))
