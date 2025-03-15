# Sarcasm Detection NLP Project

## Project Overview

This project aims to build a sarcasm detection model using Natural Language Processing (NLP). The dataset was collected manually from various subreddits, annotated by peers, and validated for consistency. The final dataset was used to train and evaluate different models, establishing baselines and exploring performance improvements.

## Dataset Collection

Data was collected from subreddits that do not explicitly indicate sarcasm (e.g., `r/nottheonion`, `r/clevercomebacks`, `r/bbc`, `r/cnn`). The data was retrieved using PRAW (Reddit API) and manually cleaned before annotation. To ensure a balanced and high-quality dataset, subreddits that explicitly mention sarcasm indicators (e.g., `/s`, "sarcasm") were excluded.

## Annotation Process

- The dataset was divided into **eight CSV files** (`data_1.csv` to `data_8.csv`).
- **15% of the total data** was duplicated across datasets for agreement verification:
  - `data_1.csv` and `data_2.csv` share **192 common entries**, with **48 unique entries** in each.
  - `data_3.csv` and `data_4.csv` share **96 common entries**, with **144 unique entries** in each.
  - `data_5.csv` to `data_8.csv` each contain **240 unique entries**.
- Peers annotated the datasets independently.
- The duplicated portion was manually reviewed by project members to calculate annotator agreement.
- A third-party adjudicated disagreements, leading to final reannotation of the duplicated portion.

## Data Processing & Splitting

- The final annotated dataset was merged into a single dataset.
- The data was split into:
  - **70% Training**
  - **15% Validation**
  - **15% Test**
- An analysis revealed class imbalance (more non-sarcastic than sarcastic samples), requiring careful handling during modeling.

## Baseline Models

To establish a benchmark, we tested two baseline models:

- **Random baseline** (assigning labels randomly):
  - Validation accuracy: **0.4939**
  - Test accuracy: **0.4898**
- **Majority baseline** (assigning the most common label to all inputs):
  - Validation accuracy: **0.7510**
  - Test accuracy: **0.7551**

The higher majority baseline indicates that sarcasm is a minority class in the dataset, necessitating strategies to handle class imbalance.

## Model Training

We trained a **Logistic Regression** model as our initial approach:

- Validation accuracy: **0.6939**
- Test accuracy: **0.6449**

The model performed worse than the majority baseline, likely due to class imbalance and the complexity of sarcasm detection. Future improvements will explore advanced techniques to enhance performance.

## Folder Structure

```
project_root/
│── data/
│   ├── ground_labels/       # Final labeled dataset
│   ├── pre_annotation/      # Unannotated split data
│   ├── post_annotation/     # Annotated split data
│   ├── raw/                 # Raw data
│   ├── resolved/            # Final adjudicated dataset
│   ├── splits/              # Train, validation, and test splits
│
│── scripts/
│   ├── data_collection/     # Data collection scripts (PRAW, Reddit API)
│   ├── data_preparation/    # Separating data into 8 datasets
│   ├── model_training/      # Model training scripts
│   ├── user_agreement/      # User Agreement calculating script
│
│── outputs/
│   ├── accuracy.txt          # Model evaluation results
│   ├── data_distribution.png # Data visualization
│
│── docs/
│   ├── project_proposal.pdf # Initial project proposal
│   ├── README.md            # Project documentation
```

## Future Work

- **Address class imbalance** using techniques like oversampling, undersampling, or weighted loss functions.
- **Collect and integrate higher-quality data** to improve model performance.
- **Experiment with deep learning models**, such as LSTMs, transformers, and CNNs.
- **Improve annotation agreement** by refining annotation guidelines and incorporating additional adjudication rounds.
- **Enhance feature engineering**, including sentiment analysis, context embeddings, and syntactic features.

## Notes

- The dataset is imbalanced (because most text in general isn't sarcastic), which is why the majority baseline outperformed the random baseline.
- We chose to include `data_3.csv` in the final dataset (`ground_labels.csv`) despite conflicts, as it helped reduce data imbalance.
- All scripts are written in Python and assume the required libraries are installed.

## Contributors

- **[Ankur Pandey]** - pandea23@mcmaster.ca
- **[Devansh Singh]** - singhd80@mcmaster.ca

## Acknowledgments

We would like to thank our peers for their contributions to the annotation process and the third-party adjudicator for helping finalize the dataset labels.
