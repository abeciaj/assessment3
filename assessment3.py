import re

class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, vehicle_capacity):
        self._vehicle_id = vehicle_id
        self._vehicle_type = vehicle_type
        self._vehicle_capacity = vehicle_capacity

    # Get vehicle_id
    def vehicle_id(self):
        return self._vehicle_id
    
    # Set vehicle_id
    def vehicle_id(self, value):
        if 4 <= len(value) <= 10 and value.isalnum():
            self._vehicle_id = value
        else:
            raise ValueError("Vehicle ID must be alphanumeric and 4-10 characters long.")

    # Get vehicle_type
    def vehicle_type(self):
        return self._vehicle_type

    # Set vehicle_type
    def vehicle_type(self, value):
        if value:
            self._vehicle_type = value
        else:
            raise ValueError("Vehicle Type cannot be empty.")

    # Get vehicle_capacity
    def vehicle_capacity(self):
        return self._vehicle_capacity

    # Set vehicle_capacity
    def vehicle_capacity(self, value):
        if isinstance(value, int) and value > 0:
            self._vehicle_capacity = value
        else:
            raise ValueError("Vehicle Capacity must be a positive integer.")



class FleetManagement():
    def __init__(self):
        self._fleet = []

    def add_item(self):
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

    def update_item(self):
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

            vehicle.vehicle_type = vehicle_type
            vehicle.vehicle_capacity = vehicle_capacity
            print("Vehicle information updated successfully!")
        else:
            print("Vehicle ID not found!")

    def remove_item(self):
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

    def view_all_items(self):
        if not self._fleet:
            print("No vehicles in the fleet.")
            return

        print(f"{'Vehicle ID':<15}{'Vehicle Type':<15}{'Vehicle Capacity':<15}")
        print("-" * 45)
        for vehicle in self._fleet:
            print(f"{vehicle.vehicle_id:<15}{vehicle.vehicle_type:<15}{vehicle.vehicle_capacity:<15}")

        input("Type 'exit' to return to the Fleet Management Menu: ")

    def validate_vehicle_id(vehicle_id):
        return re.match(r"^[a-zA-Z0-9]{4,10}$", vehicle_id) is not None

    def find_vehicle(self, vehicle_id):
        for vehicle in self._fleet:
            if vehicle.vehicle_id == vehicle_id:
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
                self.add_item()
            elif choice == '2':
                self.update_item()
            elif choice == '3':
                self.remove_item()
            elif choice == '4':
                self.view_all_items()
            elif choice == '5':
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid option! Please select a valid option.")


class MainMenu:
    def __init__(self):
        self.fleet_management = FleetManagement()

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
            elif choice == '5':
                print("Exiting the program...")
                break
            else:
                print("Invalid option! Please select a valid option.")


if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.display_menu()