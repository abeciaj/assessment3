import re
from datetime import datetime

#--------Defining the classes---------------
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, vehicle_capacity):
        self.set_vehicle_id(vehicle_id)
        self.set_vehicle_type(vehicle_type)
        self.set_vehicle_capacity(vehicle_capacity)

    # Getter and Setter for vehicle_id
    def get_vehicle_id(self):
        return self.__vehicle_id

    def set_vehicle_id(self, vehicle_id):
        if not (4 <= len(vehicle_id) <= 10 and vehicle_id.isalnum()):
            raise ValueError("Vehicle ID must be alphanumeric and 4-10 characters long.")
        self.__vehicle_id = vehicle_id

    # Getter and Setter for vehicle_type
    def get_vehicle_type(self):
        return self.__vehicle_type

    def set_vehicle_type(self, vehicle_type):
        if not vehicle_type:
            raise ValueError("Vehicle Type cannot be empty.")
        self.__vehicle_type = vehicle_type

    # Getter and Setter for vehicle_capacity
    def get_vehicle_capacity(self):
        return self.__vehicle_capacity

    def set_vehicle_capacity(self, vehicle_capacity):
        if not (isinstance(vehicle_capacity, int) and vehicle_capacity > 0):
            raise ValueError("Vehicle Capacity must be a positive integer.")
        self.__vehicle_capacity = vehicle_capacity


class Customer:
    def __init__(self, customer_id, name, dob, address, phone_num, email):
        self.customer_id = customer_id
        self.name = name
        self.dob = dob
        self.address = address
        self.phone_num = phone_num
        self.email = email
        
        
    def print_values(self):
        print(f"{self.customer_id:<15}{self.name:<20}{self.address:<30}{self.phone_num:<15}{self.email:<20}")
        
class Shipment:
    def __init__(self, shipment_id, origin, destination, weight, vehicle_id, customer_id):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.vehicle_id = vehicle_id
        self.customer_id = customer_id
        self.status = "In Transit"
        self.delivery_date = None
        
        
        
class FleetManagement():
    def __init__(self):
        self._fleet = []
        
#-----Add Vehicle-----
    def add_vehicle(self):
        vehicle_id = input("Enter Vehicle ID (e.g., V001): ")
        if not self.validate_vehicle_id(vehicle_id):
            print("Invalid Vehicle ID! Must be alphanumeric and 4-10 characters long.")
            return

        vehicle_type = input("Enter Vehicle Type (e.g., Truck, Van, Car): ")
        try:
            vehicle_capacity = int(input("Enter Vehicle Capacity in kg (e.g., 1000): "))
            if vehicle_capacity <= 0:
                print("Vehicle Capacity must be a positive integer!")
                return
        except ValueError:
            print("Invalid capacity! It must be an integer.")
            return

        new_vehicle = Vehicle(vehicle_id, vehicle_type, vehicle_capacity)
        self._fleet.append(new_vehicle)
        print("Vehicle added successfully!")

#-----Update Vehicle-----
    def update_vehicle(self):
        vehicle_id = input("Enter Vehicle ID to update: ")
        vehicle = self.find_vehicle(vehicle_id)
        if vehicle:
            vehicle_type = input("Enter new Vehicle Type: ")
            try:
                vehicle_capacity = int(input("Enter new Vehicle Capacity: "))
                if vehicle_capacity <= 0:
                    print("Vehicle Capacity must be a positive integer!")
                    return
            except ValueError:
                print("Invalid capacity! It must be an integer.")
                return

            vehicle.set_vehicle_type(vehicle_type)
            vehicle.set_vehicle_capacity(vehicle_capacity)
            print("Vehicle information updated successfully!")
        else:
            print("Vehicle ID not found!")

#-----Remove Vehicle-----
    def remove_vehicle(self):
        vehicle_id = input("Enter Vehicle ID to remove: ")
        vehicle = self.find_vehicle(vehicle_id)
        if vehicle:
            confirm = input(f"Are you sure you want to remove vehicle {vehicle_id}? (yes/no): ")
            if confirm.lower() == 'yes':
                self._fleet.remove(vehicle)
                print("Vehicle removed successfully!")
            else:
                print("Operation canceled.")
        else:
            print("Vehicle ID not found!")

