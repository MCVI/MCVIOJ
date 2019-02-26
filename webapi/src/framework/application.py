import os
from typing import Optional
from flask import Flask, g

from .common import DuplicateModelName

class Application:
    def register_model(self, model_class: type, model_name: Optional[str] = None) -> None:
        if model_name is None:
            model_name = model_class.__name__

        if model_name in self.model_dict:
            raise DuplicateModelName()
        else:
            self.model_dict[model_name] = model_class

    def api_v1_entry(self):
        g.__current_application__ = self

        #stub
        pass

    def __init__(self, import_name, config_folder='config'):
        self.wsgi_app = Flask(import_name)

        if self.wsgi_app.config['DEBUG']:
            config_file = os.path.join(config_folder, 'development.py')
        else:
            config_file = os.path.join(config_folder, 'production.py')
        self.wsgi_app.config.from_pyfile(config_file)

        self.model_dict = {}

        @self.wsgi_app.route('/v1', methods=['POST'])
        def api_v1_entry():
            self.api_v1_entry()
