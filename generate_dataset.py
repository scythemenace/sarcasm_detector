import praw
import csv

reddit = praw.Reddit(
    client_id="4vMXBeeBinRuBCS66IQSPg",
    client_secret="TKrISvck9wtLC2-tFvlYib9ij69xSQ",
    user_agent="script:sarcasm_detector:v1.0.0 (by u/Parking-Jump-1723)",
)

# print(reddit.read_only)

data = []

for submission in reddit.subreddit("nottheonion").top(limit=2500):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("nottheonion").hot(limit=2500):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("bbc").top(limit=3000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("bbc").hot(limit=3000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("clevercomebacks").top(limit=2500):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("clevercomebacks").hot(limit=2500):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("cnn").top(limit=3000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("cnn").hot(limit=3000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("PrivateEye").top(limit=500):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("PrivateEye").hot(limit=500):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("Clickhole").top(limit=500):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("Clickhole").hot(limit=500):
    data.append({"text": submission.title, "label": ""})


with open("dataset.csv", "w", newline="") as csvfile:
    fieldnames = ["text", "label"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
