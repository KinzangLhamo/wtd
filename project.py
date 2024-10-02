import tkinter as tk
from tkinter import messagebox
import sqlite3

# Initialize global variables
root = tk.Tk()
inventory_data = {
    "M.s Pipe": 10.99,
    "Electrode": 12.49,
    "Grinding Machine": 8.75,
    "Welding Machine": 15.00,
    "Try Square": 5.50,
    "Thread": 2.25,
    "Power Saw": 75.00,
    "Sand Paper": 1.50,
    "Measuring Tape": 6.00,
    "Welding Machine (BEME)": 15.00,
    "Oxy-Acetylene Sets": 50.00,
    "Power Saw (BEME)": 75.00,
    "Drilling Machine": 45.00,
    "Hand Drilling Machine": 25.00,
    "Grinding Machine (BEME)": 8.75,
    "Monitor": 120.00,
    "Projector": 300.00,
    "Marker Pen": 1.00,
    "Extension Code": 20.00,
}  # Sample inventory data with prices
history = []
is_admin = False


# Clear the frame function
def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()


# Admin Login Page
def admin_login_page():
    clear_frame()
    history.append(admin_login_page)
    tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

    tk.Label(root, text="Email").pack()
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    def login():
        global is_admin
        if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
            is_admin = True  # Set as admin
            inventory_status_page()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)


# User Login Page
def user_login_page():
    clear_frame()
    history.append(user_login_page)
    tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    def login():
        global is_admin
        if username_entry.get() and password_entry.get():  # Simple check, modify as needed
            is_admin = False  # Set as user
            user_view_inventory()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)


# User View - Inventory Viewing Only
def user_view_inventory():
    clear_frame()
    history.append(user_view_inventory)
    tk.Label(root, text="Inventory List", font=('Helvetica', 18, 'bold')).pack(pady=20)

    for item, price in inventory_data.items():
        tk.Label(root, text=f"{item}: ${price:.2f}").pack(pady=5)

    tk.Button(root, text="Report", command=report_page).pack(pady=20)
    tk.Button(root, text="Back", command=get_started_page).pack(pady=20)  # Go back to start page


# Inventory Status Page (Admin)
def inventory_status_page():
    clear_frame()
    history.append(inventory_status_page)
    tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

    tk.Button(root, text="Department", command=department_list_page).pack(pady=5)
    tk.Button(root, text="Price", command=show_price_details).pack(pady=5)


    tk.Button(root, text="Status Management", command=status_management_page).pack(pady=5)
    tk.Button(root, text="Interface", command=interface_page).pack(pady=5)
    tk.Button(root, text="Report", command=report_page).pack(pady=5)

    tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(
        pady=20)  # Back button added


# Show Price Details
def show_price_details():
    clear_frame()
    tk.Label(root, text="Price Details", font=('Helvetica', 18, 'bold')).pack(pady=20)

    for item, price in inventory_data.items():
        tk.Label(root, text=f"{item}: ${price:.2f}").pack(pady=5)

    tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)


# Department List Page
def department_list_page():
    clear_frame()
    history.append(department_list_page)
    tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

    departments = ["BEPE", "BEME", "CSN"]
    for dept in departments:
        tk.Button(root, text=dept, command=lambda d=dept: lrc_options_page(d)).pack(
            pady=10)  # Direct access to LRC options

    tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)  # Back button added


# LRC Options Page
def lrc_options_page(department):
    clear_frame()
    history.append(lrc_options_page)
    tk.Label(root, text=f"LRC Options for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

    if department == "BEPE":
        items = [
            "1. M.s Pipe",
            "2. Electrode",
            "3. Grinding Machine",
            "4. Welding Machine",
            "5. Try Square",
            "6. Thread",
            "7. Power Saw",
            "8. Sand Paper",
            "9. Measuring Tape"
        ]
    elif department == "BEME":
        items = [
            "1. Welding Machine",
            "2. Oxy-Acetylene Sets",
            "3. Power Saw",
            "4. Drilling Machine",
            "5. Hand Drilling Machine",
            "6. Grinding Machine"
        ]
    else:  # CSN
        items = [
            "1. Monitor",
            "2. Projector",
            "3. Marker Pen",
            "4. Extension Code"
        ]

    for item in items:
        tk.Label(root, text=item).pack(pady=5)

    tk.Button(root, text="Back", command=department_list_page).pack(pady=20)


# Start with Admin/User Login Options
def get_started_page():
    clear_frame()
    tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
    tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(
        pady=20)
    tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(
        pady=20)


# Call the get started page to initiate
get_started_page()
root.mainloop()
