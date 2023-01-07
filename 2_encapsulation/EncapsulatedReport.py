# Define a class with private fields
class EncapsulatedReport:
    # we will define private fields inside a constructor
    # so each object of EncapsulatedReport will have its own fields
    def __init__(self):
        self.__violations = []
        self.__info = []
        self.__debug = []
        pass

    def add_violation(self, violation):
        self.__violations.append(violation)

    def add_info(self, info):
        self.__info.append(info)

    def add_debug(self, anything):
        self.__debug.append(anything)

    def dump(self):
        output = ''
        for violation in self.__violations:
            output += f'[VIOLATION] {violation}\n'
        output += '\n'

        for info in self.__info:
            output += f'[INFO] {info}\n'
        output += '\n'

        for debug in self.__debug:
            output += f'[DEBUG] {debug}\n'

        print(output)


if __name__ == '__main__':
    report_main = EncapsulatedReport()
    report_secondary = EncapsulatedReport()

    report_main.add_violation('The variable is wrong declared!')
    report_main.add_violation('The voltage is too high!')
    report_main.add_info('it is useful information :)')

    report_secondary.add_debug('i have spend the whole evening to figure out something funny')
    report_secondary.add_debug('haven\'t figured out.')

    print('----------BEGIN--------------')
    print('_____________________________')
    report_main.dump()
    print('_____________________________')
    report_secondary.dump()
    print('_____________________________')
    print('-----------END---------------')

    # causes:AttributeError: 'EncapsulatedReport' object has no attribute '__violations'. Did you mean: 'add_violation'?
    # print(report_main.__violations)

    # the 4 following lines below :
    report_main.__violations = ['my value!']
    print(report_main.__violations)
    report_main.add_violation('another line')
    print(report_main.__violations)

    # will print:
    # ['my value!']
    # ['my value!']

    # but this function:
    print('_____________________________')
    report_main.dump()
    print('_____________________________')

    # will print the following:
    # _____________________________
    # [VIOLATION] The variable is wrong declared!
    # [VIOLATION] The voltage is too high!
    # [VIOLATION] another line
    #
    # [INFO] it is useful information:)
    #
    # _____________________________


