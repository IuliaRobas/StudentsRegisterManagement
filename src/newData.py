'''
Created on 8 ian. 2017

@author: PC
'''


class newData:

    def __init__(self, values = None):       
        if values == None:
            self.values = {}
        else:
            self.values = values
    
    def __len__(self):
        return len(self.values)
    
    def __getitem__(self, key):
        return self.values[key]
    
    def __setitem__(self, key, value):
        self.values[key] = value
    
    def __delitem__(self, key):
        del(self.values[key])
        
    def __iter__(self):
        self.index = -1
        return self
      
    def __next__(self):
        if self.index == len(self.values) -1:
            return None
        self.index = self.index + 1
        return self.values[self.index]
    
    
#     def filterf(l, condition):
#         l = self.values
# #          
# #         newList = []
# #         for x in l:
# #             if condition(x):
# #                 newList.append(x)
# #                 print(x)
# #         return newList            
#         if condition==None:
#             return [item for item in l if item]
#         return [item for item in l if condition(item)]

def main():  
    

    newList = newData(values = [4,5,6])    
    del(newList[1])
    print(newList.values)
 
     
if __name__ == '__main__':
    main()
    
    
class Repository:

    def __init__(self,entities):
        self._entities = entities
        self.__keys = list(self._entities.keys())
        self.__crt = 0

    def __getitem__(self, item):
        return self._entities[item]

    def __setitem__(self, key, value):
        self._entities[key]=value

    def __delitem__(self, key):
        del self._entities[key]

    def __contains__(self, item):
        return item in self._entities

    def __iter__(self):
        self.__crt = 0
        return self

    def __next__(self):
        print(self.__keys)
        if self.__crt < len(self.__keys):
            self.__crt +=1
            return self._entities[self.__keys[self.__crt-1]]
        else:
            raise StopIteration

    def __len__(self):
        return len(self._entities)

    def sort(self):
        self.__keys = Repository.qsort(self.__keys,reverse=True)
        print(self.__keys)
        
    @staticmethod
    def qsort(l, key=lambda x: x, reverse=False):
        if l == []: return []
        if reverse:
            return Repository.qsort([x for x in l[1:] if key(x) >= key(l[0])], key, reverse) + [l[0]] + Repository.qsort([x for x in l[1:] if key(x) < key(l[0])], key, reverse)
        else:
            return Repository.qsort([x for x in l[1:] if key(x) < key(l[0])], key, reverse)+[l[0]]+ Repository.qsort([x for x in l[1:] if key(x) >= key(l[0])], key, reverse)
    @staticmethod
    def filter(l,cmp):
        return [x for x in l if cmp(x)]

class FileRepository(Repository):

    def __init__(self,entities):
        Repository.__init__(entities)



class Controller:
    def __init__(self,repo):
        self.__repo  = repo

    def greatest_even(self):
        l=[x for x in self.__repo]
        lf= Repository.filter(l, lambda x: x % 2 == 0)
        lfs= Repository.qsort(lf,reverse=True)
        ll = len(lfs)//2
        return lfs[:ll]

d = {1: 1, 2: 2, 3: 3,4:4, 5:5, 6:6,7:7, 8:8}
print(Repository.qsort([1,2,3], reverse=True))
repo = Repository(d)
repo.sort()
for x in repo:
    print(x)

l=[[1,2],[4,5],[8,7],[7,3],[9,9]]
sorted(l,)
print(Repository.qsort(Repository.filter(l,lambda x:x[1]%2==1),key=lambda x:x[1],reverse=True))
ctrl = Controller(repo)
print(ctrl.greatest_even())
    