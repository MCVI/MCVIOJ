import os
from flask import Flask

class Application:
    def __init__(self, import_name, config_folder='config'):
        self.wsgi_app = Flask(import_name)

        if self.wsgi_app.config['DEBUG']:
            config_file = os.path.join(config_folder, 'development.py')
        else:
            config_file = os.path.join(config_folder, 'production.py')
        self.wsgi_app.config.from_pyfile(config_file)
