import argparse
import numpy as np
import pandas as pd
from pathlib import Path
from transformers import pipeline
from tqdm import tqdm

def prediction_to_class(pred, threshold=0.5):
    """
    Transform predictions into corresponding classes 
    INPUT:
        pred: Prediction from model, dict with keys "label" and "score"
        threshold: 
    OUTPUT:
        out: Either "NEGATIVE", "POSITIVE", or "NEUTRAL"
    """
    label = pred["label"]
    score = pred["score"]
    if label == "NEGATIVE" and score > threshold:
            out = "NEGATIVE"
    elif label == "POSITIVE" and score > threshold:
        out = "POSITIVE"
    else:
        out = "NEUTRAL"
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_data_folder", default="data/seattle", help="Input data folder path")
    parser.add_argument("-o", "--output_csv", default="review_sentiments", help="Output csv file name")
    args = parser.parse_args()

    # Load data
    data_folder_name = args.input_data_folder
    df = pd.read_csv(Path(data_folder_name)/"reviews.csv")

    # Consider only data with valid comments
    df = df.dropna()

    # Get model
    sentiment_classifier = pipeline('sentiment-analysis')

    # Data preprocessing
    comments = df["comments"]
    # Remove newlines and split into sentences
    comments = [x.replace("\r", "").replace("\n", "").split(".") for x in df["comments"]]
    # Remove empty strings from sentence lists
    comments = [list(filter(None, x)) for x in comments]

    print("Total entries {}".format(len(comments)))

    # Predict sentiments
    sentiment_csv = Path(data_folder_name)/(args.output_csv + ".csv")
    if not sentiment_csv.exists():
        with open(sentiment_csv, "w") as f:
            f.write("review_id,positive,negative,neutral\n")
            for i, c in tqdm(zip(df["id"][47164:], comments[47164:])):
                try:
                    sentiments = sentiment_classifier(c)
                    labels = [prediction_to_class(x) for x in sentiments]
                    positive = labels.count("POSITIVE")
                    negative = labels.count("NEGATIVE")
                    neutral = labels.count("NEUTRAL")
                    f.write("{},{},{},{}\n".format(i, positive, negative, neutral))
                except:
                    f.write("{},{},{},{}\n".format(i, np.nan, np.nan, np.nan))
    else:
        print("{} already exists! Delete it if you want to rewrite it.".format(sentiment_csv))