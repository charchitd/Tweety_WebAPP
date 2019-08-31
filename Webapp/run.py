
from flask import Flask, json, request, render_template
import tweepy

import os

DEBUG = True 
# Enable stacktrace & debugger in web browser
TWITTER_CONSUMER_KEY = 'jWyCozBU9BD48MRHzp0WhUhZu'#os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = 'mGPVR9WOTPB28zqw3QdxEE6v3KSzuBVN8H65XIc43NgdAeqVln' #os.environ['TWITTER_CONSUMER_SECRET']
TWITTER_ACCESS_TOKEN = '370556779-09vEbGdVhrNWcTQkt4F5eKq9ysEbEDkj5tBgZwnJ' #os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = 'hZFw9dZ2VOaFUhLvkRakNhDzgrcyIgUgOdZyXPei5zTzn' #os.environ['TWITTER_ACCESS_TOKEN_SECRET']


app = Flask(__name__)
# Load our config from an object, or module (config.py)
#app.config.from_object('config')

# These config variables come from 'config.py'
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
tweepy_api = tweepy.API(auth)

@app.route('/')
def hello_world():
    return "<h1>...TwEeTy Made Easy...</h1>"

def get_tweets(username):
    tweets = tweepy_api.user_timeline(screen_name=username)                                                                            
    return [{'tweet': t.text,
              'created_at': t.created_at, 
              'username': username,
              'headshot_url': t.user.profile_image_url}
           for t in tweets]

@app.route('/twitter/<string:username>')
def tweety(username):
	return render_template("tweety.html", tweets=get_tweets(username))
	#return render_template(foo.html, var1=obj1, var2=obj2, varN=objN)
  # 'tweets' is passed as a keyword-arg (**kwargs)
  # **kwargs are bound to the 'tweets.html' Jinja Template context
  
# 'app' originates from the line 'app = Flask(__name__)'
app.run(port=8080)
