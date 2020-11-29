from abc import ABC, abstractmethod

class GETAPI(ABC):
    @abstractmethod
    def search_name(self, bebida_name):
        pass