import abc
from enum import Enum

from .common import get_current_application, ModelNotFound


class Operation(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, d: dict) -> 'Operation':
        operation_type_name = d['type']
        operation_analyzer = operation_type_dict[operation_type_name]
        return operation_analyzer(d)


class OperationCombination(Operation):

    def __init__(
        self,
        atomic: bool,
        operation_list: list
    ):
        self.atomic = atomic
        self.operation_list = operation_list


class SingleOperation(Operation):
    pass


def operation_combination_analyzer(d: dict) -> OperationCombination:
    if 'atomic' in d:
        atomic = d['atomic']
    else:
        atomic = True

    operation_list = []
    for operation_dict in d['list']:
        operation = Operation.from_dict(operation_dict)
        operation_list.append(operation)

    operation = OperationCombination(
        atomic=atomic,
        operation_list=operation_list
    )
    return operation


def get_model_by_name(model_name: str):
    application = get_current_application()
    if model_name in application.model_dict:
        return application.model_dict[model_name]
    else:
        raise ModelNotFound()


def single_operation_analyzer(d: dict) -> SingleOperation:
    model_name = d['model']
    model = get_model_by_name(model_name)
    operation = model.analyze_operation_from_dict(d)
    return operation


operation_type_dict = {
    'combination': operation_combination_analyzer,
    'single': single_operation_analyzer,
}
