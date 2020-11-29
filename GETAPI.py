from abc import ABC, abstractmethod

class api_request(ABC):
    @abstractmethod
    def search_name(self, bebida_name):
        pass