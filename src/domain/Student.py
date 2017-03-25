
class Student:
    '''
    Represents an entity student:
        -studentID - unique ID
        -name - name of the student
    '''
    
    def __init__(self, studentID, studentName):
        self.__studentID = studentID
        self.__studentName = studentName
        
        
    def __str__(self):
        '''
        This function represents the student
        '''       
    
        return 'StudentID: {0}  StudentName: {1}'.format(self.__studentID, self.__studentName)
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)
        
    def __gt__(self, other):
        '''
        Function to compare two instances
        :param: other - other instance
        '''
        return self.__studentID > other.__studentID
    
    @property
    def studentID(self):
        '''
        Getter for the id of the student
        :return: an integer representing the id of the student
        '''
        return self.__studentID
    
    @studentID.setter
    def studentID(self,newID):
        '''
        Setter for the student Id
        :parameter: the new Id 
        '''
        self.__studentID = newID
        
    @studentID.deleter
    def studentID(self):
        del self.__studentID
        
    @property
    def studentName(self):
        '''
        Getter for the Name of the student
        :return: a string: the name of the student
        '''
        return self.__studentName     
    
    @studentName.setter   
    def studentName(self,newName):
        '''
        Setter for the student name
        :parameter: the new name
        '''
        self.__studentName = newName
        
    @studentName.deleter
    def studentName(self):
        del self.__studentName