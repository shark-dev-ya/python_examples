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

    def put(self, data):
        timestamp = datetime.now().strftime(self.__format)
        super().put(f'{timestamp} :: {data}')


def log_work_to_report(report, message):
    report.put(message)


if __name__ == '__main__':
    basic_report = BasicReport('basics')
    extended_report = ExtendedReport('extended')

    log_work_to_report(basic_report, 515)
    log_work_to_report(basic_report, 5.15)
    log_work_to_report(basic_report, 'string')
    log_work_to_report(basic_report, 3.14)

    log_work_to_report(extended_report, 9546)
    log_work_to_report(extended_report, -234.523)
    log_work_to_report(extended_report, 'other string')
    log_work_to_report(extended_report, 2.83)

    print('----------BEGIN--------------')
    print('_____________________________')
    print(basic_report.dump())
    print('_____________________________')
    print(extended_report.dump())
    print('_____________________________')
    print('-----------END---------------')
