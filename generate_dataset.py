import praw
import csv

reddit = praw.Reddit(
    client_id="4vMXBeeBinRuBCS66IQSPg",
    client_secret="TKrISvck9wtLC2-tFvlYib9ij69xSQ",
    user_agent="script:sarcasm_detector:v1.0.0 (by u/Parking-Jump-1723)",
)

# print(reddit.read_only)

data = []
processed_data = []

for submission in reddit.subreddit("nottheonion").top(limit=5000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("bbc").top(limit=6000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("clevercomebacks").top(limit=5000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("cnn").top(limit=6000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("PrivateEye").top(limit=2000):
    data.append({"text": submission.title, "label": ""})

for submission in reddit.subreddit("Clickhole").top(limit=2000):
    data.append({"text": submission.title, "label": ""})


for d in data:
    if d not in processed_data:
        if len(d["text"]) < 300 and len(d["text"].split(" ")) > 4:
            processed_data.append(d)


with open("dataset.csv", "w", newline="") as csvfile:
    fieldnames = ["text", "label"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(processed_data)
