import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./(0603)01_gyousei-danjyo-setai.csv")
# print(df.head())


women_IQR = df["女"].quantile(0.75) - df["女"].quantile(0.25)
women_low_limit = df["女"].quantile(0.25) - 1.5 * women_IQR
print(df["女"].quantile(0.25))
print(women_low_limit)

df[df["女"] < women_low_limit]

df.drop(df[df["女"] < women_low_limit].index, inplace=True)
df.dropna(inplace=True)
df.sort_values("女", inplace=True, ascending=False)
print(df)
