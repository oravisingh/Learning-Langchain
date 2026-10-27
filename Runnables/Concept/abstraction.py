# It simply means hidden
# By using abstraction the higher level class can compell the lower level class to abide by some methods
# An abstract class is some class that has atleast one abstract method ( the constraint method used for child classes)
from abc import ABC, abstractmethod
class BankApp(ABC):
    def database(self):
        print("Connected to the database!")

    @abstractmethod
    def security(self):
        pass


class MobileApp(BankApp):

    def mobileLogin(self):
        print("Login to Mobile")

    def security(self): # If this not implemented, You cannot use the MobileApp class since you're not standing up to some condition or constraint
        print("Secured!")

mob1 = MobileApp()
print(mob1.security())