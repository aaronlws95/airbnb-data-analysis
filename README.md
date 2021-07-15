# Airbnb Data Analysis

In this repo, we dive into the [Airbnb Seattle dataset](https://www.kaggle.com/airbnb/seattle) from Kaggle and try to find out how to have a successful listing on Airbnb. Our analysis will follow the [CRISP-DM](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining) methodology.

You can see the related blog post [here](https://aaronlws.medium.com/a-few-data-based-tips-for-being-successful-on-airbnb-4d9fa23f6b13).

This work was carried out as homework as part of the [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025).

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

## Conclusion

1. `listings_data_analysis`
    * A responsive host is a successful host
    * If you want to be a Top Performer becoming a Superhost increases your odds by quite a fair bit
    * When it comes to amenities, quality over quantity
2. `prediction_model`
    * Our modelled data did not perform well and suffered heavily from overfitting. More work to be done here.
3. `semantic-analysis`
    * Semantic score is a useful metric to rate listings but we need to keep an eye out for false predictions.

## References

* [Airbnb Seattle dataset](https://www.kaggle.com/airbnb/seattle)
* [CRISP-DM](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining)
* [Blog Post](https://aaronlws.medium.com/a-few-data-based-tips-for-being-successful-on-airbnb-4d9fa23f6b13)