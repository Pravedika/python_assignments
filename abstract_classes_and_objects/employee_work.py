from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Developer writes and maintains software.")

class Tester(Employee):
    def work(self):
        print("Tester tests software applications.")

Developer().work()
Tester().work()
