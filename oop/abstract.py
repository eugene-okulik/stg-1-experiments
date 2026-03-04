from abc import abstractmethod


class Bird:
    @abstractmethod
    def walk(self):
        pass


class Dove(Bird):
    def walk(self):
        print('')


class Flamingo(Bird):
    def walk(self):
        print()

class Duck(Bird):
    def kria(self):
        print('kria')

donald = Duck()
donald.kria()
