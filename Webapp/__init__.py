from flask import Flask
# Instantiate our app...
# Name it the '__name__' of this module (tweet-harvest)
app = Flask(__name__)

# Later, we will store our Twitter tokens/keys
# in config.py...we load our config here.
app.config.from_object('config')

# We define our URL route, and the controller to handle requests
@app.route('/')
def hello_world():
    return '<h1>TwEeTy Made Easy</h1>'