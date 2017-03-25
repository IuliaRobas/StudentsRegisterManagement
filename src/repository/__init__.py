'''
Created on Nov 28, 2016

@author: peacegabi
'''
class RepoError(Exception):
    pass
class Repository:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._entities ={}
        
    def save(self,entity):
        if entity.ident in self._entities:
            raise RepoError("id existent!!")
        self._entities[entity.ident]=entity
        
    def remove(self,ident):
        if ident not in self._entities:
            raise RepoError("id inexistent!!")
        del self._entities[ident]
        
    def update(self,entity):
        if entity.ident not in self._entities:
            raise RepoError("id inexistent!!")
        self._entities[entity.ident]=entity
        
    def getAll(self):
        return [x for x in self._entities.values()]
    
    def findById(self,ident):
        if ident not in self._entities:
            raise RepoError("id inexistent!!")
        return self._entities[ident]