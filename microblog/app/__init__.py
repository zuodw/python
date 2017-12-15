from flask import Flask
from app import config

app = Flask(__name__)
app.config.from_object(config)

'''使用以下方式可以不用import，使用string的方式'''
# app.config.from_object('app.config')

from app.views import microblogviews