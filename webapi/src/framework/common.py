from flask import g

class ModelNotFound(Exception):
    pass

class DuplicateModelName(Exception):
    pass

def get_current_application():
    return g.__current_application__
