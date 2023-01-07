from abc import ABC, abstractmethod


# It is an interface IReporter, a developer should use implemented class instead
class IReporter(ABC):
    def __init__(self, name='default'):
        super().__init__()
        self.__name = name

    @abstractmethod
    def name(self):
        return self.__name

    @abstractmethod
    def log(self, data):
        pass

    @abstractmethod
    def log_list(self, *args):
        pass

    @abstractmethod
    def log_dict(self, **kwargs):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def clear(self):
        pass
