import pandas as pd
import numpy as np

df = pd.read_csv("ds-salaries.csv")
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df["job_title"].value_counts())
# print(df["job_title"].unique())
# print(df["job_title"].nunique())

company_locatiion = pd.DataFrame(
    {"company_location": df["company_location"].value_counts()}
)
# print(company_locatiion)

col = "salary"
min = df[col].min()
max = df[col].max()
median = df[col].median()
mode = df[col].mode()[0]
midrange = (max - min) / 2
# print(
#     "col:",
#     col,
#     "\n\tmin:",
#     min,
#     "max:",
#     max,
#     "median:",
#     median,
#     "mode:",
#     mode,
#     "midrange:",
#     midrange,
# )


def getDispersion(col):
    range = df[col].max() - df[col].min()
    quantiles = df[col].quantile([0.25, 0.5, 0.75])
    IQR = quantiles[0.75] - quantiles[0.25]
    var = df[col].var()
    std = df[col].std()
    print(
        "col:",
        col,
        "\n\trange:",
        range,
        "Q1:",
        quantiles[0.25],
        "Q2:",
        quantiles[0.5],
        "Q3:",
        quantiles[0.75],
        "IQR:",
        IQR,
        "var:",
        var,
        "std:",
        std,
    )


numericalcols = ["salary", "remote_ratio"]

for cols in numericalcols:
    getDispersion(cols)

print(df[numericalcols].corr())
