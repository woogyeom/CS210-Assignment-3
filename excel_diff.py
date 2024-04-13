import pandas as pd

df1 = pd.read_excel('GooglePlaystore_afterprep5.xlsx')
df2 = pd.read_excel('GooglePlaystore_cleaned5.xlsx')

# in_df1_not_in_df2 = df1[~df1.index.isin(df2.index)]
# in_df2_not_in_df1 = df2[~df2.index.isin(df1.index)]

# print("Rows that only I have:")
# print(in_df1_not_in_df2)

# print("\nRows that only Jasmit has:")
# print(in_df2_not_in_df1)

for idx, row1 in df1.iterrows():
    row2 = df2.iloc[idx]
    if not row1.equals(row2):
        print("File 1:")
        print(row1)
        print()
        print("File 2:")
        print(row2)
        break