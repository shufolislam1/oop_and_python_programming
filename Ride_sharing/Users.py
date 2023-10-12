# there will be two types of user. 1. Driver: who will drive the bike,car 2.customer: who will take the bike,car to go somewhere

from abc import ABC, abstractmethod

# User class is inheriting from ABC, making it an abstract base class. This means that User is intended to be a base class for other classes, and it cannot be instantiated directly.
# Instead, subclasses of User should be created, and those subclasses must implement the abstract methods defined in User

class User(ABC):
    def __init__(self, user_name, user_email, user_nid) -> None:
        self.name = user_name
        self.email = user_email
        # id, nid will be private attribute
        # TODO : set user id dynamically
        self.__id = 0
        self.__nid = user_nid
        self.wallet = 0

    # display_profile method is marked as abstract using @abstractmethod. This means that any class that inherits from User must provide an implementation for the display_profile method. 
    # otherwise it will raise a NotImplementedError

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Customer(User):
    def __init__(self, user_name, user_email, user_nid) -> None:
        # customer kono ride e nai
        self.customers_current_ride = None
        super().__init__(user_name, user_email, user_nid)

    def display_profile(self):
        print(f'Customer with name {self.name} and email {self.email}')

    def request_ride(self, customer_location, customer_destination):
        # customer already arekta driver er sathe onno kono ride e ache kina/ onno kothaw jacche kina check kora
        if not self.customers_current_ride:
            #TODO: set ride request properly
            ride_request = None
            # TODO: set customers_current_ride via driver. (mane customer request pathanor por driver jabe naki jabena ta set kora)
            self.customers_current_ride = None