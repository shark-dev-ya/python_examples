from abc import abstractmethod, ABC
from datetime import datetime


class AbstractReport(ABC):
    def __init__(self, name):
        self.__name = name

    def name(self):
        return self.__name

    @abstractmethod
    def report(self, data):
        pass

    @abstractmethod
    def dump(self):
        pass


class BasicReport(AbstractReport):
    def __init__(self, name):
        super().__init__(name)
        self.__buffer = ''

    def report(self, data):
        self.__buffer += f'{data}\n'

    def dump(self):
        print(self.__buffer)


class MoreInformativeReport(AbstractReport):
    def __init__(self, name):
        super().__init__(name)
        self.__buffer = []

    def report(self, data):
        self.__buffer.append(data)

    def dump(self):
        print(f'At the time: {datetime.now()} {self.name()} contains:')
        for entry in self.__buffer:
            print(f'\n{entry}')


def log(reporter, msg):
    reporter.report(msg)


if __name__ == '__main__':
    simple = BasicReport('simple')
    timestamped = MoreInformativeReport('timestamped')

    log(simple, 'message_1_1')
    log(simple, 'message_1_2')
    log(timestamped, 'message_2_1')
    log(timestamped, 'message_2_2')

    print('----------BEGIN--------------')
    print('_____________________________')
    simple.dump()
    print('_____________________________')
    timestamped.dump()
    print('_____________________________')

    log(simple, 'message_1_3')
    log(simple, 'message_1_4')
    log(timestamped, 'message_2_3')
    log(timestamped, 'message_2_4')

    print('_____________________________')
    simple.dump()
    print('_____________________________')
    timestamped.dump()
    print('_____________________________')
    print('-----------END---------------')