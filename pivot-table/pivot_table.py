import numpy as np
import pandas as pd

df = pd.read_csv(
    "/Users/daishinmurooka/Desktop/data-wrangling/pivot-table/Spotify_Youtube_Sample 2.csv"
)

df.info()

df_pivot = df.pivot_table(
    values=["Stream", "official_video"], index=["Artist", "Track"]
)

df_pivot_sorted = df_pivot.sort_values(by=["Stream"], ascending=False)
print(df_pivot_sorted)

df_pivot_A = df_pivot.sort_values(by=["Stream", "Artist"], ascending=False).loc[
    ["Coldplay", "The Beatles"]
]

print(df_pivot_A)
