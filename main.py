from employee import Employee
from client import Client
from guest import Guest
from event import Event
from venue import Venue
from supplier import Supplier
from caterer import Caterer
from data_handler import DataHandler

def print_employee_info(employee):
    print(f"Employee: {employee.name}")
    print(f"ID: {employee.employeeID}")
    print(f"Department: {employee.department}")
    print(f"Job Title: {employee.jobTitle}")
    print(f"Salary: {employee.calculateSalary()}")

def print_client_info(client):
    print(f"Client: {client.name}")
    print(f"Budget: {client.budget}")

def print_guest_info(guest):
    print(f"Guest: {guest.name}")

def print_event_info(event):
    print(f"Event: Theme: {event.theme}")
    print(f"Guests: {', '.join(guest.name for guest in event.guests)}")

def print_venue_info(venue):
    print(f"Venue: {venue.name}")
    availability = venue.checkAvailability("2024-06-15", "18:00")
    print(f"Availability: {availability}" if availability else "Not Available")

def print_supplier_info(supplier):
    print(f"Supplier: {supplier.name}")

def main():
    try:
        emp = Employee("John Doe", "EMP001", "Sales", "Sales Manager", 50000, 30, "1992-05-20", "AB123456")
        print_employee_info(emp)
        print()

        client = Client("CL001", "ABC Company", "123 Main St", "123-456-7890", 10000)
        print_client_info(client)
        client.updateBudget(12000)
        print(f"Updated Budget: {client.budget}")
        print()

        guest = Guest("G001", "Alice", "456 Elm St", "987-654-3210")
        print_guest_info(guest)
        print()

        event = Event("E001", "Wedding", "Spring Theme", "2024-06-15", "18:00", 4, "789 Oak St")
        event.addGuest(guest)
        print_event_info(event)
        print()

        venue = Venue("V001", "Grand Hall", "789 Oak St", "123-456-7890", 50, 200)
        print_venue_info(venue)
        print()

        supplier1 = Supplier("S001", "ABC Catering", "100 Main St", "987-654-3210")
        print_supplier_info(supplier1)

        caterer = Caterer("C001", "XYZ Catering", "200 Elm St", "789-456-1230", "Menu", 50, 150)
        print_supplier_info(caterer)

        data = [emp, client, guest, event, venue, supplier1, caterer]
        DataHandler.saveData(data, "data.pickle")
        loaded_data = DataHandler.loadData("data.pickle")

        print("\nLoaded Data:")
        for obj in loaded_data:
            print(obj)
        print()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
