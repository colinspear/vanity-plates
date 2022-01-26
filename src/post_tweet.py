from pathlib import Path
from datetime import datetime
import pandas as pd

import tweet as t


home = '/Users/colinspear/dev/vanity_plates/'
df = pd.read_csv(home + 'data/clean_rejections.csv')

tweet = t.make_tweet(df)
t.post_tweet(tweet)

print(f"{datetime.now().strftime('%Y-%m-%d %X')} tweet sent")
