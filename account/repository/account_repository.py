from abc import ABC, abstractmethod

class AccountRepository(ABC):
    @abstractmethod
    def findByUsername(self, username):
        pass