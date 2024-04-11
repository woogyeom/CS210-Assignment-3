import pandas as pd


# Load the data into a DataFrame
df = pd.read_excel("GooglePlaystore.xlsx")

# Task 1: Remove record with "Reviews" value "3.0M"
df = df[df["Reviews"] != "3.0M"]

# Task 2: Remove rows with "Varies with device"
df = df[~df.eq("Varies with device").any(axis=1)]

# Task 3: Convert values in Android version column to floats
df["Android Ver"] = df["Android Ver"].str.extract(r"(\d+\.\d+)", expand=False).astype(float)

# Task 4: Convert Installs column to integers
df["Installs"] = df["Installs"].str.replace(",", "").str.rstrip("+").astype(int)

# Task 5: Handle missing ratings
rating_avg = df.groupby("Category")["Rating"].transform("mean")
df["Rating"] = df["Rating"].fillna(round(rating_avg, 2))

# Task 6: Preprocess the Size column
size_mapping = {"M": 1000000, "K": 1000}
df["Size"] = df["Size"].replace(size_mapping, regex=True).str.extract(r"([\d.]+)", expand=False).astype(float)

df.to_excel("result2.xlsx", index=False)
