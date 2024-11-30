# Import necassary  modules 
from abc import ABC, abstractmethod

# Create base class
class ABsclass(ABC):

    # function to print a value
    def print(self,x):
        print("Passed value : ", x)

    # Abstract method
    @abstractmethod
    def task(self):
        print("We are inside ABstract task")

# Create sub class
class test_class(ABsclass):
    def task(self):
        print("We are inside test_class task")

# Object of test_class created 
test_obj = test_class()
test_obj.task()
test_obj.print(100)