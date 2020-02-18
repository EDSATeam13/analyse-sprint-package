import numpy as np
import pandas as pd


def dictionary_of_metrics(items):
    """
        Calculates the mean, median, variance, standard deviation, minimum and maximum of a list of items.
        Args:
            items (array): list or array-like object containing numerical values.
        Returns:
            dict: dictionary containing the mean, median, variance, standard deviation, minimum and maximum of the given list of items.
    """
    vr_list = []
    for x in items:
        vr_list.append((x - round(np.mean(items), 2)) ** 2)
    variance = round(sum(vr_list) / (len(vr_list) - 1), 2)
    standard_deviation = round((variance) ** 0.5, 2)
    return {
        "mean": round(np.mean(items), 2),
        'median': round(np.median(items), 2),
        'var': round(variance, 2),
        'std': round(standard_deviation, 2),
        'min': round(np.min(items), 2),
        'max': round(np.max(items), 2)
    }


def five_num_summary(items):
    """
        Calculates the maximum, median, minimum and quartiles of a list of items.
        Args:
            items (array): list or array-like object containing numerical values.
        Returns:
            dict: dictionary containing the five number summary of the given list of items.
    """
    return {
        'max': round(np.max(items), 2),
        'median': round(np.median(items), 2),
        'min': round(np.min(items), 2),
        'q1': round(np.quantile(items, 0.25), 2),
        'q3': round(np.quantile(items, 0.75), 2)
    }


def stop_words_remover(df):
    """
        Remove english stop words from a tweet.
        Args:
            df (pandas dataframe): A pandas dataframe.
        Returns:
            df: Returns a modified dataframe with all stop words removed, placed in a new column called 'Without Stop Words'.
    """
    if type(df) != type(pd.DataFrame()):
        return df
    split_tweets = []
    clean_tweets = []
    lower_split_tweets = []
    for _ in df[["Tweets"]]:
        tweets = df[_]
    for tweet in tweets:
        split_tweets.append(tweet.split())
    for tweet in split_tweets:
        for value in stop_words_dict["stopwords"]:
            for word in tweet:
                if word.lower() == value:
                    tweet.remove(word)
        clean_tweets.append(tweet)
    for _ in clean_tweets:
        lower_split_tweets.append([__.lower() for __ in _])
    df.insert(loc=2, column="Without Stop Words", value=lower_split_tweets)
    return df
