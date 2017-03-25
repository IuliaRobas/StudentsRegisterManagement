'''
Created on Dec 17, 2016

@author: User
'''
from domain.Exceptions import FacultyException

class UndoOperation(object):
    def __init__(self, source_method, source_args, handler, handler_args):
        self.__source_method = source_method
        self.__handler = handler
        self.__source_args=source_args
        self.__handler_args=handler_args

    @property
    def source_method(self):
        return self.__source_method

    @property
    def source_args(self):
        return self.__source_args
    
    @property
    def handler(self):
        return self.__handler

    @property
    def handler_args(self):
        return self.__handler_args
    
class UndoControllerException(FacultyException):
    pass

class UndoController(object):
    def __init__(self):
        self.__undo_operations = []
        self.__redo_operations = []

    @property
    def operations(self):
        return self.__operations

    def register_operation(self, source_method, source_args, handler, handler_args):
        self.__undo_operations.append(UndoOperation(source_method,source_args, handler, handler_args))

    def undo(self):
        try:
            undo_operation = self.__undo_operations.pop() # TODO check for empty list
        except IndexError:
            raise UndoControllerException("There are no operations to undo!")
        self.__redo_operations.append(undo_operation)
        return undo_operation
    
    def redo(self):
        redo_operation=self.__redo_operations.pop()
        self.__undo_operations.append(redo_operation)
        return redo_operation
        
        
