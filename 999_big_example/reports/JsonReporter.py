from . import IReporter
from datetime import datetime
import json


# JSON formatted reporter. will
class JsonReporter(IReporter):
    def __init__(self, name, custom_format=None):
        super().__init__(name)
        self.__format_string = custom_format if custom_format is not None else '%Y-%m-%d %H:%M:%S:%f'
        self.__json = {'name': name, 'log_data': []}

    def name(self):
        return self.__name

    def log(self, data):
        timestamp = datetime.now().strftime(self.__format_string)
        json_data_view = {'timestamp': timestamp, 'data': data}
        self.__json['log_data'].append(json_data_view)

    def log_list(self, *args):
        timestamp = datetime.now().strftime(self.__format_string)
        for entry in args:
            json_data_view = {'timestamp': timestamp, 'data': entry}
            self.__json['log_data'].append(json_data_view)

    def log_dict(self, **kwargs):
        timestamp = datetime.now().strftime(self.__format_string)
        for kwargs_key in kwargs:
            json_data_view = {
                                'timestamp': timestamp,
                                'data': {
                                    kwargs_key: kwargs[kwargs_key]
                                }
                              }
            self.__json['log_data'].append(json_data_view)

    def print(self):
        print(json.dumps(self.__json))

    def get_content(self):
        return self.__json

    def clear(self):
        self.__json = {'name': self.name(), 'log_data': []}

    def __str__(self):
        return json.dumps(self.__json)

    def __repr__(self):
        return f'{self.name()}::JSON{json.dumps(self.__json)}'