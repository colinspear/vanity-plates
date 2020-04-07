import tweet as t

import pandas as pd


df = pd.read_csv('../data/clean_rejections.csv')

tweet = t.make_tweet(df)
t.post_tweet(tweet)
