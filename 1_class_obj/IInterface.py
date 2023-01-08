# An example class with different methods to compare with C++
from random import random


class IInterface:
    # This is an example of static property/field
    # Important note: it is available for all objects!
    amount_of_objects = 0

    # this is a static method. it can be called outside class without objects created
    @staticmethod
    def get_class_name():
        return "IInterface"

    # this is usual method, should be called from an object
    def class_method_returning_random_value(self):
        return int(random() * 100)

    def send_data(self, data):
        # some logic to send data through interface
        # but for now... just define an empty function
        pass

    def receive_data(self):
        # some logic to receive data through interface
        # but for now... just return some data
        return "John Doe was here..."


if __name__ == '__main__':
    print(IInterface.get_class_name())   # call a static method without an object
    print(IInterface.amount_of_objects)  # access a static field without an object

    # define a variable(object) of user defined type IInterface
    iinterface_obj = IInterface()
    print(iinterface_obj.class_method_returning_random_value())  # call a method through an object

    # define another variable(object) of user defined type IInterface
    iinterface_obj_2 = IInterface()
    print(iinterface_obj_2.class_method_returning_random_value())  # call a method through an object

    # call a class method!
    iinterface_obj.send_data("custom data")
    print(iinterface_obj.receive_data())       # call a method through an object
    print(iinterface_obj_2.receive_data())     # call a method through an object

    # we access the static method from an object also
    print(iinterface_obj_2.get_class_name())

    # what about our static field?
    print('{0} and {1} are {2}'.format(
           iinterface_obj.amount_of_objects,
           iinterface_obj_2.amount_of_objects,
           "equal" if iinterface_obj_2.amount_of_objects == iinterface_obj.amount_of_objects else "not equal"))
