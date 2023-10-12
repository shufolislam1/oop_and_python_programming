# there will be two types of user. 1. Driver: who will drive the bike,car 2.customer: who will take the bike,car to go somewhere

from abc import ABC, abstractmethod
from datetime import datetime

class Ride_sharing_service:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.customers = []
        self.drivers = []
        self.total_rides = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        # print(f'Company name {self.company_name} with customers {len(self.customers)} and drivers {len(self.drivers)}')
        return f'Company name {self.company_name} with customers {len(self.customers)} and drivers {len(self.drivers)}'
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
    def __init__(self, user_name, user_email, user_nid, current_location, initial_amount) -> None:
        # customer currently kono ride e nai
        self.customers_current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(user_name, user_email, user_nid)

    def display_profile(self):
        print(f'Customer with name {self.name} and email {self.email}')

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, ride_sharing, customer_destination):
        # customer already arekta driver er sathe onno kono ride e ache kina/ onno kothaw jacche kina check kora
        if not self.customers_current_ride:
            #TODO: set ride request properly
            ride_request = Ride_Request(self, customer_destination)

            # TODO: set customers_current_ride via driver. (mane customer request pathanor por driver jabe naki jabena ta set kora)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            self.customers_current_ride = ride_matcher.find_driver(ride_request)

    def show_current_ride(self):
        print(self.customers_current_ride)

class Driver(User):
    def __init__(self, user_name, user_email, user_nid, driver_cur_location) -> None:
        self.driver_cur_location = driver_cur_location
        self.wallet = 0
        super().__init__(user_name, user_email, user_nid)

    def display_profile(self):
        print(f'Driver with name {self.name} and email {self.email}')

    # ekta ride request asbe driver er kache parameter hisebe
    def accept_ride_request(self, ride_request):
        ride_request.set_driver(self) 
        # ************ this set_driver has relation with below set_driver**********


class Ride_details:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.customer = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None
    
    def set_driver(self, driver):
        self.driver = driver
        # **************with this set_driver******************

    def start_ride(self):
        self.start_time = datetime.now()
        
    def end_ride(self, driver, amount):
        self.end_time = datetime.now()
        self.customer.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
    
    def __repr__(self) -> str:
        return f'Ride details and started {self.start_location} to {self.end_location}'

# car/bike khoja. ekta ride er jonno customer hisebe apps er vitor request kora
class Ride_Request:
    def __init__(self, customer, end_location) -> None:
        self.customer = customer
        self.end_location = end_location

class Ride_Matching:
    def __init__(self, drivers) -> None:
        self.available_drivers = drivers

    def find_driver(self, ride_request):
        # check if atleast 1 driver is available in customer's area
        if len(self.available_drivers) > 0 :
            # TODO: find the closest driver of the customer
            found_driver = self.available_drivers[0]
            # creating a ride
            ride = Ride_details(ride_request.customer.current_location, ride_request.end_location)
            found_driver.accept_ride_request(ride)
            return ride
        
class Vehicle(ABC):
    speed = {
        'car': 100,
        'bike': 80,
        'cng': 50
    }

    def __init__(self, vehicle_type, licence_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.licence_plate = licence_plate
        self.rate = rate
        self.status = 'available'

    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, licence_plate, rate) -> None:
        super().__init__(vehicle_type, licence_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'

class Bike(Vehicle):
    def __init__(self, vehicle_type, licence_plate, rate) -> None:
        super().__init__(vehicle_type, licence_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'

niye_jao = Ride_sharing_service('Niye jao')
sakib = Customer('shakib khan', 'sakib@khan.com', 123, 'mohakhali', 1200)
niye_jao.add_customer(sakib)


kala_pakhi = Driver('Kala Pakhi', 'kala@pakhi.com', 321, 'gulshan 1')
niye_jao.add_driver(kala_pakhi)

print(niye_jao)

sakib.request_ride(niye_jao, 'uttara')

sakib.show_current_ride()