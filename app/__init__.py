import os

from flask import Flask, Blueprint
from flask_cors import CORS

from config import DevConfig, ProdConfig

app = Flask(__name__)
CORS(app)

app_ctx = os.environ.get("ENV_VAR", "dev")

if app_ctx == 'dev':
    cfg = DevConfig()
elif app_ctx == 'prd':
    cfg = ProdConfig()
else:
    print('Config env erro')
    exit()

app.config['SECRET_KEY'] = cfg.SECRET_KEY

from app.controllers.graphql_controller import graphql_controller
from app.controllers.rest_controller import rest_controller

app.register_blueprint(graphql_controller)
app.register_blueprint(rest_controller)