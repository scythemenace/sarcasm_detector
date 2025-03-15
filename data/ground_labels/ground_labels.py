import pandas as pd

# Load CSV files
df1 = pd.read_csv("data_1.csv")
df2 = pd.read_csv("data_2.csv")

# Merge on 'text' column
merged = df1.merge(df2, on="text", how="inner", suffixes=("_file1", "_file2"))

# saving the dataframe
same_text_label = merged[merged["label_file1"] == merged["label_file2"]]

df = same_text_label.drop('label_file1', axis=1)

df = df.rename(columns={'label_file2': 'label'})

# saving the dataframe
df.to_csv('ground_labels.csv')

df_ground = pd.read_csv("test.csv")

df_ground = df_ground.drop('label_file2', axis=1)
df_ground = df_ground.rename(columns={'label_file1': 'label'})

combined_csv = pd.concat([df_ground, df], ignore_index=True)

combined_csv = combined_csv.drop('Unnamed: 0', axis=1)

combined_csv.to_csv('ground_labels2.csv',index=False)
