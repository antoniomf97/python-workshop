"""
Python Libraries - Pandas

https://pandas.pydata.org/
"""


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# s = pd.Series([1, 3, 5, 7, 6, 8, 10, 12, 13, 17], dtype="int32")

# print(s)
# print()
# print(s.index)
# print()
# print(s.sum())
# print()

# s1 = pd.Series([5, -2, -5, 1, 6, -13, 1, 1, -2, -5, -7], dtype="int32")

# print(s + s1)
# print()

# dates = pd.date_range("20130101", periods=15)

# df = pd.DataFrame(np.random.randn(15, 4), index=dates, columns=["A", "B", "C", "D"])

# print(df)
# print()
# print(df["A"])
# print()
# print(df.loc["2013-01-03"])
# print(df.iloc[2])

# df.plot(figsize=(12, 5), style='o-')
# plt.grid()
# plt.show()


# df1 = pd.read_csv("./files/movies.csv")
# print(df1)
# print()

# df2 = df1.loc[df1["year"] >= 1985]
# print(df2)
# print()

# df3 = df1.loc[df1["runtime"] >= 100]
# print(df3)