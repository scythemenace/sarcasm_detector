import pandas as pd

# Load CSV files
df1 = pd.read_csv("data_1.csv")
df2 = pd.read_csv("data_2.csv")

# Merge on 'text' column
merged = df1.merge(df2, on="text", how="inner", suffixes=("_file1", "_file2"))

# Count where text is the same
same_text_count1 = merged.shape[0]

# Count where text and label are the same
same_text_label_count1 = merged[merged["label_file1"] == merged["label_file2"]].shape[0]

print("Data 1 and Data 2 User Agreement --->")
print("Number of rows where text is the same:", same_text_count1)
print("Number of rows where text and label are the same:", same_text_label_count1)
print("User Agreement : ", same_text_label_count1 / same_text_count1)
print()

# Load CSV files
df1 = pd.read_csv("data_3.csv")
df2 = pd.read_csv("data_4.csv")

# Merge on 'text' column
merged = df1.merge(df2, on="text", how="inner", suffixes=("_file1", "_file2"))

# Count where text is the same
same_text_count = merged.shape[0]

# Count where text and label are the same
same_text_label_count = merged[merged["label_file1"] == merged["label_file2"]].shape[0]

print("Data 3 and Data 4 User Agreement --->")
print("Number of rows where text is the same:", same_text_count)
print("Number of rows where text and label are the same:", same_text_label_count)
print("User Agreement : ", same_text_label_count / same_text_count)
print()

print("Overall User Agreement --->")
print("Number of rows where text is the same:", same_text_count + same_text_count1)
print("Number of rows where text and label are the same:", same_text_label_count + same_text_label_count1)
print("User Agreement : ", (same_text_label_count + same_text_label_count1) / (same_text_count + same_text_count1))