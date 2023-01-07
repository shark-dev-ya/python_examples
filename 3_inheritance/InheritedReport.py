# let's import datetime to add datetime and format it
from datetime import datetime


class BasicReport:
    def __init__(self, name):
        self.__name = name
        self.__buffer = []

    def put(self, data):
        self.__buffer.append(data)

    def dump(self):
        buffer = f'Report |{self.__name}| contains: '
        for elem in self.__buffer:
            buffer += f'\n{elem}'
        return buffer


class ExtendedReport(BasicReport):
    def __init__(self, name, custom_format=None):
        super().__init__(name)
        self.__format = custom_format if custom_format is not None else '%Y-%m-%d %H:%M:%S'

    def put_with_timestamp(self, data):
        timestamp = datetime.now().strftime(self.__format)
        super().put(f'{timestamp} :: {data}')


if __name__ == '__main__':
    basic_report = BasicReport('basics')
    extended_report = ExtendedReport('extended')

    basic_report.put(5.15)
    basic_report.put(24.25)
    basic_report.put('string')

    extended_report.put(9546)
    extended_report.put_with_timestamp(-234.523)
    extended_report.put_with_timestamp('other string')

    print('----------BEGIN--------------')
    print('_____________________________')
    print(basic_report.dump())
    print('_____________________________')
    print(extended_report.dump())
    print('_____________________________')
    print('-----------END---------------')
