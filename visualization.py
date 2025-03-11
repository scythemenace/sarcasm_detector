import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("ground_labels.csv")  # Replace with your file path

# Count occurrences of each label
label_counts = df['label'].value_counts()

# Plot pie chart
plt.figure(figsize=(6, 6))
plt.pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', colors=['lightblue', 'salmon'], startangle=140)
plt.title("Distribution of Sarcastic and Not-Sarcastic Labels")
plt.savefig("pie_chart.png")
plt.show()