#-----View All Vehicle-----
    def view_all_vehicles(self):
        if not self._fleet:
            print("No vehicles in the fleet.")
            return

        print(f"{'Vehicle ID':<15}{'Vehicle Type':<15}{'Vehicle Capacity':<15}")
        print("-" * 45)
        for vehicle in self._fleet:
            print(f"{vehicle.get_vehicle_id():<15}{vehicle.get_vehicle_type():<15}{vehicle.get_vehicle_capacity():<15}")

        input("Press Enter to return to the Fleet Management Menu: ")

    def validate_vehicle_id(self, vehicle_id):
        return re.match(r"^[a-zA-Z0-9]{4,10}$", vehicle_id) is not None
    
#-----Find Vehicle-----
    def find_vehicle(self, vehicle_id):
        for vehicle in self._fleet:
            if vehicle.get_vehicle_id() == vehicle_id:
                return vehicle
        return None

    def fleet_menu(self):
        while True:
            print("\nFleet Management Menu:")
            print("1. Add a vehicle")
            print("2. Update vehicle information")
            print("3. Remove a vehicle")
            print("4. View all vehicles")
            print("5. Quit fleet management")

            choice = input("Select an option: ")

            if choice == '1':
                self.add_vehicle()
            elif choice == '2':
                self.update_vehicle()
            elif choice == '3':
                self.remove_vehicle()
            elif choice == '4':
                self.view_all_vehicles()
            elif choice == '5':
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid option! Please select a valid option.")

   
   
   
class CustomerManagement:
    def __init__(self):
        self.customers = []

#--Adding Customer
    def add_customer(self):
        customer_id = input("Enter Customer ID (e.g., ABC123): ")
        if not self.validate_customer_id(customer_id):
            print("Invalid Customer ID! Must be alphanumeric and 4-10 characters long.")
            return

        name = input("Enter Name (e.g., John Smith): ")

        dob = input("Enter Date of Birth (DD/MM/YYYY): ")
        if not self.validate_dob(dob):
            print("Invalid Date of Birth! Must be in DD/MM/YYYY format and age must be at least 18.")
            return

        address = input("Enter Address (e.g., 123 Main St, Sydney, NSW 2000, Australia): ")
        if not self.validate_address(address):
            print("Invalid Address! Must be a valid Australian address.")
            return

        phone_num = input("Enter Contact Number Information (Phone: 04XXXXXXXX: ")
        if not self.validate_phone_num(phone_num):
            print("Invalid Contact Number Information! Ensure phone number formats are correct.")
            return
        
        email = input("Enter Email (Email: john@example.com): ")
        if not self.validate_email(email):
            print("Invalid Email! Ensure email formats are correct.")
            return

        new_customer = Customer(customer_id, name, dob, address, phone_num, email)
        self.customers.append(new_customer)  
        print("Customer added successfully!")
        


#--Updating customer 
    def update_customer(self):
        customer_id = input("Enter Customer ID to update: ")
        customer = self.find_customer_by_id(customer_id)
        if not customer:
            print("Customer ID not found!")
            return

        name = input("Enter new Name: ")

        dob = input("Enter new Date of Birth (DD/MM/YYYY): ")
        if not self.validate_dob(dob):
            print("Invalid Date of Birth! Must be in DD/MM/YYYY format and age must be at least 18.")
            return

        address = input("Enter new Address: ")
        if not self.validate_address(address):
            print("Invalid Address! Must be a valid Australian address.")
            return

        phone_num = input("Enter new Contact Phone Information: ")
        if not self.validate_phone_num(phone_num):
            print("Invalid Contact Phone Information! Ensure phone number formats are correct.")
            return
        
        email = input("Enter new Email: ")
        if not self.validate_email(email):
            print("Invalid Email! Ensure email formats are correct.")
            return
        
        customer.name = name
        customer.dob = dob
        customer.address = address
        customer.phone_num = phone_num
        customer.email = email
        print("Customer information updated successfully!")


#--Removing customer
    def remove_customer(self):
        customer_id = input("Enter Customer ID to remove: ")
        customer = self.find_customer_by_id(customer_id)
        if not customer:
            print("Customer ID not found!")
            return

        confirm = input(f"Are you sure you want to remove customer {customer_id}? (yes/no): ")
        if confirm.lower() == 'yes':
            self.customers.remove(customer)  
            print("Customer removed successfully!")
        else:
            print("Operation canceled.")

#--View all customers
    def view_all_customers(self):
        if not self.customers:
            print("No customers found.")
            return

        print(f"{'Customer ID':<15}{'Name':<20}{'Address':<30}{'Phone Numer':<15}{'Email':<20}")
        print("-" * 95)
        for customer in self.customers:
            customer.print_values()  

        input("Press Enter to return to the Customer Management Menu: ")
        

