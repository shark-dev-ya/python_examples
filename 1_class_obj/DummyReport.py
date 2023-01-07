# Define our own Class for dummy reports
class DummyReport:

    # let's define a constructor, empty so far
    def __init__(self):
        # important note here: for this object
        # we add a field "buffer", which is "list"
        self.buffer = []

    # define a function, which will accept *args
    # variable list of arguments of simple type
    def collect_data(self, *list_of_values):
        for val in list_of_values:
            self.buffer.append(val)

    # define a function, which will accept *args
    # variable list of arguments of "list" type
    def collect_list(self, *list_of_values):
        for val in list_of_values:
            if isinstance(val, list):
                for sub_val in val:
                    self.buffer.append(sub_val)

    # just simple function to collect all elements
    # in a string and print it.
    def print_report(self):
        output = 'DummyReport contains : \n'
        for entry in self.buffer:
            output += f' {entry}'
        print(output)


if __name__ == '__main__':
    # create 2 objects of DummyReport class
    dummy_report_1 = DummyReport()
    dummy_report_2 = DummyReport()

    # let's do bad practice and use an object's field directly here.
    dummy_report_2.buffer.append('my data outside the object/class')
    dummy_report_2.buffer.append('my data outside the object/class')

    # now, let's do good practice and use methods defined
    dummy_report_1.collect_data(5, 10, 15, 20, 25)
    dummy_report_1.collect_data(5.15, 5.20, 10.25, -54.2)
    dummy_report_1.collect_data('String1', 'String2', 'String3')
    dummy_report_1.collect_list([1, 2, 3], ['a', 'b', 'c'])
    dummy_report_1.collect_list(['abc', 'def', 'ghi'])

    # and let's print the content
    dummy_report_1.print_report()
    dummy_report_2.print_report()

