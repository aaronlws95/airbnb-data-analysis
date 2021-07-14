# Airbnb Data Analysis

Homework as part of the [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025).

You can read the [related blog post](https://aaronlws.medium.com/a-few-data-based-tips-for-being-successful-on-airbnb-4d9fa23f6b13) for a summary of the results.

In this repo, we dive into the [Airbnb Seattle dataset](https://www.kaggle.com/airbnb/seattle) from Kaggle and try to find out how to have a successful listing on Airbnb.

## Setup

Install the required libraries

```bash
pip install -r requirements.txt
```

## Info

In this repo we have 3 notebooks. Further information is provided inside the notebooks.

1. `listings_data_analysis`
    * In this notebook, we take an initial look at the data we're dealing with and do some analysis on the listings to help answer several questions. Broadly speaking we are looking to answer the question: **How do I become successful on Airbnb?**

2. `prediction_model`
    * In this notebook, we will try to predict the aggregate review score using the given listings data with just linear regression.

3. `semantic-analysis`
    * In this notebook, we use an off-the-shelf sentiment analysis model to estimate the sentiments from the reviews. There is no ultimate goal for this notebook, it is just for fun.
