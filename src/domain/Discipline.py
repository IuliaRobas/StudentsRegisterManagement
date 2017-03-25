
class Discipline:
    '''
    Represents an entit discipline:
        -disciplineID - unique ID
        -name - name of the discipline
    '''
    
    def __init__(self, disciplineID, disciplineName):
        self.__disciplineID = disciplineID
        self.__disciplineName = disciplineName
        
        
    def __str__(self):
        '''
        This function represents the discipline
        '''       
    
        return 'DisciplineID: {0}  DisciplineName: {1}'.format(self.__disciplineID, self.__disciplineName)
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)
        
    def __gt__(self, other):
        '''
        Function to compare two instances
        :param: other - other instance
        '''
        return self.__disciplineID > other.__disciplineID
    
    @property
    def disciplineID(self):
        '''
        Getter for the id of the discipline
        :return: an integer representing the id of the discipline
        '''
        return self.__disciplineID
    
    @disciplineID.setter
    def disciplineID(self,newID):
        '''
        Setter for the discipline Id
        :parameter: the new Id 
        '''
        self.__disciplineID = newID
        
    @disciplineID.deleter
    def disciplineID(self):
        del self.__disciplineID
        
    @property
    def disciplineName(self):
        '''
        Getter for the Name of the discipline
        :return: a string: the name of the discipline
        '''
        return self.__disciplineName     
    
    @disciplineName.setter   
    def disciplineName(self,newName):
        '''
        Setter for the discipline name
        :parameter: the new name
        '''
        self.__disciplineName = newName
        
    @disciplineName.deleter
    def disciplineName(self):
        del self.__disciplineName