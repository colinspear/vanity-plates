import config

import numpy as np
import tweepy

df = pd.read_csv('../data/clean_rejections.csv')

def make_tweet(df):
    # TODO sample without replacement
    row_id = np.random.randint(0, df.shape[0])
    row = df.iloc[row_id]

    s = np.random.choice(["sir", "ma'am"])
    tweet = (
        f"Californian: Check my sweet idea for a license plate: {row[0]}\n"
        '\n'
        'DMV: Uh...\n'
        '\n'
        f'C: Get it? {str.capitalize(row[2])}\n'
        '\n'
        f"DMV: I'm sorry, " + s + ", we can't do that.\n"
        '\n'
        'C: Why not?!\n'
        '\n'
        f"DMV: Well, " + s + f" because {str.lower(row[3])}"
    )

    return tweet

def post_tweet(df):
    tweet = make_tweet(df)
    # authentication of consumer key and secret 
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)

    # authentication of access token and secret 
    auth.set_access_token(config.access_token, config.access_token_secret)
    api = tweepy.API(auth)

    # update the status 
    api.update_status(status=tweet)
