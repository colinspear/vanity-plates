import tweet as t

from pathlib import Path
import pandas as pd


home = '/Users/colinspear/dev/vanity_plates/'
df = pd.read_csv(home + 'data/clean_rejections.csv')

tweet = t.make_tweet(df)
t.post_tweet(tweet)
