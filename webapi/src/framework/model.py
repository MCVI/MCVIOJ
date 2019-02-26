import abc
from typing import TypeVar, List, Dict

from .operation import SingleOperation

class Field(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        pass

class Method(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def analyze_operation_from_dict(self, model: type, d: dict) -> SingleOperation:
        pass

class ModelBase:
    plain_field_list: List[str] = []
    method_map: Dict[str, Method] = {}

    @classmethod
    def analyze_operation_from_dict(cls, d:dict) -> SingleOperation:
        method_name = d['method']
        method = cls.method_map[method_name]
        operation = method.analyze_operation_from_dict(cls, d)
        return operation
