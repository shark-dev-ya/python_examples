# let's import datetime to add datetime and format it
from datetime import datetime


class DummyDateTimeFormatter:

    def __init__(self, custom_format=None):
        # variable = value_if_true if condition else value_if_false
        self.__format = custom_format if custom_format is not None else '%Y-%m-%d %H:%M:%S'

    def format_string(self, custom_string):
        current_datetime = datetime.now()
        current_datetime_formatted = current_datetime.strftime(self.__format)
        return f'{current_datetime_formatted} :: {custom_string}'


if __name__ == '__main__':
    custom_formatter_1 = DummyDateTimeFormatter()
    custom_formatter_2 = DummyDateTimeFormatter('%Y/%m/%d__%H_%M_%S')
    custom_formatter_3 = DummyDateTimeFormatter('%Y_%m_%d::%H_%M_%S')

    print(custom_formatter_1.format_string('an example of using custom_formatter_1'))
    print(custom_formatter_2.format_string('an example of using custom_formatter_2'))
    print(custom_formatter_3.format_string('an example of using custom_formatter_3'))

    print()

    print(custom_formatter_1.format_string('another example of using custom_formatter_1'))
    print(custom_formatter_2.format_string('another example of using custom_formatter_2'))
    print(custom_formatter_3.format_string('another example of using custom_formatter_3'))



