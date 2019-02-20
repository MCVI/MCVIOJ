from src import *

framework_app = framework.Application(__name__)
app = framework_app.wsgi_app
