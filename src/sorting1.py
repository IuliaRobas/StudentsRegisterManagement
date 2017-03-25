'''
Created on Jan 2, 2017

@author: User
'''
#from domain.Student import Student
from abc import ABC, abstractmethod, ABCMeta
from enum import Enum, unique

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
        
# class GenericSort(metaclass=ABCMeta):
class GenericSort(ABC):
    
    def __init__(self, col, key, reverse):
        self.__col = col
        self.__key = key
        self.__reverse = reverse
        
    @property
    def col(self):
        return self.__col
    
    @property
    def key(self):
        return self.__key
    
    @key.setter
    def key(self, key):
        self.__key = key
    
    @property
    def reverse(self):
        return self.__reverse
    
    @abstractmethod
    def sort(self):
        pass
    
    def _in_order(self, e1, e2, eq=True):
        if self.key is None:
            self.key = lambda x:x        
        if self.key(e1) == self.key(e2):
            return eq
        if not self.reverse:
            return self.key(e1) < self.key(e2)
        return self.key(e1) > self.key(e2)
    
class ShellSort(GenericSort):
    def __init__(self, col, key, reverse):
        super().__init__(col, key, reverse)
        
    def sort(self):
#         size = len(self.col)
#         #we start with a bigger gap
#         gap = int(size/2)
#         while gap>0:
#             #we do the insertion sort of the gapped elements
#             i = gap
#             while (i<size) : 
#                 j=i-gap
#                 while (j>=0 and self.col[j] > self.col[j+gap]):
#                     temp=self.col[j]
#                     self.col[j] = self.col[j+gap]
#                     self.col[j+gap] = temp
#                     j = j-gap
#                               
#                 #increase current index
#                 i=i+1
#                 #reduce the gap by half
#             gap = int(gap/2)
        size = len(self.col)
        gap = int(size/2)
        while gap>0:
            i = gap
            while (i<size) : 
                j=i-gap
                while j>=0 and self.col[j] > self.col[j+gap]:
                    temp=self.col[j]
                    self.col[j] = self.col[j+gap]
                    self.col[j+gap] = temp
                    j = j-gap
                i=i+1
            gap = int(gap/2)
   
   
class GnomeSort(GenericSort):
    def __init__(self, col, key, reverse):
        super().__init__(col, key, reverse)
        
    def sort(self):
#         n=len(self.col)
#         index=0
#         while index<n:
#             
#             if index==0:
#                 index=index+1
#             print (self.col[index])
#             if self.col[index]>self.col[index-1] or self.col[index] == self.col[index-1]:
#             #if self.col[index]>=self.col[index-1]:    
#                 index=index+1
#             else:
# #                 temp=self.col[index]
# #                 self.col[index]=self.col[index-1]
# #                 self.col[index-1]=temp
#                 self.col[index],self.col[index-1] = self.col[index-1], self.col[index]
#                 index=index-1

        pos = 0
        while pos < len(self.col):
            if (pos == 0 or not self._in_order(self.col[pos],  self.col[pos - 1])):
                pos = pos + 1
            else:
                self.col[pos], self.col[pos-1] = self.col[pos-1], self.col[pos]
                pos = pos - 1
    #complexity O(n) because of index which gets incremented, but also decremented
 
class BubbleSort(GenericSort):
    def __init__(self, col, key, reverse):
        super().__init__(col, key, reverse)

    def sort(self):
        while True:
            sw = True
            for i in range(len(self.col) - 1):
                if not self._in_order(self.col[i], self.col[i + 1]):
                    self.col[i], self.col[i + 1] = self.col[i + 1], self.col[i]
                    sw = False
            if sw: break
@unique
class Algorithm(Enum):
    BUBBLE_SORT = BubbleSort
    GNOME_SORT = GnomeSort
    SHELL_SORT = ShellSort
                                   
class Sorting(object):
    @staticmethod
    def sort(col, key=None, reverse=False, algorithm=Algorithm.GNOME_SORT):
        sorting_alg = algorithm.value(col, key, reverse)
        #sorting_alg.sort()
        #sorting_alg = GnomeSort(col,key,reverse)
        sorting_alg.sort()

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
