import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Employee:
    def __init__(self, name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails):
        self.name = name
        self.employeeID = employeeID
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.age = age
        self.dateOfBirth = dateOfBirth
        self.passportDetails = passportDetails

class Event:
    def __init__(self, eventID, type, theme, date, time, duration, venueAddress):
        self.eventID = eventID
        self.type = type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venueAddress = venueAddress

class Venue:
    def __init__(self, venueID, name, address, contactDetails, minGuests, maxGuests):
        self.venueID = venueID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.minGuests = minGuests
        self.maxGuests = maxGuests

class Client:
    def __init__(self, clientID, name, address, contactDetails, budget):
        self.clientID = clientID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.budget = budget

class Guest:
    def __init__(self, guestID, name, address, contactDetails):
        self.guestID = guestID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

class Supplier:
    def __init__(self, supplierID, name, address, contactDetails):
        self.supplierID = supplierID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

class Caterer(Supplier):
    def __init__(self, catererID, name, address, contactDetails, menu, minGuests, maxGuests):
        super().__init__(catererID, name, address, contactDetails)
        self.menu = menu
        self.minGuests = minGuests
        self.maxGuests = maxGuests

class GUI:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Event Management System")
        self.root.geometry("800x600")

        self.create_tabs()

    def create_tabs(self):
        self.tabControl = ttk.Notebook(self.root)

        self.employee_tab = tk.Frame(self.tabControl)
        self.client_tab = tk.Frame(self.tabControl)
        self.guest_tab = tk.Frame(self.tabControl)
        self.event_tab = tk.Frame(self.tabControl)
        self.supplier_tab = tk.Frame(self.tabControl)
        self.caterer_tab = tk.Frame(self.tabControl)
        self.venue_tab = tk.Frame(self.tabControl)

        self.tabControl.add(self.employee_tab, text="Employees")
        self.tabControl.add(self.client_tab, text="Clients")
        self.tabControl.add(self.guest_tab, text="Guests")
        self.tabControl.add(self.event_tab, text="Events")
        self.tabControl.add(self.supplier_tab, text="Suppliers")
        self.tabControl.add(self.caterer_tab, text="Caterers")
        self.tabControl.add(self.venue_tab, text="Venues")

        self.tabControl.pack(expand=1, fill="both")

        self.create_employee_tab()
        self.create_client_tab()
        self.create_guest_tab()
        self.create_event_tab()
        self.create_supplier_tab()
        self.create_caterer_tab()
        self.create_venue_tab()

    def create_employee_tab(self):
        lbl_name = tk.Label(self.employee_tab, text="Employee Name:")
        lbl_name.grid(row=0, column=0, padx=5, pady=5)
        self.emp_name_entry = tk.Entry(self.employee_tab)
        self.emp_name_entry.grid(row=0, column=1, padx=5, pady=5)

        lbl_id = tk.Label(self.employee_tab, text="Employee ID:")
        lbl_id.grid(row=1, column=0, padx=5, pady=5)
        self.emp_id_entry = tk.Entry(self.employee_tab)
        self.emp_id_entry.grid(row=1, column=1, padx=5, pady=5)

        lbl_department = tk.Label(self.employee_tab, text="Department:")
        lbl_department.grid(row=2, column=0, padx=5, pady=5)
        self.department_entry = tk.Entry(self.employee_tab)
        self.department_entry.grid(row=2, column=1, padx=5, pady=5)

        lbl_job_title = tk.Label(self.employee_tab, text="Job Title:")
        lbl_job_title.grid(row=3, column=0, padx=5, pady=5)
        self.job_title_entry = tk.Entry(self.employee_tab)
        self.job_title_entry.grid(row=3, column=1, padx=5, pady=5)

        lbl_basic_salary = tk.Label(self.employee_tab, text="Basic Salary:")
        lbl_basic_salary.grid(row=4, column=0, padx=5, pady=5)
        self.basic_salary_entry = tk.Entry(self.employee_tab)
        self.basic_salary_entry.grid(row=4, column=1, padx=5, pady=5)

        lbl_age = tk.Label(self.employee_tab, text="Age:")
        lbl_age.grid(row=5, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.employee_tab)
        self.age_entry.grid(row=5, column=1, padx=5, pady=5)

        lbl_date_of_birth = tk.Label(self.employee_tab, text="Date of Birth:")
        lbl_date_of_birth.grid(row=6, column=0, padx=5, pady=5)
        self.date_of_birth_entry = tk.Entry(self.employee_tab)
        self.date_of_birth_entry.grid(row=6, column=1, padx=5, pady=5)

        lbl_passport_details = tk.Label(self.employee_tab, text="Passport Details:")
        lbl_passport_details.grid(row=7, column=0, padx=5, pady=5)
        self.passport_details_entry = tk.Entry(self.employee_tab)
        self.passport_details_entry.grid(row=7, column=1, padx=5, pady=5)

        btn_add = tk.Button(self.employee_tab, text="Add Employee", command=self.add_employee)
        btn_add.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        btn_update = tk.Button(self.employee_tab, text="Update Employee", command=self.update_employee)
        btn_update.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        btn_delete = tk.Button(self.employee_tab, text="Delete Employee", command=self.delete_employee)
        btn_delete.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

        btn_display = tk.Button(self.employee_tab, text="Display Details", command=self.display_employee_details)
        btn_display.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

    def add_employee(self):
        name = self.emp_name_entry.get()
        employee_id = self.emp_id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()
        age = self.age_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        passport_details = self.passport_details_entry.get()

        emp = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        messagebox.showinfo("Add Employee", f"Employee Added:\n\n{emp.__dict__}")

    def update_employee(self):
        name = self.emp_name_entry.get()
        employee_id = self.emp_id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()
        age = self.age_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        passport_details = self.passport_details_entry.get()

        emp = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        messagebox.showinfo("Update Employee", f"Employee Updated:\n\n{emp.__dict__}")

    def delete_employee(self):
        employee_id = self.emp_id_entry.get()
        messagebox.showinfo("Delete Employee", f"Employee Deleted with ID: {employee_id}")

    def display_employee_details(self):
        name = self.emp_name_entry.get()
        employee_id = self.emp_id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()
        age = self.age_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        passport_details = self.passport_details_entry.get()

        emp = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        messagebox.showinfo("Employee Details", f"Employee Details:\n\nName: {emp.name}\nID: {emp.employeeID}\nDepartment: {emp.department}\nJob Title: {emp.jobTitle}\nBasic Salary: {emp.basicSalary}\nAge: {emp.age}\nDate of Birth: {emp.dateOfBirth}\nPassport Details: {emp.passportDetails}")

    def create_client_tab(self):
        lbl_id = tk.Label(self.client_tab, text="Client ID:")
        lbl_id.grid(row=0, column=0, padx=5, pady=5)
        self.client_id_entry = tk.Entry(self.client_tab)
        self.client_id_entry.grid(row=0, column=1, padx=5, pady=5)

        lbl_name = tk.Label(self.client_tab, text="Name:")
        lbl_name.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.client_tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        lbl_address = tk.Label(self.client_tab, text="Address:")
        lbl_address.grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.client_tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        lbl_contact = tk.Label(self.client_tab, text="Contact Details:")
        lbl_contact.grid(row=3, column=0, padx=5, pady=5)
        self.contact_entry = tk.Entry(self.client_tab)
        self.contact_entry.grid(row=3, column=1, padx=5, pady=5)

        lbl_budget = tk.Label(self.client_tab, text="Budget:")
        lbl_budget.grid(row=4, column=0, padx=5, pady=5)
        self.budget_entry = tk.Entry(self.client_tab)
        self.budget_entry.grid(row=4, column=1, padx=5, pady=5)

        btn_add = tk.Button(self.client_tab, text="Add Client", command=self.add_client)
        btn_add.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        btn_update = tk.Button(self.client_tab, text="Update Client", command=self.update_client)
        btn_update.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        btn_delete = tk.Button(self.client_tab, text="Delete Client", command=self.delete_client)
        btn_delete.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        btn_display = tk.Button(self.client_tab, text="Display Details", command=self.display_client_details)
        btn_display.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    def add_client(self):
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        budget = self.budget_entry.get()

        client = Client(client_id, name, address, contact_details, budget)
        messagebox.showinfo("Add Client", f"Client Added:\n\n{client.__dict__}")

    def update_client(self):
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        budget = self.budget_entry.get()

        client = Client(client_id, name, address, contact_details, budget)
        messagebox.showinfo("Update Client", f"Client Updated:\n\n{client.__dict__}")

    def delete_client(self):
        client_id = self.client_id_entry.get()
        messagebox.showinfo("Delete Client", f"Client Deleted with ID: {client_id}")

    def display_client_details(self):
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        budget = self.budget_entry.get()
    
        client_details = f"Client ID: {client_id}\nName: {name}\nAddress: {address}\nContact Details: {contact_details}\nBudget: {budget}"
        messagebox.showinfo("Client Details", client_details)


    def create_guest_tab(self):
        lbl_id = tk.Label(self.guest_tab, text="Guest ID:")
        lbl_id.grid(row=0, column=0, padx=5, pady=5)
        self.guest_id_entry = tk.Entry(self.guest_tab)
        self.guest_id_entry.grid(row=0, column=1, padx=5, pady=5)

        lbl_name = tk.Label(self.guest_tab, text="Name:")
        lbl_name.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.guest_tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        lbl_address = tk.Label(self.guest_tab, text="Address:")
        lbl_address.grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.guest_tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        lbl_contact = tk.Label(self.guest_tab, text="Contact Details:")
        lbl_contact.grid(row=3, column=0, padx=5, pady=5)
        self.contact_entry = tk.Entry(self.guest_tab)
        self.contact_entry.grid(row=3, column=1, padx=5, pady=5)

        btn_add = tk.Button(self.guest_tab, text="Add Guest", command=self.add_guest)
        btn_add.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        btn_update = tk.Button(self.guest_tab, text="Update Guest", command=self.update_guest)
        btn_update.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        btn_delete = tk.Button(self.guest_tab, text="Delete Guest", command=self.delete_guest)
        btn_delete.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        btn_display = tk.Button(self.guest_tab, text="Display Details", command=self.display_guest_details)
        btn_display.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def add_guest(self):
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()

        guest = Guest(guest_id, name, address, contact_details)
        messagebox.showinfo("Add Guest", f"Guest Added:\n\n{guest.__dict__}")

    def update_guest(self):
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()

        guest = Guest(guest_id, name, address, contact_details)
        messagebox.showinfo("Update Guest", f"Guest Updated:\n\n{guest.__dict__}")

    def delete_guest(self):
        guest_id = self.guest_id_entry.get()
        messagebox.showinfo("Delete Guest", f"Guest Deleted with ID: {guest_id}")

    def display_guest_details(self):
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()

        guest = Guest(guest_id, name, address, contact_details)
        messagebox.showinfo("Guest Details", f"Guest Details:\n\nID: {guest.guestID}\nName: {guest.name}\nAddress: {guest.address}\nContact Details: {guest.contactDetails}")

    def create_event_tab(self):
        lbl_id = tk.Label(self.event_tab, text="Event ID:")
        lbl_id.grid(row=0, column=0, padx=5, pady=5)
        self.event_id_entry = tk.Entry(self.event_tab)
        self.event_id_entry.grid(row=0, column=1, padx=5, pady=5)

        lbl_type = tk.Label(self.event_tab, text="Type:")
        lbl_type.grid(row=1, column=0, padx=5, pady=5)
        self.type_entry = tk.Entry(self.event_tab)
        self.type_entry.grid(row=1, column=1, padx=5, pady=5)

        lbl_theme = tk.Label(self.event_tab, text="Theme:")
        lbl_theme.grid(row=2, column=0, padx=5, pady=5)
        self.theme_entry = tk.Entry(self.event_tab)
        self.theme_entry.grid(row=2, column=1, padx=5, pady=5)

        lbl_date = tk.Label(self.event_tab, text="Date:")
        lbl_date.grid(row=3, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self.event_tab)
        self.date_entry.grid(row=3, column=1, padx=5, pady=5)

        lbl_time = tk.Label(self.event_tab, text="Time:")
        lbl_time.grid(row=4, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self.event_tab)
        self.time_entry.grid(row=4, column=1, padx=5, pady=5)

        lbl_duration = tk.Label(self.event_tab, text="Duration:")
        lbl_duration.grid(row=5, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(self.event_tab)
        self.duration_entry.grid(row=5, column=1, padx=5, pady=5)

        lbl_venue_address = tk.Label(self.event_tab, text="Venue Address:")
        lbl_venue_address.grid(row=6, column=0, padx=5, pady=5)
        self.venue_address_entry = tk.Entry(self.event_tab)
        self.venue_address_entry.grid(row=6, column=1, padx=5, pady=5)

        btn_add = tk.Button(self.event_tab, text="Add Event", command=self.add_event)
        btn_add.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        btn_update = tk.Button(self.event_tab, text="Update Event", command=self.update_event)
        btn_update.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        btn_delete = tk.Button(self.event_tab, text="Delete Event", command=self.delete_event)
        btn_delete.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        btn_display = tk.Button(self.event_tab, text="Display Details", command=self.display_event_details)
        btn_display.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

    def add_event(self):
        event_id = self.event_id_entry.get()
        type = self.type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue_address = self.venue_address_entry.get()

        event = Event(event_id, type, theme, date, time, duration, venue_address)
        messagebox.showinfo("Add Event", f"Event Added:\n\n{event.__dict__}")

    def update_event(self):
        event_id = self.event_id_entry.get()
        type = self.type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue_address = self.venue_address_entry.get()

        event = Event(event_id, type, theme, date, time, duration, venue_address)
        messagebox.showinfo("Update Event", f"Event Updated:\n\n{event.__dict__}")

    def delete_event(self):
        event_id = self.event_id_entry.get()
        messagebox.showinfo("Delete Event", f"Event Deleted with ID: {event_id}")

    def display_event_details(self):
        event_id = self.event_id_entry.get()
        event_type = self.type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue_address = self.venue_address_entry.get()

        event = Event(event_id, event_type, theme, date, time, duration, venue_address)
        messagebox.showinfo("Event Details", f"Event Details:\n\nID: {event.eventID}\nType: {event.type}\nTheme: {event.theme}\nDate: {event.date}\nTime: {event.time}\nDuration: {event.duration}\nVenue Address: {event.venueAddress}")
        
    def create_supplier_tab(self):
        lbl_id = tk.Label(self.supplier_tab, text="Supplier ID:")
        lbl_id.grid(row=0, column=0, padx=5, pady=5)
        self.supplier_id_entry = tk.Entry(self.supplier_tab)
        self.supplier_id_entry.grid(row=0, column=1, padx=5, pady=5)

        lbl_name = tk.Label(self.supplier_tab, text="Name:")
        lbl_name.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.supplier_tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        lbl_address = tk.Label(self.supplier_tab, text="Address:")
        lbl_address.grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.supplier_tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        lbl_contact = tk.Label(self.supplier_tab, text="Contact Details:")
        lbl_contact.grid(row=3, column=0, padx=5, pady=5)
        self.contact_entry = tk.Entry(self.supplier_tab)
        self.contact_entry.grid(row=3, column=1, padx=5, pady=5)

        btn_add = tk.Button(self.supplier_tab, text="Add Supplier", command=self.add_supplier)
        btn_add.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        btn_update = tk.Button(self.supplier_tab, text="Update Supplier", command=self.update_supplier)
        btn_update.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        btn_delete = tk.Button(self.supplier_tab, text="Delete Supplier", command=self.delete_supplier)
        btn_delete.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        btn_display = tk.Button(self.supplier_tab, text="Display Details", command=self.display_supplier_details)
        btn_display.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def add_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()

        supplier = Supplier(supplier_id, name, address, contact_details)
        messagebox.showinfo("Add Supplier", f"Supplier Added:\n\n{supplier.__dict__}")

    def update_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()

        supplier = Supplier(supplier_id, name, address, contact_details)
        messagebox.showinfo("Update Supplier", f"Supplier Updated:\n\n{supplier.__dict__}")

    def delete_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        messagebox.showinfo("Delete Supplier", f"Supplier Deleted with ID: {supplier_id}")

    def display_supplier_details(self):
        supplier_id = self.supplier_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()

        supplier = Supplier(supplier_id, name, address, contact_details)
        messagebox.showinfo("Supplier Details", f"Supplier Details:\n\nID: {supplier.supplierID}\nName: {supplier.name}\nAddress: {supplier.address}\nContact Details: {supplier.contactDetails}")


    def create_caterer_tab(self):
        lbl_id = tk.Label(self.caterer_tab, text="Caterer ID:")
        lbl_id.grid(row=0, column=0, padx=5, pady=5)
        self.caterer_id_entry = tk.Entry(self.caterer_tab)
        self.caterer_id_entry.grid(row=0, column=1, padx=5, pady=5)

        lbl_name = tk.Label(self.caterer_tab, text="Name:")
        lbl_name.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.caterer_tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        lbl_address = tk.Label(self.caterer_tab, text="Address:")
        lbl_address.grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.caterer_tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        lbl_contact = tk.Label(self.caterer_tab, text="Contact Details:")
        lbl_contact.grid(row=3, column=0, padx=5, pady=5)
        self.contact_entry = tk.Entry(self.caterer_tab)
        self.contact_entry.grid(row=3, column=1, padx=5, pady=5)

        lbl_menu = tk.Label(self.caterer_tab, text="Menu:")
        lbl_menu.grid(row=4, column=0, padx=5, pady=5)
        self.menu_entry = tk.Entry(self.caterer_tab)
        self.menu_entry.grid(row=4, column=1, padx=5, pady=5)

        lbl_min_guests = tk.Label(self.caterer_tab, text="Minimum Guests:")
        lbl_min_guests.grid(row=5, column=0, padx=5, pady=5)
        self.min_guests_entry = tk.Entry(self.caterer_tab)
        self.min_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        lbl_max_guests = tk.Label(self.caterer_tab, text="Maximum Guests:")
        lbl_max_guests.grid(row=6, column=0, padx=5, pady=5)
        self.max_guests_entry = tk.Entry(self.caterer_tab)
        self.max_guests_entry.grid(row=6, column=1, padx=5, pady=5)

        btn_add = tk.Button(self.caterer_tab, text="Add Caterer", command=self.add_caterer)
        btn_add.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        btn_update = tk.Button(self.caterer_tab, text="Update Caterer", command=self.update_caterer)
        btn_update.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        btn_delete = tk.Button(self.caterer_tab, text="Delete Caterer", command=self.delete_caterer)
        btn_delete.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        btn_display = tk.Button(self.caterer_tab, text="Display Details", command=self.display_caterer_details)
        btn_display.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

    def add_caterer(self):
        caterer_id = self.caterer_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        menu = self.menu_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        caterer = Caterer(caterer_id, name, address, contact_details, menu, min_guests, max_guests)
        messagebox.showinfo("Add Caterer", f"Caterer Added:\n\n{caterer.__dict__}")

    def update_caterer(self):
        caterer_id = self.caterer_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        menu = self.menu_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        caterer = Caterer(caterer_id, name, address, contact_details, menu, min_guests, max_guests)
        messagebox.showinfo("Update Caterer", f"Caterer Updated:\n\n{caterer.__dict__}")

    def delete_caterer(self):
        caterer_id = self.caterer_id_entry.get()
        messagebox.showinfo("Delete Caterer", f"Caterer Deleted with ID: {caterer_id}")

    def display_caterer_details(self):
        caterer_id = self.caterer_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        menu = self.menu_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        caterer = Caterer(caterer_id, name, address, contact_details, menu, min_guests, max_guests)
        messagebox.showinfo("Caterer Details", f"Caterer Details:\n\nID: {caterer_id}\nName: {name}\nAddress: {address}\nContact Details: {contact_details}\nMenu: {menu}\nMinimum Guests: {min_guests}\nMaximum Guests: {max_guests}")

    def create_venue_tab(self):
        lbl_id = tk.Label(self.venue_tab, text="Venue ID:")
        lbl_id.grid(row=0, column=0, padx=5, pady=5)
        self.venue_id_entry = tk.Entry(self.venue_tab)
        self.venue_id_entry.grid(row=0, column=1, padx=5, pady=5)

        lbl_name = tk.Label(self.venue_tab, text="Name:")
        lbl_name.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.venue_tab)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        lbl_address = tk.Label(self.venue_tab, text="Address:")
        lbl_address.grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.venue_tab)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        lbl_contact = tk.Label(self.venue_tab, text="Contact Details:")
        lbl_contact.grid(row=3, column=0, padx=5, pady=5)
        self.contact_entry = tk.Entry(self.venue_tab)
        self.contact_entry.grid(row=3, column=1, padx=5, pady=5)

        lbl_min_guests = tk.Label(self.venue_tab, text="Min Guests:")
        lbl_min_guests.grid(row=4, column=0, padx=5, pady=5)
        self.min_guests_entry = tk.Entry(self.venue_tab)
        self.min_guests_entry.grid(row=4, column=1, padx=5, pady=5)

        lbl_max_guests = tk.Label(self.venue_tab, text="Max Guests:")
        lbl_max_guests.grid(row=5, column=0, padx=5, pady=5)
        self.max_guests_entry = tk.Entry(self.venue_tab)
        self.max_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        btn_add = tk.Button(self.venue_tab, text="Add Venue", command=self.add_venue)
        btn_add.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        btn_update = tk.Button(self.venue_tab, text="Update Venue", command=self.update_venue)
        btn_update.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        btn_delete = tk.Button(self.venue_tab, text="Delete Venue", command=self.delete_venue)
        btn_delete.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        btn_display = tk.Button(self.venue_tab, text="Display Details", command=self.display_venue_details)
        btn_display.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    def add_venue(self):
        venue_id = self.venue_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        venue = Venue(venue_id, name, address, contact_details, min_guests, max_guests)
        messagebox.showinfo("Add Venue", f"Venue Added:\n\n{venue.__dict__}")

    def update_venue(self):
        venue_id = self.venue_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        venue = Venue(venue_id, name, address, contact_details, min_guests, max_guests)
        messagebox.showinfo("Update Venue", f"Venue Updated:\n\n{venue.__dict__}")

    def delete_venue(self):
        venue_id = self.venue_id_entry.get()
        messagebox.showinfo("Delete Venue", f"Venue Deleted with ID: {venue_id}")

    def display_venue_details(self):
        venue_id = self.venue_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()

        venue = Venue(venue_id, name, address, contact_details, min_guests, max_guests)
        messagebox.showinfo("Add Venue", f"Venue Added:\n\nID: {venue_id}\nName: {name}\nAddress: {address}\nContact Details: {contact_details}\nMinimum Guests: {min_guests}\nMaximum Guests: {max_guests}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = GUI()
    gui.run()