#--View customer shipments
    def view_customer_shipments(self, shipment_management):
        customer_id = input("Enter Customer ID to view shipments: ")
        customer = self.find_customer_by_id(customer_id)
        if not customer:
            print("Customer ID not found!")
            return
        
        # # Dummy data for shipments, this can be linked to actual shipment objects later.
        # print(f"Viewing shipments for customer {customer_id}:")
        # print(f"{'Shipment ID':<15}{'Origin':<15}{'Destination':<15}{'Weight':<10}{'Vehicle ID':<15}{'Status':<15}{'Delivery Date':<15}")
        # print("-" * 95)
     

        # input("Press Enter to return to the Customer Management Menu...")
    

#----Validation for customer information 
    def find_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

  
    def validate_customer_id(self, customer_id):
        return 4 <= len(customer_id) <= 10 and customer_id.isalnum()

    
    def validate_dob(self, dob):
        try:
            dob_datetime = datetime.strptime(dob, "%d/%m/%Y")
            age = (datetime.now() - dob_datetime).days // 365
            return age >= 18
        except ValueError:
            return False
  
    def validate_address(self, address):
       return re.match(r".+, (NSW|VIC|QLD|SA|WA|TAS|ACT|NT) \d{4}, Australia", address) is not None

   
    def validate_phone_num(self, phone_num):
       phone_pattern = re.compile(r"^04\d{8}$")
       return phone_pattern.match(phone_num) is not None
   
    def validate_email(self, email):
        email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        return email_pattern.match(email) is not None

    
    
    
    
    def customer_menu(self, shipment_management):
        while True:
            print("\nCustomer Management Menu:")
            print("1. Add a customer")
            print("2. Update customer information")
            print("3. Remove a customer")
            print("4. View all customers")
            print("5. View a customer's shipments")
            print("6. Quit customer management")

            choice = input("Select an option: ")

            if choice == '1':
                self.add_customer()
            elif choice == '2':
                self.update_customer()
            elif choice == '3':
                self.remove_customer()
            elif choice == '4':
                self.view_all_customers()
            elif choice == '5':
                self.view_customer_shipments(shipment_management)
            elif choice == '6':
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid option! Please select a valid option.")









#---------------Shipment Management--------------




