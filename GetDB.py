
from abc import ABC, abstractmethod

class GETDB(ABC):
    @abstractmethod
    def SaveCoctel(self, bebida):
        pass