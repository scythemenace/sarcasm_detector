import praw
import csv
import pandas as pd

reddit = praw.Reddit(
    client_id="4vMXBeeBinRuBCS66IQSPg",
    client_secret="TKrISvck9wtLC2-tFvlYib9ij69xSQ",
    user_agent="script:sarcasm_detector:v1.0.0 (by u/Parking-Jump-1723)",
)

# print(reddit.read_only)

data = []


for submission in reddit.subreddit("TheOnion").top(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("TheOnion").hot(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("TheOnion").new(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("TheOnion").controversial(limit=1000):
    data.append({"text": submission.title, "label": ""})

# --------------------------------------------------------------

for submission in reddit.subreddit("nottheonion").top(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("nottheonion").hot(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("nottheonion").new(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("nottheonion").controversial(limit=1000):
    data.append({"text": submission.title, "label": ""})

# --------------------------------------------------------------


for submission in reddit.subreddit("bbc").top(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("bbc").hot(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("bbc").new(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("bbc").controversial(limit=1000):
    data.append({"text": submission.title, "label": ""})

# --------------------------------------------------------------

for submission in reddit.subreddit("clevercomebacks").top(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("clevercomebacks").hot(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("clevercomebacks").new(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("clevercomebacks").controversial(limit=1000):
    data.append({"text": submission.title, "label": ""})

# --------------------------------------------------------------

for submission in reddit.subreddit("cnn").top(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("cnn").hot(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("cnn").new(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("cnn").controversial(limit=1000):
    data.append({"text": submission.title, "label": ""})

# --------------------------------------------------------------

for submission in reddit.subreddit("PrivateEye").top(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("PrivateEye").hot(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("PrivateEye").new(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("PrivateEye").controversial(limit=1000):
    data.append({"text": submission.title, "label": ""})

# --------------------------------------------------------------


for submission in reddit.subreddit("Clickhole").top(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("Clickhole").hot(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("Clickhole").new(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("Clickhole").controversial(limit=1000):
    data.append({"text": submission.title, "label": ""})

# --------------------------------------------------------------

for submission in reddit.subreddit("worldnews").top(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("worldnews").hot(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("worldnews").new(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("worldnews").controversial(limit=1000):
    data.append({"text": submission.title, "label": ""})

# --------------------------------------------------------------

for submission in reddit.subreddit("TheBabylonBee").top(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("TheBabylonBee").hot(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("TheBabylonBee").new(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("TheBabylonBee").controversial(limit=1000):
    data.append({"text": submission.title, "label": ""})

# --------------------------------------------------------------

for submission in reddit.subreddit("politics").top(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("politics").hot(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("politics").new(limit=1000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("politics").controversial(limit=1000):
    data.append({"text": submission.title, "label": ""})

# --------------------------------------------------------------


with open("dataset.csv", "w", newline="") as csvfile:
    fieldnames = ["text", "label"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Read CSV
df = pd.read_csv("dataset.csv")

# For complete row duplicate
df.drop_duplicates(inplace=True)

# Remove text with more than 300 characters
df = df[df["text"].str.len() < 300]

# Remove text with less than 4 words
df = df[df["text"].str.split().str.len() > 4]

# Save then
df.to_csv("data.csv", index=False)
