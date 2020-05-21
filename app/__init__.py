from flask import Flask
app = Flask(__name__)
# import routes file containing page view functions
from app import routes
app.config['SECRET_KEY'] = 'any secret string'
app.jinja_env.cache = {}