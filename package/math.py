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


def date_parser(dates):
    """
        Takes as input a list of these datetime strings and returns only the date in 'yyyy-mm-dd' format.
        Args:
            dates (array): list or array-like object containing datetime strings.
        Returns:
            list: list of strings where each element in the returned list contains only the date in the 'yyyy-mm-dd' format.
    """
    return [date.split()[0] for date in dates]


def number_of_tweets_per_day(df):
    """
        Calculates the number of tweets that were posted per day.
        Args:
            df (pandas dataframe): A pandas dataframe.
        Returns:
            df: Returns a new dataframe, grouped by day, with the number of tweets for that day.
    """
    df['Date']=df['Date'].str.split(expand=True)[0]
    return df.groupby('Date').count()


def word_splitter(df):
    """
        Split the sentences in a dataframe's column into a list of the separate words.
        Args:
            df (pandas dataframe): A pandas dataframe.
        Returns:
            df: returns a modified dataframe with new a column; 'Split Tweets', containing sentences in 'Tweets' which have been split.
    """
    lowercase_tweets = df['Tweets'].str.lower()
    df['Split Tweets'] = lowercase_tweets.str.split()
    return df


def extract_municipality_hashtags(df):
    """
        Extracts the municipality from a tweet using the mun_dict dictonary and, and inserts the result into a new column named
        'municipality' in the same dataframe. And extracts a list of hashtags from a tweet into a new column named 'hashtags' in
        the same dataframe.
        Args:
            df (pandas dataframe): A pandas dataframe.
        Returns:
            df: The input dataframe with additional columns.
    """
    for _ in df[["Tweets"]]:
        tweets = df[_]
    municipalities = []
    for _ in tweets:
        found = False
        tweet = _.split()
        for word in tweet:
            for key, value in mun_dict.items():
                if word == key:
                    municipalities.append(value)
                    found = True
                    break
            if found:
                break
        if not found:
            municipalities.append(np.nan)
    hashtags = []
    for _ in tweets:
        tweet = _.split()
        tags = []
        for word in tweet:
            if '#' in word:
                tags.append(word.lower())
        if len(tags) == 0:
            hashtags.append(np.nan)
        else:
            hashtags.append(tags)
    df.insert(loc=2, column="municipality", value=municipalities)
    df.insert(loc=3, column="hashtags", value=hashtags)
    return df

