import tweepy
from tweepy.auth import OAuthHandler
import os
from dotenv import load_dotenv


load_dotenv()

_api_key = os.getenv('API_Key')
_api_key_secret = os.getenv('API_Key_Secret')
_bearer_token = os.getenv('Bearer_Token')
_client_id = os.getenv('Client_ID')
_client_secret = os.getenv('Client_Secret')
_access_token = os.getenv('Access_Token')
_access_token_secret = os.getenv('Access_Token_Secret')

auth = tweepy.OAuthHandler(_api_key, _api_key_secret)
auth.set_access_token(_access_token, _access_token_secret)
resp= tweepy.API(auth)

api = tweepy.API(auth)

user = api.get_user(screen_name='elmejorgrunon')
print(user.screen_name)
print(user.followers_count)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)