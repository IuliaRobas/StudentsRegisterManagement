
from sorting.algorithms.algorithm import Algorithm
from sorting.sorting import Sorting


class Student:
    '''
    Represents an entity student:
        -studentID - unique ID
        -name - name of the student
    '''
    
    def __init__(self, studentID, studentName):
        self.__studentID = studentID
        self.__studentName = studentName
        

    def student_less_than(self, other):
        """name ascending, age descending
        """
        if self.studentName == other.studentName:
            return self.studentID > other.studentID
        return self.studentName < other.studentName
 
 
    def __lt__(self, other):
        return self.student_less_than(other)
    def __gt__(self):
        return lambda x, y: not self.student_less_than(x, y)
   
    def __str__(self):
        '''
        This function represents the student
        '''       
    
        return 'StudentID: {0}  StudentName: {1}'.format(self.__studentID, self.__studentName)
        
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


if __name__ == '__main__':
    l = [2, 1, 3]
    Sorting.sort(l)
    assert (l == [1, 2, 3])

    l = [2, 1, 4,3,-1]
    Sorting.sort(l)
    assert (l == [-1,1,2,3,4])
    
    l=[-3,4,0,-1]
    Sorting.sort(l)
    assert(l==[-3,-1,0,4])
        
        
    st1=Student(3,"Mary")
    st2=Student(1,"Anne")
    st3=Student(2,"Eric")
    st4=Student(4,"Christian")
      
    
    l=[st1,st2,st3,st4]
    Sorting.sort(l, key=lambda x: x.studentID)
    assert(l==[st2,st3,st1,st4])
      
    l=[st1,st2,st3,st4]
    Sorting.sort(l, key=lambda x: x.studentID,reverse=True)
    assert(l==[st4,st1,st3,st2])
       
    l=[st1,st2,st3,st4]
    Sorting.sort(l, key=lambda x: x.studentName)
    assert(l==[st2,st4,st3,st1])
    
    l=[st1,st2,st3,st4]
    Sorting.sort(l, key=lambda x:x.studentName, reverse=True)
    assert(l==[st1,st3,st4,st2])   
    

    st1=Student(3,"st1")
    st2=Student(1,"st3")
    st3=Student(3,"st4")
    st4=Student(4,"st3")
    st5=Student(0,"st3")
    
    # sort by name,id ascending
    l = [st3, st2, st1, st4,st5]
    Sorting.sort(l, key=lambda x: (x.studentName, x.studentID))
    assert (l == [st1, st5,st2, st4, st3])   

    # sort by name ascending and by ID descending    
    l = [st3, st2, st1, st4,st5]
    Sorting.sort(l)
    assert (l == [st1,st4,st2,st5,st3]) 
    
    print("Sorting works!")   

#     #sort by name ascending and by ID descending with BubbleSort2
#     l = [st3, st2, st1, st4,st5]
#     Sorting.sort(l,algorithm=Algorithm.BUBBLE_SORT2)
#     assert (l == [st1,st4,st2,st5,st3])     
#     
#  
#     # sort by name ascending and by age descending with InsertionSort
#     l = [p3, p2, p1, p4]
#     Sorting.sort(l, algorithm=Algorithm.INSERTION_SORT)
#     assert (l == [p4, p1, p2, p3])
 
#     # sort by name ascending and by age descending with InsertionSort
#     l = [st3, st2, st1, st4,st5]
#     Sorting.sort(l,algorithm=Algorithm.INSERTION_SORT_REC)
#     assert (l == [st1,st4,st2,st5,st3])
#  
#     # sort by name ascending and by age descending with QuickSort
#     l = [st3, st2, st1, st4,st5]
#     Sorting.sort(l,algorithm=Algorithm.QUICK_SORT)
#     assert (l == [st1,st4,st2,st5,st3])        
# 
#     # sort by name ascending and by age descending with MergeSort
#     l = [p3, p2, p1, p4]
#     Sorting.sort(l, algorithm=Algorithm.MERGE_SORT)
#     assert (l == [p4, p1, p2, p3])
# 
#     print("hello world")
