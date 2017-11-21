from aiohttp import web
from routes import setup_routes
import os

app = web.Application()

setup_routes(app)

# config_path = os.path.join('config', 'polls.yaml')
# print(config_path)

# conf = load_config(config_path)
# app['config'] = conf

web.run_app(app, host='127.0.0.1', port=8000)