class ShipmentManagement:
    
    def __init__(self):
                 self.shipments = []
                 
    
    def add_shipment(self, fleet_management, customer_management):
        shipment_id = input("Enter the Shipment ID (e.g., S123): ")
        if not self.validate_shipment_id(shipment_id):
            print("Invalid shipment Id, It must be the alphanumeric with 4 characters ")
            return
        
        origin = input("Enter the Origin Location (e.g., Sydney, NSW, Australia): ")
        destination = input("Enter the Destination Location (e.g., Melbourne, VIC, Australia): ")
        
        try:
            weight = float(input("Enter the Weight in kg (e.g., 500): "))
            if not self.validate_weight(weight):
                print("Invalid weight, The weight must be positive.")
        
        except ValueError:
            print("Invalid input, Weight must have a numeric value")
            return
        
        print("Available Vehicles: ")
        fleet_management.view_all_vehicles()
        vehicle_id = input("Select a Vehicle ID: ")
        vehicle = fleet_management.find_vehicle(vehicle_id)
        if not vehicle:
            print("Invalid Vehicle ID")
            return
        print("Available Customers: ")
        customer_management.view_all_customers()
        customer_id = input("Enter Customer ID for the shipment: ")
        customer = customer_management.find_customer_by_id(customer_id)
        if not customer:
            print("Invalid Customer ID")
            return
        
        new_shipment = Shipment(shipment_id, origin, destination, weight, vehicle_id, customer_id)
        self.shipments.append(new_shipment)
        print("Shipment ", shipment_id, " has been created successfully!")
        
        
        
    def track_shipment(self):
        shipment_id = input("Please Enter the Shipment ID to track: ")
        shipment = self.find_shipment(shipment_id)
        if not shipment:
            print("Shipment ", shipment_id, " not found")
            return
        
        print(f"Shipment Status: {shipment.status}")
        
        
    def view_all_shipments(self):
        if not self.shipments:
            print("No shipments are available")
            return
        
        print(f"{'Shipment ID':<15}{'Origin':<20}{'Destination':<20}{'Weight':<10}{'Vehicle ID':<15}{'Status':<15}{'Delivery Date':<20}")
        for shipment in self.shipments:
            delivery_date = shipment.delivery_date if shipment.delivery_date else "N/A"
            print(f"{shipment.shipment_id:<15}{shipment.origin:<20}{shipment.destination:<20}{shipment.weight:<10}{shipment.vehicle_id:<15}{shipment.status:<15}{delivery_date:<20}")

    def find_shipment(self, shipment_id):
        for shipment in self.shipments:
            if shipment.shipment_id == shipment_id:
                return shipment
        return None
  
    

    def validate_shipment_id(self, shipment_id):
        return bool(re.match(r'^[A-Za-z0-9]{3,6}$', shipment_id))
    
    def validate_weight(self, weight):
        return weight > 0
    
    def validate_customer_id(self, customer_id):
        return customer_id in self.customers
    
    def get_vehicle_by_id(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None
    
    def get_shipment_by_id(self, shipment_id):
        for shipment in self.shipments:
            if shipment.shipment_id == shipment_id:
                return shipment
        return None
    
    def display_vehicles(self):
        print("Available Vehicles: ")
        for vehicle in self.vehicles:
            print("")
            
            
    def shipment_menu(self, fleet_management, customer_management):
        while True:
            print("\nShipment Management Menu:")
            print("1. Create a new shipment")
            print("2. Track a shipment")
            print("3. View all shipments")
            print("4. Quit shipment management")

            choice = input("Select an option: ")

            if choice == '1':
                self.add_shipment(fleet_management, customer_management)
            elif choice == '2':
                self.track_shipment()
            elif choice == '3':
                self.view_all_shipments()
            elif choice == '4':
                print("Returning to the Main Menu ")
                break
            else:
                print("Invalid option! Please select a valid option.")
            
    
        
#-----------Functions for Delivery Management ------------------       
        
class DeliveryManagement:
    def __init__(self, shipment_management):
                 self.shipment_management = shipment_management
                 
    def mark_delivery(self):
        shipment_id = input("Enter Shipment ID to mark delivery: ")
        shipment = self.shipment_management.find_shipment(shipment_id)
        if shipment:
            if shipment.status == 'Delivered':
                print(f"Shipment {shipment_id} has already been delivered!")
                return
        
            shipment.status =  "Delivered"
            shipment.delivery_date = datetime.now().strftime("%d/%m/%Y %H:%M")
            print("Shipment", shipment_id , " has been marked as delivered successfully")
        else:
            print("Shipment", shipment_id, " not found")
        
        
    
    def view_delivery_status(self):
        shipment_id = input("Enter Shipment ID to view delivery status: ")
        shipment = self.shipment_management.find_shipment(shipment_id)
        if shipment:
            if shipment.status == 'Delivered':
                print(f"Shipment {shipment_id} was delivered on {shipment.delivery_date}.")
            else:
                print(f"Shipment {shipment_id} is still in transit.")
        else:
            print(f"Shipment {shipment_id} not found!")
        

    
    def delivery_menu(self, shipment_management):
        while True:
            print("\nShipment Management Menu:")
            print("1. Mark shipment delivery")
            print("2. View delivery status for a shipment")
            print("3. Quit delivery management")
     
            choice = input("Select an option: ")

            if choice == '1':
                self.mark_delivery()
            elif choice == '2':
                self.view_delivery_status()
            elif choice == '3':
                break
            else:
                print("Invalid option! Please select a valid option.")
    








#----------------Main menu for the Program

class MainMenu:
    def __init__(self):
        self.fleet_management = FleetManagement()
        self.customer_management = CustomerManagement()
        self.shipment_management = ShipmentManagement()
        self.delivery_management = DeliveryManagement(self.shipment_management)

    def display_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Fleet Management")
            print("2. Customer Management")
            print("3. Shipment Management")
            print("4. Delivery Management")
            print("5. Exit")

            choice = input("Select an option: ")

            if choice == '1':
                self.fleet_management.fleet_menu()
            elif choice == '2':
                self.customer_management.customer_menu(self.shipment_management)
            elif choice == '3':
                self.shipment_management.shipment_menu(self.fleet_management, self.customer_management)
            elif choice == '4':
                self.delivery_management.delivery_menu(self.shipment_management)
            elif choice == '5':
                print("Exiting the program...")
                break
            else:
                print("Invalid option! Please select a valid option.")
                
                
    

if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.display_menu()
