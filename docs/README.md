# Dataset Information

## Disclaimer

This dataset may contain abusive or foul language, inappropriate jokes, or other offensive content. The data is collected from various online sources and is provided as-is. Users should exercise discretion when using this dataset.

## Raw Data

The raw data was gathered from multiple subreddits using the Reddit API via the `praw` library. Specifically, data was collected from the following subreddits:

- `TheOnion`
- `nottheonion`
- `bbc`
- `clevercomebacks`
- `cnn`
- `PrivateEye`
- `Clickhole`
- `worldnews`
- `TheBabylonBee`
- `politics`

Posts were extracted from different sorting categories (`top`, `hot`, `new`, and `controversial`), and the dataset was cleaned to remove duplicate entries, excessively long posts, and posts with fewer than four words.

## Data

The dataset consists of text data extracted from Reddit posts. Each entry contains:

- `text`: The title of the Reddit post.
- `label`: This field is currently empty and will be replaced with the labels by the annotator ,the labels are Sarcastic or Not-Sarcastic.

## Segments

The dataset is divided into eight CSV files (`data_1.csv` to `data_8.csv`).

- `data_1.csv` and `data_2.csv` share 192 common entries, with 48 unique entries in each.
- `data_3.csv` and `data_4.csv` share 96 common entries, with 144 unique entries in each.
- `data_5.csv` to `data_8.csv` each contain 240 unique entries.

This segmentation ensures a structured distribution of data for the 15% common data overall to to calculate annotator agreement.

## Additional Information

- Use of AI : For this stage of the project, AI/ChatGPT was used for three queries-> one to generate a template for the annotation guidelines and two for the README.md file. Given that the estimated carbon footprint per query is 4.32g CO₂, the total emissions for these queries amount to approximately 12.96g .
- Contact Information :
  - Devansh Singh : Through email (singhd80@mcmaster.ca) or teams direct message.
  - Ankur Pandey : Through email (pandea23@mcmaster.ca) or teams direct message.
