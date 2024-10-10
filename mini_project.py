# # # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # # from tkinter import messagebox
# # # # # # # # # # # # # import sqlite3

# # # # # # # # # # # # # # Initialize global variables
# # # # # # # # # # # # # root = tk.Tk()
# # # # # # # # # # # # # inventory_data = {}  # This will be populated from the database
# # # # # # # # # # # # # history = []
# # # # # # # # # # # # # is_admin = False

# # # # # # # # # # # # # # Initialize the SQLite database
# # # # # # # # # # # # # def init_db():
# # # # # # # # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # # # # # # # #     cursor = conn.cursor()
    
# # # # # # # # # # # # #     # Create Inventory Table
# # # # # # # # # # # # #     cursor.execute('''
# # # # # # # # # # # # #     CREATE TABLE IF NOT EXISTS inventory (
# # # # # # # # # # # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # # # # # # # # # # #         item_name TEXT NOT NULL,
# # # # # # # # # # # # #         price REAL NOT NULL
# # # # # # # # # # # # #     )
# # # # # # # # # # # # #     ''')
    
# # # # # # # # # # # # #     # Insert sample inventory data if the table is empty
# # # # # # # # # # # # #     cursor.execute("SELECT COUNT(*) FROM inventory")
# # # # # # # # # # # # #     if cursor.fetchone()[0] == 0:  # If table is empty
# # # # # # # # # # # # #         sample_data = [
# # # # # # # # # # # # #             ("M.s Pipe", 10.99),
# # # # # # # # # # # # #             ("Electrode", 12.49),
# # # # # # # # # # # # #             ("Grinding Machine", 8.75),
# # # # # # # # # # # # #             ("Welding Machine", 15.00),
# # # # # # # # # # # # #             ("Try Square", 5.50),
# # # # # # # # # # # # #             ("Thread", 2.25),
# # # # # # # # # # # # #             ("Power Saw", 75.00),
# # # # # # # # # # # # #             ("Sand Paper", 1.50),
# # # # # # # # # # # # #             ("Measuring Tape", 6.00),
# # # # # # # # # # # # #             ("Welding Machine (BEME)", 15.00),
# # # # # # # # # # # # #             ("Oxy-Acetylene Sets", 50.00),
# # # # # # # # # # # # #             ("Power Saw (BEME)", 75.00),
# # # # # # # # # # # # #             ("Drilling Machine", 45.00),
# # # # # # # # # # # # #             ("Hand Drilling Machine", 25.00),
# # # # # # # # # # # # #             ("Grinding Machine (BEME)", 8.75),
# # # # # # # # # # # # #             ("Monitor", 120.00),
# # # # # # # # # # # # #             ("Projector", 300.00),
# # # # # # # # # # # # #             ("Marker Pen", 1.00),
# # # # # # # # # # # # #             ("Extension Code", 20.00)
# # # # # # # # # # # # #         ]
# # # # # # # # # # # # #         cursor.executemany("INSERT INTO inventory (item_name, price) VALUES (?, ?)", sample_data)

# # # # # # # # # # # # #     conn.commit()
# # # # # # # # # # # # #     conn.close()

# # # # # # # # # # # # # # Load inventory data from the database
# # # # # # # # # # # # # def load_inventory_data():
# # # # # # # # # # # # #     global inventory_data
# # # # # # # # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # # # # # # # #     cursor = conn.cursor()
    
# # # # # # # # # # # # #     cursor.execute("SELECT item_name, price FROM inventory")
# # # # # # # # # # # # #     inventory_data = {item[0]: item[1] for item in cursor.fetchall()}
# # # # # # # # # # # # #     conn.close()

# # # # # # # # # # # # # # Clear the frame function
# # # # # # # # # # # # # def clear_frame():
# # # # # # # # # # # # #     for widget in root.winfo_children():
# # # # # # # # # # # # #         widget.destroy()

# # # # # # # # # # # # # # Admin Login Page
# # # # # # # # # # # # # def admin_login_page():
# # # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # # #     history.append(admin_login_page)
# # # # # # # # # # # # #     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # # # # # # # #     tk.Label(root, text="Email").pack()
# # # # # # # # # # # # #     email_entry = tk.Entry(root)
# # # # # # # # # # # # #     email_entry.pack(pady=5)

# # # # # # # # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # # # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # # # # # # # #     password_entry.pack(pady=5)

# # # # # # # # # # # # #     def login():
# # # # # # # # # # # # #         global is_admin
# # # # # # # # # # # # #         if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
# # # # # # # # # # # # #             is_admin = True  # Set as admin
# # # # # # # # # # # # #             inventory_status_page()
# # # # # # # # # # # # #         else:
# # # # # # # # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # # # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)


# # # # # # # # # # # # # # User Login Page
# # # # # # # # # # # # # def user_login_page():
# # # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # # #     history.append(user_login_page)
# # # # # # # # # # # # #     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # # # # # # # #     tk.Label(root, text="Username").pack()
# # # # # # # # # # # # #     username_entry = tk.Entry(root)
# # # # # # # # # # # # #     username_entry.pack(pady=5)

# # # # # # # # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # # # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # # # # # # # #     password_entry.pack(pady=5)

# # # # # # # # # # # # #     def login():
# # # # # # # # # # # # #         global is_admin
# # # # # # # # # # # # #         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
# # # # # # # # # # # # #             is_admin = False  # Set as user
# # # # # # # # # # # # #             user_view_department()
# # # # # # # # # # # # #         else:
# # # # # # # # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # # # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)


# # # # # # # # # # # # # # User View - Departments Only
# # # # # # # # # # # # # def user_view_department():
# # # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # # #     history.append(user_view_department)
# # # # # # # # # # # # #     tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # # # # # # # #     for dept in departments:
# # # # # # # # # # # # #         tk.Button(root, text=dept, command=lambda d=dept: user_view_price(d)).pack(pady=10)

# # # # # # # # # # # # #     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)


# # # # # # # # # # # # # # User View Prices based on Department
# # # # # # # # # # # # # def user_view_price(department):
# # # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # # #     history.append(user_view_price)

# # # # # # # # # # # # #     tk.Label(root, text=f"Inventory Price List for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # # #     if department == "BEPE":
# # # # # # # # # # # # #         items = [
# # # # # # # # # # # # #             "1. M.s Pipe: $10.99",
# # # # # # # # # # # # #             "2. Electrode: $12.49",
# # # # # # # # # # # # #             "3. Grinding Machine: $8.75",
# # # # # # # # # # # # #             "4. Welding Machine: $15.00",
# # # # # # # # # # # # #             "5. Try Square: $5.50",
# # # # # # # # # # # # #             "6. Thread: $2.25",
# # # # # # # # # # # # #             "7. Power Saw: $75.00",
# # # # # # # # # # # # #             "8. Sand Paper: $1.50",
# # # # # # # # # # # # #             "9. Measuring Tape: $6.00"
# # # # # # # # # # # # #         ]
# # # # # # # # # # # # #     elif department == "BEME":
# # # # # # # # # # # # #         items = [
# # # # # # # # # # # # #             "1. Welding Machine: $15.00",
# # # # # # # # # # # # #             "2. Oxy-Acetylene Sets: $50.00",
# # # # # # # # # # # # #             "3. Power Saw: $75.00",
# # # # # # # # # # # # #             "4. Drilling Machine: $45.00",
# # # # # # # # # # # # #             "5. Hand Drilling Machine: $25.00",
# # # # # # # # # # # # #             "6. Grinding Machine: $8.75"
# # # # # # # # # # # # #         ]
# # # # # # # # # # # # #     else:  # CSN
# # # # # # # # # # # # #         items = [
# # # # # # # # # # # # #             "1. Monitor: $120.00",
# # # # # # # # # # # # #             "2. Projector: $300.00",
# # # # # # # # # # # # #             "3. Marker Pen: $1.00",
# # # # # # # # # # # # #             "4. Extension Code: $20.00"
# # # # # # # # # # # # #         ]

# # # # # # # # # # # # #     for item in items:
# # # # # # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # # # # # #     tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)
    
# # # # # # # # # # # # #     # Adding Price Button for the inventory
# # # # # # # # # # # # #     tk.Button(root, text="Show Price List", command=lambda: show_price_details(department)).pack(pady=5)


# # # # # # # # # # # # # # Show Price Details function
# # # # # # # # # # # # # def show_price_details(department):
# # # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # # #     tk.Label(root, text=f"Price Details for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # # #     if department == "BEPE":
# # # # # # # # # # # # #         items = [
# # # # # # # # # # # # #             "1. M.s Pipe: $10.99",
# # # # # # # # # # # # #             "2. Electrode: $12.49",
# # # # # # # # # # # # #             "3. Grinding Machine: $8.75",
# # # # # # # # # # # # #             "4. Welding Machine: $15.00",
# # # # # # # # # # # # #             "5. Try Square: $5.50",
# # # # # # # # # # # # #             "6. Thread: $2.25",
# # # # # # # # # # # # #             "7. Power Saw: $75.00",
# # # # # # # # # # # # #             "8. Sand Paper: $1.50",
# # # # # # # # # # # # #             "9. Measuring Tape: $6.00"
# # # # # # # # # # # # #         ]
# # # # # # # # # # # # #     elif department == "BEME":
# # # # # # # # # # # # #         items = [
# # # # # # # # # # # # #             "1. Welding Machine: $15.00",
# # # # # # # # # # # # #             "2. Oxy-Acetylene Sets: $50.00",
# # # # # # # # # # # # #             "3. Power Saw: $75.00",
# # # # # # # # # # # # #             "4. Drilling Machine: $45.00",
# # # # # # # # # # # # #             "5. Hand Drilling Machine: $25.00",
# # # # # # # # # # # # #             "6. Grinding Machine: $8.75"
# # # # # # # # # # # # #         ]
# # # # # # # # # # # # #     else:  # CSN
# # # # # # # # # # # # #         items = [
# # # # # # # # # # # # #             "1. Monitor: $120.00",
# # # # # # # # # # # # #             "2. Projector: $300.00",
# # # # # # # # # # # # #             "3. Marker Pen: $1.00",
# # # # # # # # # # # # #             "4. Extension Code: $20.00"
# # # # # # # # # # # # #         ]

# # # # # # # # # # # # #     for item in items:
# # # # # # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # # # # # #     tk.Button(root, text="Back to Prices", command=lambda: user_view_price(department)).pack(pady=20)


# # # # # # # # # # # # # # Inventory Status Page (Admin)
# # # # # # # # # # # # # def inventory_status_page():
# # # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # # #     history.append(inventory_status_page)
# # # # # # # # # # # # #     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # # #     tk.Button(root, text="Department", command=department_list_page).pack(pady=5)
# # # # # # # # # # # # #     tk.Button(root, text="Price", command=show_price_details).pack(pady=5)
# # # # # # # # # # # # #     tk.Button(root, text="Update", command=update_inventory_page).pack(pady=5)  # Update button added
# # # # # # # # # # # # #     tk.Button(root, text="Report", command=report_page).pack(pady=5)
# # # # # # # # # # # # #     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)  # Back button added


# # # # # # # # # # # # # # Update Inventory Page (Admin)
# # # # # # # # # # # # # def update_inventory_page():
# # # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # # #     history.append(update_inventory_page)
# # # # # # # # # # # # #     tk.Label(root, text="Update Inventory", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # # #     item_name_label = tk.Label(root, text="Item Name")
# # # # # # # # # # # # #     item_name_label.pack(pady=5)
# # # # # # # # # # # # #     item_name_entry = tk.Entry(root)
# # # # # # # # # # # # #     item_name_entry.pack(pady=5)

# # # # # # # # # # # # #     price_label = tk.Label(root, text="New Price")
# # # # # # # # # # # # #     price_label.pack(pady=5)
# # # # # # # # # # # # #     price_entry = tk.Entry(root)
# # # # # # # # # # # # #     price_entry.pack(pady=5)

# # # # # # # # # # # # #     def update_item():
# # # # # # # # # # # # #         item_name = item_name_entry.get()
# # # # # # # # # # # # #         new_price = price_entry.get()

# # # # # # # # # # # # #         if item_name in inventory_data and new_price.replace('.', '', 1).isdigit():
# # # # # # # # # # # # #             new_price = float(new_price)
# # # # # # # # # # # # #             conn = sqlite3.connect('inventory.db')
# # # # # # # # # # # # #             cursor = conn.cursor()
# # # # # # # # # # # # #             cursor.execute("UPDATE inventory SET price = ? WHERE item_name = ?", (new_price, item_name))
# # # # # # # # # # # # #             conn.commit()
# # # # # # # # # # # # #             conn.close()
# # # # # # # # # # # # #             messagebox.showinfo("Success", f"Updated {item_name} to ${new_price:.2f}")
# # # # # # # # # # # # #             load_inventory_data()  # Reload inventory data
# # # # # # # # # # # # #         else:
# # # # # # # # # # # # #             messagebox.showerror("Error", "Invalid item name or price.")

# # # # # # # # # # # # #     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
# # # # # # # # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)


# # # # # # # # # # # # # # Department List Page (Admin)
# # # # # # # # # # # # # def department_list_page():
# # # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # # #     history.append(department_list_page)
# # # # # # # # # # # # #     tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # # # # # # # #     for dept in departments:
# # # # # # # # # # # # #         tk.Button(root, text=dept, command=lambda d=dept: raw_materials_options_page(d)).pack(pady=10)

# # # # # # # # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)  # Back button added


# # # # # # # # # # # # # # Raw Materials Options Page
# # # # # # # # # # # # # def raw_materials_options_page(department):
# # # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # # #     history.append(raw_materials_options_page)
# # # # # # # # # # # # #     tk.Label(root, text=f"Raw Materials for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # # #     if department == "BEPE":
# # # # # # # # # # # # #         items = [
# # # # # # # # # # # # #             "1. M.s Pipe",
# # # # # # # # # # # # #             "2. Electrode",
# # # # # # # # # # # # #             "3. Grinding Machine",
# # # # # # # # # # # # #             "4. Welding Machine",
# # # # # # # # # # # # #             "5. Try Square",
# # # # # # # # # # # # #             "6. Thread",
# # # # # # # # # # # # #             "7. Power Saw",
# # # # # # # # # # # # #             "8. Sand Paper",
# # # # # # # # # # # # #             "9. Measuring Tape"
# # # # # # # # # # # # #         ]
# # # # # # # # # # # # #     elif department == "BEME":
# # # # # # # # # # # # #         items = [
# # # # # # # # # # # # #             "1. Welding Machine",
# # # # # # # # # # # # #             "2. Oxy-Acetylene Sets",
# # # # # # # # # # # # #             "3. Power Saw",
# # # # # # # # # # # # #             "4. Drilling Machine",
# # # # # # # # # # # # #             "5. Hand Drilling Machine",
# # # # # # # # # # # # #             "6. Grinding Machine"
# # # # # # # # # # # # #         ]
# # # # # # # # # # # # #     else:  # CSN
# # # # # # # # # # # # #         items = [
# # # # # # # # # # # # #             "1. Monitor",
# # # # # # # # # # # # #             "2. Projector",
# # # # # # # # # # # # #             "3. Marker Pen",
# # # # # # # # # # # # #             "4. Extension Code"
# # # # # # # # # # # # #         ]

# # # # # # # # # # # # #     for item in items:
# # # # # # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # # # # # #     tk.Button(root, text="Back", command=department_list_page).pack(pady=20)


# # # # # # # # # # # # # # Start with Admin/User Login Options
# # # # # # # # # # # # # def get_started_page():
# # # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # # #     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
# # # # # # # # # # # # #     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
# # # # # # # # # # # # #     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)


# # # # # # # # # # # # # # Call the init_db to create the database and load data
# # # # # # # # # # # # # init_db()
# # # # # # # # # # # # # load_inventory_data()

# # # # # # # # # # # # # # Call the get started page to initiate
# # # # # # # # # # # # # get_started_page()
# # # # # # # # # # # # # root.mainloop()

# # # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # # from tkinter import messagebox
# # # # # # # # # # # # import sqlite3

# # # # # # # # # # # # # Initialize global variables
# # # # # # # # # # # # root = tk.Tk()
# # # # # # # # # # # # inventory_data = {}  # This will be populated from the database
# # # # # # # # # # # # history = []
# # # # # # # # # # # # is_admin = False

# # # # # # # # # # # # # Initialize the SQLite database
# # # # # # # # # # # # def init_db():
# # # # # # # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # # # # # # #     cursor = conn.cursor()

# # # # # # # # # # # #     # Create Inventory Table
# # # # # # # # # # # #     cursor.execute('''
# # # # # # # # # # # #     CREATE TABLE IF NOT EXISTS inventory (
# # # # # # # # # # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # # # # # # # # # #         item_name TEXT NOT NULL,
# # # # # # # # # # # #         price REAL NOT NULL
# # # # # # # # # # # #     )
# # # # # # # # # # # #     ''')

# # # # # # # # # # # #     # Insert sample inventory data if the table is empty
# # # # # # # # # # # #     cursor.execute("SELECT COUNT(*) FROM inventory")
# # # # # # # # # # # #     if cursor.fetchone()[0] == 0:  # If table is empty
# # # # # # # # # # # #         sample_data = [
# # # # # # # # # # # #             ("M.s Pipe", 10.99),
# # # # # # # # # # # #             ("Electrode", 12.49),
# # # # # # # # # # # #             ("Grinding Machine", 8.75),
# # # # # # # # # # # #             ("Welding Machine", 15.00),
# # # # # # # # # # # #             ("Try Square", 5.50),
# # # # # # # # # # # #             ("Thread", 2.25),
# # # # # # # # # # # #             ("Power Saw", 75.00),
# # # # # # # # # # # #             ("Sand Paper", 1.50),
# # # # # # # # # # # #             ("Measuring Tape", 6.00),
# # # # # # # # # # # #             ("Welding Machine (BEME)", 15.00),
# # # # # # # # # # # #             ("Oxy-Acetylene Sets", 50.00),
# # # # # # # # # # # #             ("Power Saw (BEME)", 75.00),
# # # # # # # # # # # #             ("Drilling Machine", 45.00),
# # # # # # # # # # # #             ("Hand Drilling Machine", 25.00),
# # # # # # # # # # # #             ("Grinding Machine (BEME)", 8.75),
# # # # # # # # # # # #             ("Monitor", 120.00),
# # # # # # # # # # # #             ("Projector", 300.00),
# # # # # # # # # # # #             ("Marker Pen", 1.00),
# # # # # # # # # # # #             ("Extension Code", 20.00)
# # # # # # # # # # # #         ]
# # # # # # # # # # # #         cursor.executemany("INSERT INTO inventory (item_name, price) VALUES (?, ?)", sample_data)

# # # # # # # # # # # #     conn.commit()
# # # # # # # # # # # #     conn.close()

# # # # # # # # # # # # # Load inventory data from the database
# # # # # # # # # # # # def load_inventory_data():
# # # # # # # # # # # #     global inventory_data
# # # # # # # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # # # # # # #     cursor = conn.cursor()

# # # # # # # # # # # #     cursor.execute("SELECT item_name, price FROM inventory")
# # # # # # # # # # # #     inventory_data = {item[0]: item[1] for item in cursor.fetchall()}
# # # # # # # # # # # #     conn.close()

# # # # # # # # # # # # # Clear the frame function
# # # # # # # # # # # # def clear_frame():
# # # # # # # # # # # #     for widget in root.winfo_children():
# # # # # # # # # # # #         widget.destroy()

# # # # # # # # # # # # # Admin Login Page
# # # # # # # # # # # # def admin_login_page():
# # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # #     history.append(admin_login_page)
# # # # # # # # # # # #     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # # # # # # #     tk.Label(root, text="Email").pack()
# # # # # # # # # # # #     email_entry = tk.Entry(root)
# # # # # # # # # # # #     email_entry.pack(pady=5)

# # # # # # # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # # # # # # #     password_entry.pack(pady=5)

# # # # # # # # # # # #     def login():
# # # # # # # # # # # #         global is_admin
# # # # # # # # # # # #         if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
# # # # # # # # # # # #             is_admin = True  # Set as admin
# # # # # # # # # # # #             inventory_status_page()
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # # # # # # # User Login Page
# # # # # # # # # # # # def user_login_page():
# # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # #     history.append(user_login_page)
# # # # # # # # # # # #     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # # # # # # #     tk.Label(root, text="Username").pack()
# # # # # # # # # # # #     username_entry = tk.Entry(root)
# # # # # # # # # # # #     username_entry.pack(pady=5)

# # # # # # # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # # # # # # #     password_entry.pack(pady=5)

# # # # # # # # # # # #     def login():
# # # # # # # # # # # #         global is_admin
# # # # # # # # # # # #         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
# # # # # # # # # # # #             is_admin = False  # Set as user
# # # # # # # # # # # #             user_view_department()
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # # # # # # # User View - Departments Only
# # # # # # # # # # # # def user_view_department():
# # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # #     history.append(user_view_department)
# # # # # # # # # # # #     tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # # # # # # #     for dept in departments:
# # # # # # # # # # # #         tk.Button(root, text=dept, command=lambda d=dept: user_view_price(d)).pack(pady=10)

# # # # # # # # # # # #     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# # # # # # # # # # # # # User View Prices based on Department
# # # # # # # # # # # # def user_view_price(department):
# # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # #     history.append(user_view_price)

# # # # # # # # # # # #     tk.Label(root, text=f"Inventory Price List for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # #     items = []
# # # # # # # # # # # #     if department == "BEPE":
# # # # # # # # # # # #         items = [
# # # # # # # # # # # #             "1. M.s Pipe: $10.99",
# # # # # # # # # # # #             "2. Electrode: $12.49",
# # # # # # # # # # # #             "3. Grinding Machine: $8.75",
# # # # # # # # # # # #             "4. Welding Machine: $15.00",
# # # # # # # # # # # #             "5. Try Square: $5.50",
# # # # # # # # # # # #             "6. Thread: $2.25",
# # # # # # # # # # # #             "7. Power Saw: $75.00",
# # # # # # # # # # # #             "8. Sand Paper: $1.50",
# # # # # # # # # # # #             "9. Measuring Tape: $6.00"
# # # # # # # # # # # #         ]
# # # # # # # # # # # #     elif department == "BEME":
# # # # # # # # # # # #         items = [
# # # # # # # # # # # #             "1. Welding Machine: $15.00",
# # # # # # # # # # # #             "2. Oxy-Acetylene Sets: $50.00",
# # # # # # # # # # # #             "3. Power Saw: $75.00",
# # # # # # # # # # # #             "4. Drilling Machine: $45.00",
# # # # # # # # # # # #             "5. Hand Drilling Machine: $25.00",
# # # # # # # # # # # #             "6. Grinding Machine: $8.75"
# # # # # # # # # # # #         ]
# # # # # # # # # # # #     else:  # CSN
# # # # # # # # # # # #         items = [
# # # # # # # # # # # #             "1. Monitor: $120.00",
# # # # # # # # # # # #             "2. Projector: $300.00",
# # # # # # # # # # # #             "3. Marker Pen: $1.00",
# # # # # # # # # # # #             "4. Extension Code: $20.00"
# # # # # # # # # # # #         ]

# # # # # # # # # # # #     for item in items:
# # # # # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # # # # #     tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)
    
# # # # # # # # # # # #     # Adding Price Button for the inventory
# # # # # # # # # # # #     tk.Button(root, text="Show Price List", command=lambda: show_price_details(department)).pack(pady=5)

# # # # # # # # # # # # # Show Price Details function
# # # # # # # # # # # # def show_price_details(department):
# # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # #     tk.Label(root, text=f"Price Details for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # #     if department == "BEPE":
# # # # # # # # # # # #         items = [
# # # # # # # # # # # #             "1. M.s Pipe: $10.99",
# # # # # # # # # # # #             "2. Electrode: $12.49",
# # # # # # # # # # # #             "3. Grinding Machine: $8.75",
# # # # # # # # # # # #             "4. Welding Machine: $15.00",
# # # # # # # # # # # #             "5. Try Square: $5.50",
# # # # # # # # # # # #             "6. Thread: $2.25",
# # # # # # # # # # # #             "7. Power Saw: $75.00",
# # # # # # # # # # # #             "8. Sand Paper: $1.50",
# # # # # # # # # # # #             "9. Measuring Tape: $6.00"
# # # # # # # # # # # #         ]
# # # # # # # # # # # #     elif department == "BEME":
# # # # # # # # # # # #         items = [
# # # # # # # # # # # #             "1. Welding Machine: $15.00",
# # # # # # # # # # # #             "2. Oxy-Acetylene Sets: $50.00",
# # # # # # # # # # # #             "3. Power Saw: $75.00",
# # # # # # # # # # # #             "4. Drilling Machine: $45.00",
# # # # # # # # # # # #             "5. Hand Drilling Machine: $25.00",
# # # # # # # # # # # #             "6. Grinding Machine: $8.75"
# # # # # # # # # # # #         ]
# # # # # # # # # # # #     else:  # CSN
# # # # # # # # # # # #         items = [
# # # # # # # # # # # #             "1. Monitor: $120.00",
# # # # # # # # # # # #             "2. Projector: $300.00",
# # # # # # # # # # # #             "3. Marker Pen: $1.00",
# # # # # # # # # # # #             "4. Extension Code: $20.00"
# # # # # # # # # # # #         ]

# # # # # # # # # # # #     for item in items:
# # # # # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # # # # #     tk.Button(root, text="Back to Prices", command=lambda: user_view_price(department)).pack(pady=20)

# # # # # # # # # # # # # Inventory Status Page (Admin)
# # # # # # # # # # # # def inventory_status_page():
# # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # #     history.append(inventory_status_page)
# # # # # # # # # # # #     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # #     tk.Button(root, text="Department", command=department_list_page).pack(pady=5)
# # # # # # # # # # # #     tk.Button(root, text="Price", command=lambda: show_price_details("BEPE")).pack(pady=5)  # Specify a default department
# # # # # # # # # # # #     tk.Button(root, text="Update", command=update_inventory_page).pack(pady=5)  # Update button
# # # # # # # # # # # #     tk.Button(root, text="Report", command=report_page).pack(pady=5)
# # # # # # # # # # # #     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# # # # # # # # # # # # # Update Inventory Page (Admin)
# # # # # # # # # # # # def update_inventory_page():
# # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # #     history.append(update_inventory_page)
# # # # # # # # # # # #     tk.Label(root, text="Update Inventory", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # #     item_name_label = tk.Label(root, text="Item Name")
# # # # # # # # # # # #     item_name_label.pack(pady=5)
# # # # # # # # # # # #     item_name_entry = tk.Entry(root)
# # # # # # # # # # # #     item_name_entry.pack(pady=5)

# # # # # # # # # # # #     price_label = tk.Label(root, text="New Price")
# # # # # # # # # # # #     price_label.pack(pady=5)
# # # # # # # # # # # #     price_entry = tk.Entry(root)
# # # # # # # # # # # #     price_entry.pack(pady=5)

# # # # # # # # # # # #     def update_item():
# # # # # # # # # # # #         item_name = item_name_entry.get()
# # # # # # # # # # # #         new_price = price_entry.get()

# # # # # # # # # # # #         if item_name in inventory_data and new_price.replace('.', '', 1).isdigit():
# # # # # # # # # # # #             new_price = float(new_price)
# # # # # # # # # # # #             conn = sqlite3.connect('inventory.db')
# # # # # # # # # # # #             cursor = conn.cursor()
# # # # # # # # # # # #             cursor.execute("UPDATE inventory SET price = ? WHERE item_name = ?", (new_price, item_name))
# # # # # # # # # # # #             conn.commit()
# # # # # # # # # # # #             conn.close()
# # # # # # # # # # # #             messagebox.showinfo("Success", f"Updated {item_name} to ${new_price:.2f}")
# # # # # # # # # # # #             load_inventory_data()  # Reload inventory data
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             messagebox.showerror("Error", "Invalid item name or price.")

# # # # # # # # # # # #     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
# # # # # # # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # # # # # # # # # # Department List Page (Admin)
# # # # # # # # # # # # def department_list_page():
# # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # #     history.append(department_list_page)
# # # # # # # # # # # #     tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # # # # # # #     for dept in departments:
# # # # # # # # # # # #         tk.Button(root, text=dept, command=lambda d=dept: raw_materials_options_page(d)).pack(pady=10)

# # # # # # # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)  # Back button added

# # # # # # # # # # # # # Raw Materials Options Page
# # # # # # # # # # # # def raw_materials_options_page(department):
# # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # #     history.append(raw_materials_options_page)
# # # # # # # # # # # #     tk.Label(root, text=f"Raw Materials for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # # #     if department == "BEPE":
# # # # # # # # # # # #         items = [
# # # # # # # # # # # #             "1. M.s Pipe",
# # # # # # # # # # # #             "2. Electrode",
# # # # # # # # # # # #             "3. Grinding Machine",
# # # # # # # # # # # #             "4. Welding Machine",
# # # # # # # # # # # #             "5. Try Square",
# # # # # # # # # # # #             "6. Thread",
# # # # # # # # # # # #             "7. Power Saw",
# # # # # # # # # # # #             "8. Sand Paper",
# # # # # # # # # # # #             "9. Measuring Tape"
# # # # # # # # # # # #         ]
# # # # # # # # # # # #     elif department == "BEME":
# # # # # # # # # # # #         items = [
# # # # # # # # # # # #             "1. Welding Machine",
# # # # # # # # # # # #             "2. Oxy-Acetylene Sets",
# # # # # # # # # # # #             "3. Power Saw",
# # # # # # # # # # # #             "4. Drilling Machine",
# # # # # # # # # # # #             "5. Hand Drilling Machine",
# # # # # # # # # # # #             "6. Grinding Machine"
# # # # # # # # # # # #         ]
# # # # # # # # # # # #     else:  # CSN
# # # # # # # # # # # #         items = [
# # # # # # # # # # # #             "1. Monitor",
# # # # # # # # # # # #             "2. Projector",
# # # # # # # # # # # #             "3. Marker Pen",
# # # # # # # # # # # #             "4. Extension Code"
# # # # # # # # # # # #         ]

# # # # # # # # # # # #     for item in items:
# # # # # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # # # # #     tk.Button(root, text="Back", command=department_list_page).pack(pady=20)

# # # # # # # # # # # # # Start with Admin/User Login Options
# # # # # # # # # # # # def get_started_page():
# # # # # # # # # # # #     clear_frame()
# # # # # # # # # # # #     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
# # # # # # # # # # # #     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
# # # # # # # # # # # #     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# # # # # # # # # # # # # Call the init_db to create the database and load data
# # # # # # # # # # # # init_db()
# # # # # # # # # # # # load_inventory_data()

# # # # # # # # # # # # # Call the get started page to initiate
# # # # # # # # # # # # get_started_page()
# # # # # # # # # # # # root.mainloop()

# # # # # # # # # # # import tkinter as tk
# # # # # # # # # # # from tkinter import messagebox
# # # # # # # # # # # import sqlite3

# # # # # # # # # # # # Initialize global variables
# # # # # # # # # # # root = tk.Tk()
# # # # # # # # # # # inventory_data = {}  # This will be populated from the database
# # # # # # # # # # # history = []
# # # # # # # # # # # is_admin = False

# # # # # # # # # # # # Initialize the SQLite database
# # # # # # # # # # # def init_db():
# # # # # # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # # # # # #     cursor = conn.cursor()

# # # # # # # # # # #     # Create Inventory Table
# # # # # # # # # # #     cursor.execute('''
# # # # # # # # # # #     CREATE TABLE IF NOT EXISTS inventory (
# # # # # # # # # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # # # # # # # # #         item_name TEXT NOT NULL,
# # # # # # # # # # #         price REAL NOT NULL
# # # # # # # # # # #     )
# # # # # # # # # # #     ''')

# # # # # # # # # # #     # Insert sample inventory data if the table is empty
# # # # # # # # # # #     cursor.execute("SELECT COUNT(*) FROM inventory")
# # # # # # # # # # #     if cursor.fetchone()[0] == 0:  # If table is empty
# # # # # # # # # # #         sample_data = [
# # # # # # # # # # #             ("M.s Pipe", 10.99),
# # # # # # # # # # #             ("Electrode", 12.49),
# # # # # # # # # # #             ("Grinding Machine", 8.75),
# # # # # # # # # # #             ("Welding Machine", 15.00),
# # # # # # # # # # #             ("Try Square", 5.50),
# # # # # # # # # # #             ("Thread", 2.25),
# # # # # # # # # # #             ("Power Saw", 75.00),
# # # # # # # # # # #             ("Sand Paper", 1.50),
# # # # # # # # # # #             ("Measuring Tape", 6.00),
# # # # # # # # # # #             ("Welding Machine (BEME)", 15.00),
# # # # # # # # # # #             ("Oxy-Acetylene Sets", 50.00),
# # # # # # # # # # #             ("Power Saw (BEME)", 75.00),
# # # # # # # # # # #             ("Drilling Machine", 45.00),
# # # # # # # # # # #             ("Hand Drilling Machine", 25.00),
# # # # # # # # # # #             ("Grinding Machine (BEME)", 8.75),
# # # # # # # # # # #             ("Monitor", 120.00),
# # # # # # # # # # #             ("Projector", 300.00),
# # # # # # # # # # #             ("Marker Pen", 1.00),
# # # # # # # # # # #             ("Extension Code", 20.00)
# # # # # # # # # # #         ]
# # # # # # # # # # #         cursor.executemany("INSERT INTO inventory (item_name, price) VALUES (?, ?)", sample_data)

# # # # # # # # # # #     conn.commit()
# # # # # # # # # # #     conn.close()

# # # # # # # # # # # # Load inventory data from the database
# # # # # # # # # # # def load_inventory_data():
# # # # # # # # # # #     global inventory_data
# # # # # # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # # # # # #     cursor = conn.cursor()

# # # # # # # # # # #     cursor.execute("SELECT item_name, price FROM inventory")
# # # # # # # # # # #     inventory_data = {item[0]: item[1] for item in cursor.fetchall()}
# # # # # # # # # # #     conn.close()

# # # # # # # # # # # # Clear the frame function
# # # # # # # # # # # def clear_frame():
# # # # # # # # # # #     for widget in root.winfo_children():
# # # # # # # # # # #         widget.destroy()

# # # # # # # # # # # # Admin Login Page
# # # # # # # # # # # def admin_login_page():
# # # # # # # # # # #     clear_frame()
# # # # # # # # # # #     history.append(admin_login_page)
# # # # # # # # # # #     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # # # # # #     tk.Label(root, text="Email").pack()
# # # # # # # # # # #     email_entry = tk.Entry(root)
# # # # # # # # # # #     email_entry.pack(pady=5)

# # # # # # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # # # # # #     password_entry.pack(pady=5)

# # # # # # # # # # #     def login():
# # # # # # # # # # #         global is_admin
# # # # # # # # # # #         if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
# # # # # # # # # # #             is_admin = True  # Set as admin
# # # # # # # # # # #             inventory_status_page()
# # # # # # # # # # #         else:
# # # # # # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # # # # # # User Login Page
# # # # # # # # # # # def user_login_page():
# # # # # # # # # # #     clear_frame()
# # # # # # # # # # #     history.append(user_login_page)
# # # # # # # # # # #     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # # # # # #     tk.Label(root, text="Username").pack()
# # # # # # # # # # #     username_entry = tk.Entry(root)
# # # # # # # # # # #     username_entry.pack(pady=5)

# # # # # # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # # # # # #     password_entry.pack(pady=5)

# # # # # # # # # # #     def login():
# # # # # # # # # # #         global is_admin
# # # # # # # # # # #         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
# # # # # # # # # # #             is_admin = False  # Set as user
# # # # # # # # # # #             user_view_department()
# # # # # # # # # # #         else:
# # # # # # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # # # # # # User View - Departments Only
# # # # # # # # # # # def user_view_department():
# # # # # # # # # # #     clear_frame()
# # # # # # # # # # #     history.append(user_view_department)
# # # # # # # # # # #     tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # # # # # #     for dept in departments:
# # # # # # # # # # #         tk.Button(root, text=dept, command=lambda d=dept: user_view_price(d)).pack(pady=10)

# # # # # # # # # # #     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# # # # # # # # # # # # User View Prices based on Department
# # # # # # # # # # # def user_view_price(department):
# # # # # # # # # # #     clear_frame()
# # # # # # # # # # #     history.append(user_view_price)

# # # # # # # # # # #     tk.Label(root, text=f"Inventory Price List for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # #     items = []
# # # # # # # # # # #     if department == "BEPE":
# # # # # # # # # # #         items = [
# # # # # # # # # # #             "1. M.s Pipe: $10.99",
# # # # # # # # # # #             "2. Electrode: $12.49",
# # # # # # # # # # #             "3. Grinding Machine: $8.75",
# # # # # # # # # # #             "4. Welding Machine: $15.00",
# # # # # # # # # # #             "5. Try Square: $5.50",
# # # # # # # # # # #             "6. Thread: $2.25",
# # # # # # # # # # #             "7. Power Saw: $75.00",
# # # # # # # # # # #             "8. Sand Paper: $1.50",
# # # # # # # # # # #             "9. Measuring Tape: $6.00"
# # # # # # # # # # #         ]
# # # # # # # # # # #     elif department == "BEME":
# # # # # # # # # # #         items = [
# # # # # # # # # # #             "1. Welding Machine: $15.00",
# # # # # # # # # # #             "2. Oxy-Acetylene Sets: $50.00",
# # # # # # # # # # #             "3. Power Saw: $75.00",
# # # # # # # # # # #             "4. Drilling Machine: $45.00",
# # # # # # # # # # #             "5. Hand Drilling Machine: $25.00",
# # # # # # # # # # #             "6. Grinding Machine: $8.75"
# # # # # # # # # # #         ]
# # # # # # # # # # #     else:  # CSN
# # # # # # # # # # #         items = [
# # # # # # # # # # #             "1. Monitor: $120.00",
# # # # # # # # # # #             "2. Projector: $300.00",
# # # # # # # # # # #             "3. Marker Pen: $1.00",
# # # # # # # # # # #             "4. Extension Code: $20.00"
# # # # # # # # # # #         ]

# # # # # # # # # # #     for item in items:
# # # # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # # # #     tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)
    
# # # # # # # # # # #     # Adding Price Button for the inventory
# # # # # # # # # # #     tk.Button(root, text="Show Price List", command=lambda: show_price_details(department)).pack(pady=5)

# # # # # # # # # # # # Show Price Details function
# # # # # # # # # # # def show_price_details(department):
# # # # # # # # # # #     clear_frame()
# # # # # # # # # # #     tk.Label(root, text=f"Price Details for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # #     if department == "BEPE":
# # # # # # # # # # #         items = [
# # # # # # # # # # #             "1. M.s Pipe: $10.99",
# # # # # # # # # # #             "2. Electrode: $12.49",
# # # # # # # # # # #             "3. Grinding Machine: $8.75",
# # # # # # # # # # #             "4. Welding Machine: $15.00",
# # # # # # # # # # #             "5. Try Square: $5.50",
# # # # # # # # # # #             "6. Thread: $2.25",
# # # # # # # # # # #             "7. Power Saw: $75.00",
# # # # # # # # # # #             "8. Sand Paper: $1.50",
# # # # # # # # # # #             "9. Measuring Tape: $6.00"
# # # # # # # # # # #         ]
# # # # # # # # # # #     elif department == "BEME":
# # # # # # # # # # #         items = [
# # # # # # # # # # #             "1. Welding Machine: $15.00",
# # # # # # # # # # #             "2. Oxy-Acetylene Sets: $50.00",
# # # # # # # # # # #             "3. Power Saw: $75.00",
# # # # # # # # # # #             "4. Drilling Machine: $45.00",
# # # # # # # # # # #             "5. Hand Drilling Machine: $25.00",
# # # # # # # # # # #             "6. Grinding Machine: $8.75"
# # # # # # # # # # #         ]
# # # # # # # # # # #     else:  # CSN
# # # # # # # # # # #         items = [
# # # # # # # # # # #             "1. Monitor: $120.00",
# # # # # # # # # # #             "2. Projector: $300.00",
# # # # # # # # # # #             "3. Marker Pen: $1.00",
# # # # # # # # # # #             "4. Extension Code: $20.00"
# # # # # # # # # # #         ]

# # # # # # # # # # #     for item in items:
# # # # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # # # #     tk.Button(root, text="Back to Prices", command=lambda: user_view_price(department)).pack(pady=20)

# # # # # # # # # # # # Inventory Status Page (Admin)
# # # # # # # # # # # def inventory_status_page():
# # # # # # # # # # #     clear_frame()
# # # # # # # # # # #     history.append(inventory_status_page)
# # # # # # # # # # #     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # #     tk.Button(root, text="Department", command=department_list_page).pack(pady=5)
# # # # # # # # # # #     tk.Button(root, text="Price", command=lambda: show_price_details("BEPE")).pack(pady=5)  # Specify a default department
# # # # # # # # # # #     tk.Button(root, text="Update", command=update_inventory_page).pack(pady=5)  # Update button
# # # # # # # # # # #     tk.Button(root, text="Report", command=report_page).pack(pady=5)
# # # # # # # # # # #     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# # # # # # # # # # # # Update Inventory Page (Admin)
# # # # # # # # # # # def update_inventory_page():
# # # # # # # # # # #     clear_frame()
# # # # # # # # # # #     history.append(update_inventory_page)
# # # # # # # # # # #     tk.Label(root, text="Update Inventory", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # #     item_name_label = tk.Label(root, text="Item Name")
# # # # # # # # # # #     item_name_label.pack(pady=5)
# # # # # # # # # # #     item_name_entry = tk.Entry(root)
# # # # # # # # # # #     item_name_entry.pack(pady=5)

# # # # # # # # # # #     price_label = tk.Label(root, text="New Price")
# # # # # # # # # # #     price_label.pack(pady=5)
# # # # # # # # # # #     price_entry = tk.Entry(root)
# # # # # # # # # # #     price_entry.pack(pady=5)

# # # # # # # # # # #     def update_item():
# # # # # # # # # # #         item_name = item_name_entry.get().strip()
# # # # # # # # # # #         new_price = price_entry.get().strip()

# # # # # # # # # # #         # Check if item exists in a case-insensitive way
# # # # # # # # # # #         normalized_inventory = {k.lower(): v for k, v in inventory_data.items()}
# # # # # # # # # # #         item_key = item_name.lower()

# # # # # # # # # # #         if item_key in normalized_inventory and new_price.replace('.', '', 1).isdigit():
# # # # # # # # # # #             new_price = float(new_price)
# # # # # # # # # # #             conn = sqlite3.connect('inventory.db')
# # # # # # # # # # #             cursor = conn.cursor()
# # # # # # # # # # #             cursor.execute("UPDATE inventory SET price = ? WHERE item_name = ?", (new_price, item_name))
# # # # # # # # # # #             conn.commit()
# # # # # # # # # # #             conn.close()
# # # # # # # # # # #             messagebox.showinfo("Success", f"Updated '{item_name}' to ${new_price:.2f}")
# # # # # # # # # # #             load_inventory_data()  # Reload inventory data
# # # # # # # # # # #         else:
# # # # # # # # # # #             if item_key not in normalized_inventory:
# # # # # # # # # # #                 messagebox.showerror("Error", "Item name does not exist.")
# # # # # # # # # # #             else:
# # # # # # # # # # #                 messagebox.showerror("Error", "Invalid price. Please enter a valid numeric value.")

# # # # # # # # # # #     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
# # # # # # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # # # # # # # # # Department List Page (Admin)
# # # # # # # # # # # def department_list_page():
# # # # # # # # # # #     clear_frame()
# # # # # # # # # # #     history.append(department_list_page)
# # # # # # # # # # #     tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # # # # # #     for dept in departments:
# # # # # # # # # # #         tk.Button(root, text=dept, command=lambda d=dept: raw_materials_options_page(d)).pack(pady=10)

# # # # # # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)  # Back button added

# # # # # # # # # # # # Raw Materials Options Page
# # # # # # # # # # # def raw_materials_options_page(department):
# # # # # # # # # # #     clear_frame()
# # # # # # # # # # #     history.append(raw_materials_options_page)
# # # # # # # # # # #     tk.Label(root, text=f"Raw Materials for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # # #     if department == "BEPE":
# # # # # # # # # # #         items = [
# # # # # # # # # # #             "1. M.s Pipe",
# # # # # # # # # # #             "2. Electrode",
# # # # # # # # # # #             "3. Grinding Machine",
# # # # # # # # # # #             "4. Welding Machine",
# # # # # # # # # # #             "5. Try Square",
# # # # # # # # # # #             "6. Thread",
# # # # # # # # # # #             "7. Power Saw",
# # # # # # # # # # #             "8. Sand Paper",
# # # # # # # # # # #             "9. Measuring Tape"
# # # # # # # # # # #         ]
# # # # # # # # # # #     elif department == "BEME":
# # # # # # # # # # #         items = [
# # # # # # # # # # #             "1. Welding Machine",
# # # # # # # # # # #             "2. Oxy-Acetylene Sets",
# # # # # # # # # # #             "3. Power Saw",
# # # # # # # # # # #             "4. Drilling Machine",
# # # # # # # # # # #             "5. Hand Drilling Machine",
# # # # # # # # # # #             "6. Grinding Machine"
# # # # # # # # # # #         ]
# # # # # # # # # # #     else:  # CSN
# # # # # # # # # # #         items = [
# # # # # # # # # # #             "1. Monitor",
# # # # # # # # # # #             "2. Projector",
# # # # # # # # # # #             "3. Marker Pen",
# # # # # # # # # # #             "4. Extension Code"
# # # # # # # # # # #         ]

# # # # # # # # # # #     for item in items:
# # # # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # # # #     tk.Button(root, text="Back", command=department_list_page).pack(pady=20)

# # # # # # # # # # # # Start with Admin/User Login Options
# # # # # # # # # # # def get_started_page():
# # # # # # # # # # #     clear_frame()
# # # # # # # # # # #     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
# # # # # # # # # # #     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
# # # # # # # # # # #     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# # # # # # # # # # # # Call the init_db to create the database and load data
# # # # # # # # # # # init_db()
# # # # # # # # # # # load_inventory_data()

# # # # # # # # # # # # Call the get started page to initiate
# # # # # # # # # # # get_started_page()
# # # # # # # # # # # root.mainloop()

# # # # # # # # # # import tkinter as tk
# # # # # # # # # # from tkinter import messagebox
# # # # # # # # # # import sqlite3

# # # # # # # # # # # Initialize global variables
# # # # # # # # # # root = tk.Tk()
# # # # # # # # # # inventory_data = {}  # This will be populated from the database
# # # # # # # # # # history = []
# # # # # # # # # # is_admin = False

# # # # # # # # # # # Initialize the SQLite database
# # # # # # # # # # def init_db():
# # # # # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # # # # #     cursor = conn.cursor()

# # # # # # # # # #     # Create Inventory Table
# # # # # # # # # #     cursor.execute('''
# # # # # # # # # #     CREATE TABLE IF NOT EXISTS inventory (
# # # # # # # # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # # # # # # # #         item_name TEXT NOT NULL,
# # # # # # # # # #         price REAL NOT NULL
# # # # # # # # # #     )
# # # # # # # # # #     ''')

# # # # # # # # # #     # Insert sample inventory data if the table is empty
# # # # # # # # # #     cursor.execute("SELECT COUNT(*) FROM inventory")
# # # # # # # # # #     if cursor.fetchone()[0] == 0:  # If table is empty
# # # # # # # # # #         sample_data = [
# # # # # # # # # #             ("M.s Pipe", 10.99),
# # # # # # # # # #             ("Electrode", 12.49),
# # # # # # # # # #             ("Grinding Machine", 8.75),
# # # # # # # # # #             ("Welding Machine", 15.00),
# # # # # # # # # #             ("Try Square", 5.50),
# # # # # # # # # #             ("Thread", 2.25),
# # # # # # # # # #             ("Power Saw", 75.00),
# # # # # # # # # #             ("Sand Paper", 1.50),
# # # # # # # # # #             ("Measuring Tape", 6.00),
# # # # # # # # # #             ("Welding Machine (BEME)", 15.00),
# # # # # # # # # #             ("Oxy-Acetylene Sets", 50.00),
# # # # # # # # # #             ("Power Saw (BEME)", 75.00),
# # # # # # # # # #             ("Drilling Machine", 45.00),
# # # # # # # # # #             ("Hand Drilling Machine", 25.00),
# # # # # # # # # #             ("Grinding Machine (BEME)", 8.75),
# # # # # # # # # #             ("Monitor", 120.00),
# # # # # # # # # #             ("Projector", 300.00),
# # # # # # # # # #             ("Marker Pen", 1.00),
# # # # # # # # # #             ("Extension Code", 20.00)
# # # # # # # # # #         ]
# # # # # # # # # #         cursor.executemany("INSERT INTO inventory (item_name, price) VALUES (?, ?)", sample_data)

# # # # # # # # # #     conn.commit()
# # # # # # # # # #     conn.close()

# # # # # # # # # # # Load inventory data from the database
# # # # # # # # # # def load_inventory_data():
# # # # # # # # # #     global inventory_data
# # # # # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # # # # #     cursor = conn.cursor()

# # # # # # # # # #     cursor.execute("SELECT item_name, price FROM inventory")
# # # # # # # # # #     inventory_data = {item[0]: item[1] for item in cursor.fetchall()}
# # # # # # # # # #     conn.close()

# # # # # # # # # # # Clear the frame function
# # # # # # # # # # def clear_frame():
# # # # # # # # # #     for widget in root.winfo_children():
# # # # # # # # # #         widget.destroy()

# # # # # # # # # # # Admin Login Page
# # # # # # # # # # def admin_login_page():
# # # # # # # # # #     clear_frame()
# # # # # # # # # #     history.append(admin_login_page)
# # # # # # # # # #     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # # # # #     tk.Label(root, text="Email").pack()
# # # # # # # # # #     email_entry = tk.Entry(root)
# # # # # # # # # #     email_entry.pack(pady=5)

# # # # # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # # # # #     password_entry.pack(pady=5)

# # # # # # # # # #     def login():
# # # # # # # # # #         global is_admin
# # # # # # # # # #         if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
# # # # # # # # # #             is_admin = True  # Set as admin
# # # # # # # # # #             inventory_status_page()
# # # # # # # # # #         else:
# # # # # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # # # # # User Login Page
# # # # # # # # # # def user_login_page():
# # # # # # # # # #     clear_frame()
# # # # # # # # # #     history.append(user_login_page)
# # # # # # # # # #     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # # # # #     tk.Label(root, text="Username").pack()
# # # # # # # # # #     username_entry = tk.Entry(root)
# # # # # # # # # #     username_entry.pack(pady=5)

# # # # # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # # # # #     password_entry.pack(pady=5)

# # # # # # # # # #     def login():
# # # # # # # # # #         global is_admin
# # # # # # # # # #         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
# # # # # # # # # #             is_admin = False  # Set as user
# # # # # # # # # #             user_view_department()
# # # # # # # # # #         else:
# # # # # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # # # # # User View - Departments Only
# # # # # # # # # # def user_view_department():
# # # # # # # # # #     clear_frame()
# # # # # # # # # #     history.append(user_view_department)
# # # # # # # # # #     tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # # # # #     for dept in departments:
# # # # # # # # # #         tk.Button(root, text=dept, command=lambda d=dept: user_view_price(d)).pack(pady=10)

# # # # # # # # # #     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# # # # # # # # # # # User View Prices based on Department
# # # # # # # # # # def user_view_price(department):
# # # # # # # # # #     clear_frame()
# # # # # # # # # #     history.append(user_view_price)

# # # # # # # # # #     tk.Label(root, text=f"Inventory Price List for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # #     items = []
# # # # # # # # # #     if department == "BEPE":
# # # # # # # # # #         items = [
# # # # # # # # # #             "1. M.s Pipe: $10.99",
# # # # # # # # # #             "2. Electrode: $12.49",
# # # # # # # # # #             "3. Grinding Machine: $8.75",
# # # # # # # # # #             "4. Welding Machine: $15.00",
# # # # # # # # # #             "5. Try Square: $5.50",
# # # # # # # # # #             "6. Thread: $2.25",
# # # # # # # # # #             "7. Power Saw: $75.00",
# # # # # # # # # #             "8. Sand Paper: $1.50",
# # # # # # # # # #             "9. Measuring Tape: $6.00"
# # # # # # # # # #         ]
# # # # # # # # # #     elif department == "BEME":
# # # # # # # # # #         items = [
# # # # # # # # # #             "1. Welding Machine: $15.00",
# # # # # # # # # #             "2. Oxy-Acetylene Sets: $50.00",
# # # # # # # # # #             "3. Power Saw: $75.00",
# # # # # # # # # #             "4. Drilling Machine: $45.00",
# # # # # # # # # #             "5. Hand Drilling Machine: $25.00",
# # # # # # # # # #             "6. Grinding Machine: $8.75"
# # # # # # # # # #         ]
# # # # # # # # # #     else:  # CSN
# # # # # # # # # #         items = [
# # # # # # # # # #             "1. Monitor: $120.00",
# # # # # # # # # #             "2. Projector: $300.00",
# # # # # # # # # #             "3. Marker Pen: $1.00",
# # # # # # # # # #             "4. Extension Code: $20.00"
# # # # # # # # # #         ]

# # # # # # # # # #     for item in items:
# # # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # # #     # Adding Price Button for the inventory inside each department price view.
# # # # # # # # # #     tk.Button(root, text="Show Price List", command=lambda: show_price_details(department)).pack(pady=5)

# # # # # # # # # #     tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)

# # # # # # # # # # # Show Price Details function
# # # # # # # # # # def show_price_details(department):
# # # # # # # # # #     clear_frame()
# # # # # # # # # #     tk.Label(root, text=f"Price Details for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # #     if department == "BEPE":
# # # # # # # # # #         items = [
# # # # # # # # # #             "1. M.s Pipe: $10.99",
# # # # # # # # # #             "2. Electrode: $12.49",
# # # # # # # # # #             "3. Grinding Machine: $8.75",
# # # # # # # # # #             "4. Welding Machine: $15.00",
# # # # # # # # # #             "5. Try Square: $5.50",
# # # # # # # # # #             "6. Thread: $2.25",
# # # # # # # # # #             "7. Power Saw: $75.00",
# # # # # # # # # #             "8. Sand Paper: $1.50",
# # # # # # # # # #             "9. Measuring Tape: $6.00"
# # # # # # # # # #         ]
# # # # # # # # # #     elif department == "BEME":
# # # # # # # # # #         items = [
# # # # # # # # # #             "1. Welding Machine: $15.00",
# # # # # # # # # #             "2. Oxy-Acetylene Sets: $50.00",
# # # # # # # # # #             "3. Power Saw: $75.00",
# # # # # # # # # #             "4. Drilling Machine: $45.00",
# # # # # # # # # #             "5. Hand Drilling Machine: $25.00",
# # # # # # # # # #             "6. Grinding Machine: $8.75"
# # # # # # # # # #         ]
# # # # # # # # # #     else:  # CSN
# # # # # # # # # #         items = [
# # # # # # # # # #             "1. Monitor: $120.00",
# # # # # # # # # #             "2. Projector: $300.00",
# # # # # # # # # #             "3. Marker Pen: $1.00",
# # # # # # # # # #             "4. Extension Code: $20.00"
# # # # # # # # # #         ]

# # # # # # # # # #     for item in items:
# # # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # # #     tk.Button(root, text="Back to Prices", command=lambda: user_view_price(department)).pack(pady=20)

# # # # # # # # # # # Inventory Status Page (Admin)
# # # # # # # # # # def inventory_status_page():
# # # # # # # # # #     clear_frame()
# # # # # # # # # #     history.append(inventory_status_page)
# # # # # # # # # #     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # #     tk.Button(root, text="Department", command=department_list_page).pack(pady=5)
# # # # # # # # # #     tk.Button(root, text="Price", command=lambda: show_price_details("BEPE")).pack(pady=5)  # Specify a default department
# # # # # # # # # #     tk.Button(root, text="Update", command=update_inventory_page).pack(pady=5)  # Update button
# # # # # # # # # #     tk.Button(root, text="Report", command=report_page).pack(pady=5)
# # # # # # # # # #     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# # # # # # # # # # # Update Inventory Page (Admin)
# # # # # # # # # # def update_inventory_page():
# # # # # # # # # #     clear_frame()
# # # # # # # # # #     history.append(update_inventory_page)
# # # # # # # # # #     tk.Label(root, text="Update Inventory", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # #     item_name_label = tk.Label(root, text="Item Name")
# # # # # # # # # #     item_name_label.pack(pady=5)
# # # # # # # # # #     item_name_entry = tk.Entry(root)
# # # # # # # # # #     item_name_entry.pack(pady=5)

# # # # # # # # # #     price_label = tk.Label(root, text="New Price")
# # # # # # # # # #     price_label.pack(pady=5)
# # # # # # # # # #     price_entry = tk.Entry(root)
# # # # # # # # # #     price_entry.pack(pady=5)

# # # # # # # # # #     def update_item():
# # # # # # # # # #         item_name = item_name_entry.get().strip()
# # # # # # # # # #         new_price = price_entry.get().strip()

# # # # # # # # # #         # Check if item exists in a case-insensitive way
# # # # # # # # # #         normalized_inventory = {k.lower(): v for k, v in inventory_data.items()}
# # # # # # # # # #         item_key = item_name.lower()

# # # # # # # # # #         if item_key in normalized_inventory and new_price.replace('.', '', 1).isdigit():
# # # # # # # # # #             new_price = float(new_price)
# # # # # # # # # #             conn = sqlite3.connect('inventory.db')
# # # # # # # # # #             cursor = conn.cursor()
# # # # # # # # # #             cursor.execute("UPDATE inventory SET price = ? WHERE item_name = ?", (new_price, item_name))
# # # # # # # # # #             conn.commit()
# # # # # # # # # #             conn.close()
# # # # # # # # # #             messagebox.showinfo("Success", f"Updated '{item_name}' to ${new_price:.2f}")
# # # # # # # # # #             load_inventory_data()  # Reload inventory data
# # # # # # # # # #         else:
# # # # # # # # # #             if item_key not in normalized_inventory:
# # # # # # # # # #                 messagebox.showerror("Error", "Item name does not exist.")
# # # # # # # # # #             else:
# # # # # # # # # #                 messagebox.showerror("Error", "Invalid price. Please enter a valid numeric value.")

# # # # # # # # # #     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
# # # # # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # # # # # # # # Department List Page (Admin)
# # # # # # # # # # def department_list_page():
# # # # # # # # # #     clear_frame()
# # # # # # # # # #     history.append(department_list_page)
# # # # # # # # # #     tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # # # # #     for dept in departments:
# # # # # # # # # #         tk.Button(root, text=dept, command=lambda d=dept: raw_materials_options_page(d)).pack(pady=10)

# # # # # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)  # Back button added

# # # # # # # # # # # Raw Materials Options Page
# # # # # # # # # # def raw_materials_options_page(department):
# # # # # # # # # #     clear_frame()
# # # # # # # # # #     history.append(raw_materials_options_page)
# # # # # # # # # #     tk.Label(root, text=f"Raw Materials for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # # #     if department == "BEPE":
# # # # # # # # # #         items = [
# # # # # # # # # #             "1. M.s Pipe",
# # # # # # # # # #             "2. Electrode",
# # # # # # # # # #             "3. Grinding Machine",
# # # # # # # # # #             "4. Welding Machine",
# # # # # # # # # #             "5. Try Square",
# # # # # # # # # #             "6. Thread",
# # # # # # # # # #             "7. Power Saw",
# # # # # # # # # #             "8. Sand Paper",
# # # # # # # # # #             "9. Measuring Tape"
# # # # # # # # # #         ]
# # # # # # # # # #     elif department == "BEME":
# # # # # # # # # #         items = [
# # # # # # # # # #             "1. Welding Machine",
# # # # # # # # # #             "2. Oxy-Acetylene Sets",
# # # # # # # # # #             "3. Power Saw",
# # # # # # # # # #             "4. Drilling Machine",
# # # # # # # # # #             "5. Hand Drilling Machine",
# # # # # # # # # #             "6. Grinding Machine"
# # # # # # # # # #         ]
# # # # # # # # # #     else:  # CSN
# # # # # # # # # #         items = [
# # # # # # # # # #             "1. Monitor",
# # # # # # # # # #             "2. Projector",
# # # # # # # # # #             "3. Marker Pen",
# # # # # # # # # #             "4. Extension Code"
# # # # # # # # # #         ]

# # # # # # # # # #     for item in items:
# # # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # # #     tk.Button(root, text="Back", command=department_list_page).pack(pady=20)

# # # # # # # # # # # Start with Admin/User Login Options
# # # # # # # # # # def get_started_page():
# # # # # # # # # #     clear_frame()
# # # # # # # # # #     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
# # # # # # # # # #     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
# # # # # # # # # #     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# # # # # # # # # # # Call the init_db to create the database and load data
# # # # # # # # # # init_db()
# # # # # # # # # # load_inventory_data()

# # # # # # # # # # # Call the get started page to initiate
# # # # # # # # # # get_started_page()
# # # # # # # # # # root.mainloop()   

# # # # # # # # # import tkinter as tk
# # # # # # # # # from tkinter import messagebox
# # # # # # # # # import sqlite3

# # # # # # # # # # Initialize global variables
# # # # # # # # # root = tk.Tk()
# # # # # # # # # inventory_data = {}  # This will be populated from the database
# # # # # # # # # history = []
# # # # # # # # # is_admin = False

# # # # # # # # # # Initialize the SQLite database
# # # # # # # # # def init_db():
# # # # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # # # #     cursor = conn.cursor()

# # # # # # # # #     # Create Inventory Table
# # # # # # # # #     cursor.execute('''
# # # # # # # # #     CREATE TABLE IF NOT EXISTS inventory (
# # # # # # # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # # # # # # #         item_name TEXT NOT NULL,
# # # # # # # # #         price REAL NOT NULL
# # # # # # # # #     )
# # # # # # # # #     ''')

# # # # # # # # #     # Insert sample inventory data if the table is empty
# # # # # # # # #     cursor.execute("SELECT COUNT(*) FROM inventory")
# # # # # # # # #     if cursor.fetchone()[0] == 0:  # If table is empty
# # # # # # # # #         sample_data = [
# # # # # # # # #             ("M.s Pipe", 10.99),
# # # # # # # # #             ("Electrode", 12.49),
# # # # # # # # #             ("Grinding Machine", 8.75),
# # # # # # # # #             ("Welding Machine", 15.00),
# # # # # # # # #             ("Try Square", 5.50),
# # # # # # # # #             ("Thread", 2.25),
# # # # # # # # #             ("Power Saw", 75.00),
# # # # # # # # #             ("Sand Paper", 1.50),
# # # # # # # # #             ("Measuring Tape", 6.00),
# # # # # # # # #             ("Welding Machine (BEME)", 15.00),
# # # # # # # # #             ("Oxy-Acetylene Sets", 50.00),
# # # # # # # # #             ("Power Saw (BEME)", 75.00),
# # # # # # # # #             ("Drilling Machine", 45.00),
# # # # # # # # #             ("Hand Drilling Machine", 25.00),
# # # # # # # # #             ("Grinding Machine (BEME)", 8.75),
# # # # # # # # #             ("Monitor", 120.00),
# # # # # # # # #             ("Projector", 300.00),
# # # # # # # # #             ("Marker Pen", 1.00),
# # # # # # # # #             ("Extension Code", 20.00)
# # # # # # # # #         ]
# # # # # # # # #         cursor.executemany("INSERT INTO inventory (item_name, price) VALUES (?, ?)", sample_data)

# # # # # # # # #     conn.commit()
# # # # # # # # #     conn.close()

# # # # # # # # # # Load inventory data from the database
# # # # # # # # # def load_inventory_data():
# # # # # # # # #     global inventory_data
# # # # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # # # #     cursor = conn.cursor()

# # # # # # # # #     cursor.execute("SELECT item_name, price FROM inventory")
# # # # # # # # #     inventory_data = {item[0]: item[1] for item in cursor.fetchall()}
# # # # # # # # #     conn.close()

# # # # # # # # # # Clear the frame function
# # # # # # # # # def clear_frame():
# # # # # # # # #     for widget in root.winfo_children():
# # # # # # # # #         widget.destroy()

# # # # # # # # # # Admin Login Page
# # # # # # # # # def admin_login_page():
# # # # # # # # #     clear_frame()
# # # # # # # # #     history.append(admin_login_page)
# # # # # # # # #     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # # # #     tk.Label(root, text="Email").pack()
# # # # # # # # #     email_entry = tk.Entry(root)
# # # # # # # # #     email_entry.pack(pady=5)

# # # # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # # # #     password_entry.pack(pady=5)

# # # # # # # # #     def login():
# # # # # # # # #         global is_admin
# # # # # # # # #         if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
# # # # # # # # #             is_admin = True  # Set as admin
# # # # # # # # #             inventory_status_page()
# # # # # # # # #         else:
# # # # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # # # # User Login Page
# # # # # # # # # def user_login_page():
# # # # # # # # #     clear_frame()
# # # # # # # # #     history.append(user_login_page)
# # # # # # # # #     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # # # #     tk.Label(root, text="Username").pack()
# # # # # # # # #     username_entry = tk.Entry(root)
# # # # # # # # #     username_entry.pack(pady=5)

# # # # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # # # #     password_entry.pack(pady=5)

# # # # # # # # #     def login():
# # # # # # # # #         global is_admin
# # # # # # # # #         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
# # # # # # # # #             is_admin = False  # Set as user
# # # # # # # # #             user_view_department()
# # # # # # # # #         else:
# # # # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # # # # User View - Departments Only
# # # # # # # # # def user_view_department():
# # # # # # # # #     clear_frame()
# # # # # # # # #     history.append(user_view_department)
# # # # # # # # #     tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # # # #     for dept in departments:
# # # # # # # # #         tk.Button(root, text=dept, command=lambda d=dept: user_view_price(d)).pack(pady=10)
# # # # # # # # #         tk.Button(root, text=f"Show Price List for {dept}", command=lambda d=dept: show_price_details(d)).pack(pady=5)

# # # # # # # # #     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# # # # # # # # # # User View Prices based on Department
# # # # # # # # # def user_view_price(department):
# # # # # # # # #     clear_frame()
# # # # # # # # #     history.append(user_view_price)

# # # # # # # # #     tk.Label(root, text=f"Inventory Price List for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # #     items = []
# # # # # # # # #     if department == "BEPE":
# # # # # # # # #         items = [
# # # # # # # # #             "1. M.s Pipe: $10.99",
# # # # # # # # #             "2. Electrode: $12.49",
# # # # # # # # #             "3. Grinding Machine: $8.75",
# # # # # # # # #             "4. Welding Machine: $15.00",
# # # # # # # # #             "5. Try Square: $5.50",
# # # # # # # # #             "6. Thread: $2.25",
# # # # # # # # #             "7. Power Saw: $75.00",
# # # # # # # # #             "8. Sand Paper: $1.50",
# # # # # # # # #             "9. Measuring Tape: $6.00"
# # # # # # # # #         ]
# # # # # # # # #     elif department == "BEME":
# # # # # # # # #         items = [
# # # # # # # # #             "1. Welding Machine: $15.00",
# # # # # # # # #             "2. Oxy-Acetylene Sets: $50.00",
# # # # # # # # #             "3. Power Saw: $75.00",
# # # # # # # # #             "4. Drilling Machine: $45.00",
# # # # # # # # #             "5. Hand Drilling Machine: $25.00",
# # # # # # # # #             "6. Grinding Machine: $8.75"
# # # # # # # # #         ]
# # # # # # # # #     else:  # CSN
# # # # # # # # #         items = [
# # # # # # # # #             "1. Monitor: $120.00",
# # # # # # # # #             "2. Projector: $300.00",
# # # # # # # # #             "3. Marker Pen: $1.00",
# # # # # # # # #             "4. Extension Code: $20.00"
# # # # # # # # #         ]

# # # # # # # # #     for item in items:
# # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # #     tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)

# # # # # # # # # # Show Price Details function
# # # # # # # # # def show_price_details(department):
# # # # # # # # #     clear_frame()
# # # # # # # # #     tk.Label(root, text=f"Price Details for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # #     if department == "BEPE":
# # # # # # # # #         items = [
# # # # # # # # #             "1. M.s Pipe: $10.99",
# # # # # # # # #             "2. Electrode: $12.49",
# # # # # # # # #             "3. Grinding Machine: $8.75",
# # # # # # # # #             "4. Welding Machine: $15.00",
# # # # # # # # #             "5. Try Square: $5.50",
# # # # # # # # #             "6. Thread: $2.25",
# # # # # # # # #             "7. Power Saw: $75.00",
# # # # # # # # #             "8. Sand Paper: $1.50",
# # # # # # # # #             "9. Measuring Tape: $6.00"
# # # # # # # # #         ]
# # # # # # # # #     elif department == "BEME":
# # # # # # # # #         items = [
# # # # # # # # #             "1. Welding Machine: $15.00",
# # # # # # # # #             "2. Oxy-Acetylene Sets: $50.00",
# # # # # # # # #             "3. Power Saw: $75.00",
# # # # # # # # #             "4. Drilling Machine: $45.00",
# # # # # # # # #             "5. Hand Drilling Machine: $25.00",
# # # # # # # # #             "6. Grinding Machine: $8.75"
# # # # # # # # #         ]
# # # # # # # # #     else:  # CSN
# # # # # # # # #         items = [
# # # # # # # # #             "1. Monitor: $120.00",
# # # # # # # # #             "2. Projector: $300.00",
# # # # # # # # #             "3. Marker Pen: $1.00",
# # # # # # # # #             "4. Extension Code: $20.00"
# # # # # # # # #         ]

# # # # # # # # #     for item in items:
# # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # #     tk.Button(root, text="Back to Prices", command=lambda: user_view_price(department)).pack(pady=20)

# # # # # # # # # # Inventory Status Page (Admin)
# # # # # # # # # def inventory_status_page():
# # # # # # # # #     clear_frame()
# # # # # # # # #     history.append(inventory_status_page)
# # # # # # # # #     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # #     tk.Button(root, text="Department", command=department_list_page).pack(pady=5)
# # # # # # # # #     tk.Button(root, text="Price", command=lambda: show_price_details("BEPE")).pack(pady=5)  # Specify a default department
# # # # # # # # #     tk.Button(root, text="Update", command=update_inventory_page).pack(pady=5)  # Update button
# # # # # # # # #     tk.Button(root, text="Report", command=report_page).pack(pady=5)
# # # # # # # # #     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# # # # # # # # # # Update Inventory Page (Admin)
# # # # # # # # # def update_inventory_page():
# # # # # # # # #     clear_frame()
# # # # # # # # #     history.append(update_inventory_page)
# # # # # # # # #     tk.Label(root, text="Update Inventory", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # #     item_name_label = tk.Label(root, text="Item Name")
# # # # # # # # #     item_name_label.pack(pady=5)
# # # # # # # # #     item_name_entry = tk.Entry(root)
# # # # # # # # #     item_name_entry.pack(pady=5)

# # # # # # # # #     price_label = tk.Label(root, text="New Price")
# # # # # # # # #     price_label.pack(pady=5)
# # # # # # # # #     price_entry = tk.Entry(root)
# # # # # # # # #     price_entry.pack(pady=5)

# # # # # # # # #     def update_item():
# # # # # # # # #         item_name = item_name_entry.get().strip()
# # # # # # # # #         new_price = price_entry.get().strip()

# # # # # # # # #         # Check if item exists in a case-insensitive way
# # # # # # # # #         normalized_inventory = {k.lower(): v for k, v in inventory_data.items()}
# # # # # # # # #         item_key = item_name.lower()

# # # # # # # # #         if item_key in normalized_inventory and new_price.replace('.', '', 1).isdigit():
# # # # # # # # #             new_price = float(new_price)
# # # # # # # # #             conn = sqlite3.connect('inventory.db')
# # # # # # # # #             cursor = conn.cursor()
# # # # # # # # #             cursor.execute("UPDATE inventory SET price = ? WHERE item_name = ?", (new_price, item_name))
# # # # # # # # #             conn.commit()
# # # # # # # # #             conn.close()
# # # # # # # # #             messagebox.showinfo("Success", f"Updated '{item_name}' to ${new_price:.2f}")
# # # # # # # # #             load_inventory_data()  # Reload inventory data
# # # # # # # # #         else:
# # # # # # # # #             if item_key not in normalized_inventory:
# # # # # # # # #                 messagebox.showerror("Error", "Item name does not exist.")
# # # # # # # # #             else:
# # # # # # # # #                 messagebox.showerror("Error", "Invalid price. Please enter a valid numeric value.")

# # # # # # # # #     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
# # # # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # # # # # # # Department List Page (Admin)
# # # # # # # # # def department_list_page():
# # # # # # # # #     clear_frame()
# # # # # # # # #     history.append(department_list_page)
# # # # # # # # #     tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # # # #     for dept in departments:
# # # # # # # # #         tk.Button(root, text=dept, command=lambda d=dept: raw_materials_options_page(d)).pack(pady=10)

# # # # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)  # Back button added

# # # # # # # # # # Raw Materials Options Page
# # # # # # # # # def raw_materials_options_page(department):
# # # # # # # # #     clear_frame()
# # # # # # # # #     history.append(raw_materials_options_page)
# # # # # # # # #     tk.Label(root, text=f"Raw Materials for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # # #     if department == "BEPE":
# # # # # # # # #         items = [
# # # # # # # # #             "1. M.s Pipe",
# # # # # # # # #             "2. Electrode",
# # # # # # # # #             "3. Grinding Machine",
# # # # # # # # #             "4. Welding Machine",
# # # # # # # # #             "5. Try Square",
# # # # # # # # #             "6. Thread",
# # # # # # # # #             "7. Power Saw",
# # # # # # # # #             "8. Sand Paper",
# # # # # # # # #             "9. Measuring Tape"
# # # # # # # # #         ]
# # # # # # # # #     elif department == "BEME":
# # # # # # # # #         items = [
# # # # # # # # #             "1. Welding Machine",
# # # # # # # # #             "2. Oxy-Acetylene Sets",
# # # # # # # # #             "3. Power Saw",
# # # # # # # # #             "4. Drilling Machine",
# # # # # # # # #             "5. Hand Drilling Machine",
# # # # # # # # #             "6. Grinding Machine"
# # # # # # # # #         ]
# # # # # # # # #     else:  # CSN
# # # # # # # # #         items = [
# # # # # # # # #             "1. Monitor",
# # # # # # # # #             "2. Projector",
# # # # # # # # #             "3. Marker Pen",
# # # # # # # # #             "4. Extension Code"
# # # # # # # # #         ]

# # # # # # # # #     for item in items:
# # # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # # #     tk.Button(root, text="Back", command=department_list_page).pack(pady=20)

# # # # # # # # # # Start with Admin/User Login Options
# # # # # # # # # def get_started_page():
# # # # # # # # #     clear_frame()
# # # # # # # # #     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
# # # # # # # # #     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
# # # # # # # # #     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# # # # # # # # # # Call the init_db to create the database and load data
# # # # # # # # # init_db()
# # # # # # # # # load_inventory_data()

# # # # # # # # # # Call the get started page to initiate
# # # # # # # # # get_started_page()
# # # # # # # # # root.mainloop()

# # # # # # # # import tkinter as tk
# # # # # # # # from tkinter import messagebox
# # # # # # # # import sqlite3

# # # # # # # # # Initialize global variables
# # # # # # # # root = tk.Tk()
# # # # # # # # inventory_data = {}  # This will be populated from the database
# # # # # # # # history = []
# # # # # # # # is_admin = False

# # # # # # # # # Initialize the SQLite database
# # # # # # # # def init_db():
# # # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # # #     cursor = conn.cursor()

# # # # # # # #     # Create Inventory Table
# # # # # # # #     cursor.execute('''
# # # # # # # #     CREATE TABLE IF NOT EXISTS inventory (
# # # # # # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # # # # # #         item_name TEXT NOT NULL,
# # # # # # # #         price REAL NOT NULL
# # # # # # # #     )
# # # # # # # #     ''')

# # # # # # # #     # Insert sample inventory data if the table is empty
# # # # # # # #     cursor.execute("SELECT COUNT(*) FROM inventory")
# # # # # # # #     if cursor.fetchone()[0] == 0:  # If table is empty
# # # # # # # #         sample_data = [
# # # # # # # #             ("M.s Pipe", 10.99),
# # # # # # # #             ("Electrode", 12.49),
# # # # # # # #             ("Grinding Machine", 8.75),
# # # # # # # #             ("Welding Machine", 15.00),
# # # # # # # #             ("Try Square", 5.50),
# # # # # # # #             ("Thread", 2.25),
# # # # # # # #             ("Power Saw", 75.00),
# # # # # # # #             ("Sand Paper", 1.50),
# # # # # # # #             ("Measuring Tape", 6.00),
# # # # # # # #             ("Welding Machine (BEME)", 15.00),
# # # # # # # #             ("Oxy-Acetylene Sets", 50.00),
# # # # # # # #             ("Power Saw (BEME)", 75.00),
# # # # # # # #             ("Drilling Machine", 45.00),
# # # # # # # #             ("Hand Drilling Machine", 25.00),
# # # # # # # #             ("Grinding Machine (BEME)", 8.75),
# # # # # # # #             ("Monitor", 120.00),
# # # # # # # #             ("Projector", 300.00),
# # # # # # # #             ("Marker Pen", 1.00),
# # # # # # # #             ("Extension Code", 20.00)
# # # # # # # #         ]
# # # # # # # #         cursor.executemany("INSERT INTO inventory (item_name, price) VALUES (?, ?)", sample_data)

# # # # # # # #     conn.commit()
# # # # # # # #     conn.close()

# # # # # # # # # Load inventory data from the database
# # # # # # # # def load_inventory_data():
# # # # # # # #     global inventory_data
# # # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # # #     cursor = conn.cursor()

# # # # # # # #     cursor.execute("SELECT item_name, price FROM inventory")
# # # # # # # #     inventory_data = {item[0]: item[1] for item in cursor.fetchall()}
# # # # # # # #     conn.close()

# # # # # # # # # Clear the frame function
# # # # # # # # def clear_frame():
# # # # # # # #     for widget in root.winfo_children():
# # # # # # # #         widget.destroy()

# # # # # # # # # Admin Login Page
# # # # # # # # def admin_login_page():
# # # # # # # #     clear_frame()
# # # # # # # #     history.append(admin_login_page)
# # # # # # # #     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # # #     tk.Label(root, text="Email").pack()
# # # # # # # #     email_entry = tk.Entry(root)
# # # # # # # #     email_entry.pack(pady=5)

# # # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # # #     password_entry.pack(pady=5)

# # # # # # # #     def login():
# # # # # # # #         global is_admin
# # # # # # # #         if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
# # # # # # # #             is_admin = True  # Set as admin
# # # # # # # #             inventory_status_page()
# # # # # # # #         else:
# # # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # # # User Login Page
# # # # # # # # def user_login_page():
# # # # # # # #     clear_frame()
# # # # # # # #     history.append(user_login_page)
# # # # # # # #     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # # #     tk.Label(root, text="Username").pack()
# # # # # # # #     username_entry = tk.Entry(root)
# # # # # # # #     username_entry.pack(pady=5)

# # # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # # #     password_entry.pack(pady=5)

# # # # # # # #     def login():
# # # # # # # #         global is_admin
# # # # # # # #         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
# # # # # # # #             is_admin = False  # Set as user
# # # # # # # #             user_view_department()
# # # # # # # #         else:
# # # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # # # User View - Departments Only
# # # # # # # # def user_view_department():
# # # # # # # #     clear_frame()
# # # # # # # #     history.append(user_view_department)
# # # # # # # #     tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # # #     for dept in departments:
# # # # # # # #         # Create a frame for each department
# # # # # # # #         dept_frame = tk.Frame(root)
# # # # # # # #         dept_frame.pack(pady=10)
        
# # # # # # # #         tk.Label(dept_frame, text=dept, font=('Helvetica', 16)).pack(side=tk.LEFT)

# # # # # # # #         # Button to view items in that department
# # # # # # # #         tk.Button(dept_frame, text="Show Items", command=lambda d=dept: user_view_price(d)).pack(side=tk.LEFT, padx=10)

# # # # # # # #         # Button to show prices for that department
# # # # # # # #         tk.Button(dept_frame, text="Show Price List", command=lambda d=dept: show_price_details(d)).pack(side=tk.LEFT)

# # # # # # # #     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# # # # # # # # # User View Prices based on Department
# # # # # # # # def user_view_price(department):
# # # # # # # #     clear_frame()
# # # # # # # #     history.append(user_view_price)

# # # # # # # #     tk.Label(root, text=f"Inventory Items in {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # #     items = []
# # # # # # # #     if department == "BEPE":
# # # # # # # #         items = [
# # # # # # # #             "1. M.s Pipe",
# # # # # # # #             "2. Electrode",
# # # # # # # #             "3. Grinding Machine",
# # # # # # # #             "4. Welding Machine",
# # # # # # # #             "5. Try Square",
# # # # # # # #             "6. Thread",
# # # # # # # #             "7. Power Saw",
# # # # # # # #             "8. Sand Paper",
# # # # # # # #             "9. Measuring Tape"
# # # # # # # #         ]
# # # # # # # #     elif department == "BEME":
# # # # # # # #         items = [
# # # # # # # #             "1. Welding Machine",
# # # # # # # #             "2. Oxy-Acetylene Sets",
# # # # # # # #             "3. Power Saw",
# # # # # # # #             "4. Drilling Machine",
# # # # # # # #             "5. Hand Drilling Machine",
# # # # # # # #             "6. Grinding Machine"
# # # # # # # #         ]
# # # # # # # #     else:  # CSN
# # # # # # # #         items = [
# # # # # # # #             "1. Monitor",
# # # # # # # #             "2. Projector",
# # # # # # # #             "3. Marker Pen",
# # # # # # # #             "4. Extension Code"
# # # # # # # #         ]

# # # # # # # #     for item in items:
# # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # #     tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)

# # # # # # # # # Show Price Details function
# # # # # # # # def show_price_details(department):
# # # # # # # #     clear_frame()
# # # # # # # #     tk.Label(root, text=f"Price Details for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # #     if department == "BEPE":
# # # # # # # #         items = [
# # # # # # # #             "1. M.s Pipe: $10.99",
# # # # # # # #             "2. Electrode: $12.49",
# # # # # # # #             "3. Grinding Machine: $8.75",
# # # # # # # #             "4. Welding Machine: $15.00",
# # # # # # # #             "5. Try Square: $5.50",
# # # # # # # #             "6. Thread: $2.25",
# # # # # # # #             "7. Power Saw: $75.00",
# # # # # # # #             "8. Sand Paper: $1.50",
# # # # # # # #             "9. Measuring Tape: $6.00"
# # # # # # # #         ]
# # # # # # # #     elif department == "BEME":
# # # # # # # #         items = [
# # # # # # # #             "1. Welding Machine: $15.00",
# # # # # # # #             "2. Oxy-Acetylene Sets: $50.00",
# # # # # # # #             "3. Power Saw: $75.00",
# # # # # # # #             "4. Drilling Machine: $45.00",
# # # # # # # #             "5. Hand Drilling Machine: $25.00",
# # # # # # # #             "6. Grinding Machine: $8.75"
# # # # # # # #         ]
# # # # # # # #     else:  # CSN
# # # # # # # #         items = [
# # # # # # # #             "1. Monitor: $120.00",
# # # # # # # #             "2. Projector: $300.00",
# # # # # # # #             "3. Marker Pen: $1.00",
# # # # # # # #             "4. Extension Code: $20.00"
# # # # # # # #         ]

# # # # # # # #     for item in items:
# # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # #     tk.Button(root, text="Back to Prices", command=lambda: user_view_price(department)).pack(pady=20)

# # # # # # # # # Inventory Status Page (Admin)
# # # # # # # # def inventory_status_page():
# # # # # # # #     clear_frame()
# # # # # # # #     history.append(inventory_status_page)
# # # # # # # #     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # #     tk.Button(root, text="Department", command=department_list_page).pack(pady=5)
# # # # # # # #     tk.Button(root, text="Price", command=lambda: show_price_details("BEPE")).pack(pady=5)  # Specify a default department
# # # # # # # #     tk.Button(root, text="Update", command=update_inventory_page).pack(pady=5)  # Update button
# # # # # # # #     tk.Button(root, text="Report", command=report_page).pack(pady=5)
# # # # # # # #     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# # # # # # # # # Update Inventory Page (Admin)
# # # # # # # # def update_inventory_page():
# # # # # # # #     clear_frame()
# # # # # # # #     history.append(update_inventory_page)
# # # # # # # #     tk.Label(root, text="Update Inventory", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # #     item_name_label = tk.Label(root, text="Item Name")
# # # # # # # #     item_name_label.pack(pady=5)
# # # # # # # #     item_name_entry = tk.Entry(root)
# # # # # # # #     item_name_entry.pack(pady=5)

# # # # # # # #     price_label = tk.Label(root, text="New Price")
# # # # # # # #     price_label.pack(pady=5)
# # # # # # # #     price_entry = tk.Entry(root)
# # # # # # # #     price_entry.pack(pady=5)

# # # # # # # #     def update_item():
# # # # # # # #         item_name = item_name_entry.get().strip()
# # # # # # # #         new_price = price_entry.get().strip()

# # # # # # # #         # Check if item exists in a case-insensitive way
# # # # # # # #         normalized_inventory = {k.lower(): v for k, v in inventory_data.items()}
# # # # # # # #         item_key = item_name.lower()

# # # # # # # #         if item_key in normalized_inventory and new_price.replace('.', '', 1).isdigit():
# # # # # # # #             new_price = float(new_price)
# # # # # # # #             conn = sqlite3.connect('inventory.db')
# # # # # # # #             cursor = conn.cursor()
# # # # # # # #             cursor.execute("UPDATE inventory SET price = ? WHERE item_name = ?", (new_price, item_name))
# # # # # # # #             conn.commit()
# # # # # # # #             conn.close()
# # # # # # # #             messagebox.showinfo("Success", f"Updated '{item_name}' to ${new_price:.2f}")
# # # # # # # #             load_inventory_data()  # Reload inventory data
# # # # # # # #         else:
# # # # # # # #             if item_key not in normalized_inventory:
# # # # # # # #                 messagebox.showerror("Error", "Item name does not exist.")
# # # # # # # #             else:
# # # # # # # #                 messagebox.showerror("Error", "Invalid price. Please enter a valid numeric value.")

# # # # # # # #     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
# # # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # # # # # # Department List Page (Admin)
# # # # # # # # def department_list_page():
# # # # # # # #     clear_frame()
# # # # # # # #     history.append(department_list_page)
# # # # # # # #     tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # # #     for dept in departments:
# # # # # # # #         tk.Button(root, text=dept, command=lambda d=dept: raw_materials_options_page(d)).pack(pady=10)

# # # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)  # Back button added

# # # # # # # # # Raw Materials Options Page
# # # # # # # # def raw_materials_options_page(department):
# # # # # # # #     clear_frame()
# # # # # # # #     history.append(raw_materials_options_page)
# # # # # # # #     tk.Label(root, text=f"Raw Materials for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # # #     items = []
# # # # # # # #     if department == "BEPE":
# # # # # # # #         items = [
# # # # # # # #             "1. M.s Pipe",
# # # # # # # #             "2. Electrode",
# # # # # # # #             "3. Grinding Machine",
# # # # # # # #             "4. Welding Machine",
# # # # # # # #             "5. Try Square",
# # # # # # # #             "6. Thread",
# # # # # # # #             "7. Power Saw",
# # # # # # # #             "8. Sand Paper",
# # # # # # # #             "9. Measuring Tape"
# # # # # # # #         ]
# # # # # # # #     elif department == "BEME":
# # # # # # # #         items = [
# # # # # # # #             "1. Welding Machine",
# # # # # # # #             "2. Oxy-Acetylene Sets",
# # # # # # # #             "3. Power Saw",
# # # # # # # #             "4. Drilling Machine",
# # # # # # # #             "5. Hand Drilling Machine",
# # # # # # # #             "6. Grinding Machine"
# # # # # # # #         ]
# # # # # # # #     else:  # CSN
# # # # # # # #         items = [
# # # # # # # #             "1. Monitor",
# # # # # # # #             "2. Projector",
# # # # # # # #             "3. Marker Pen",
# # # # # # # #             "4. Extension Code"
# # # # # # # #         ]

# # # # # # # #     for item in items:
# # # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # # #     tk.Button(root, text="Back", command=department_list_page).pack(pady=20)

# # # # # # # # # Start with Admin/User Login Options
# # # # # # # # def get_started_page():
# # # # # # # #     clear_frame()
# # # # # # # #     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
# # # # # # # #     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
# # # # # # # #     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# # # # # # # # # Call the init_db to create the database and load data
# # # # # # # # init_db()
# # # # # # # # load_inventory_data()

# # # # # # # # # Call the get started page to initiate
# # # # # # # # get_started_page()
# # # # # # # # root.mainloop()

# # # # # # # import tkinter as tk
# # # # # # # from tkinter import messagebox
# # # # # # # from tkinter import ttk
# # # # # # # import sqlite3

# # # # # # # # Initialize global variables
# # # # # # # root = tk.Tk()
# # # # # # # inventory_data = {}  # This will be populated from the database
# # # # # # # history = []
# # # # # # # is_admin = False

# # # # # # # # Initialize the SQLite database
# # # # # # # def init_db():
# # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # #     cursor = conn.cursor()

# # # # # # #     # Create Inventory Table
# # # # # # #     cursor.execute('''
# # # # # # #     CREATE TABLE IF NOT EXISTS inventory (
# # # # # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # # # # #         item_name TEXT NOT NULL,
# # # # # # #         price REAL NOT NULL
# # # # # # #     )
# # # # # # #     ''')

# # # # # # #     # Insert sample inventory data if the table is empty
# # # # # # #     cursor.execute("SELECT COUNT(*) FROM inventory")
# # # # # # #     if cursor.fetchone()[0] == 0:  # If table is empty
# # # # # # #         sample_data = [
# # # # # # #             ("M.s Pipe", 10.99),
# # # # # # #             ("Electrode", 12.49),
# # # # # # #             ("Grinding Machine", 8.75),
# # # # # # #             ("Welding Machine", 15.00),
# # # # # # #             ("Try Square", 5.50),
# # # # # # #             ("Thread", 2.25),
# # # # # # #             ("Power Saw", 75.00),
# # # # # # #             ("Sand Paper", 1.50),
# # # # # # #             ("Measuring Tape", 6.00),
# # # # # # #             ("Welding Machine (BEME)", 15.00),
# # # # # # #             ("Oxy-Acetylene Sets", 50.00),
# # # # # # #             ("Power Saw (BEME)", 75.00),
# # # # # # #             ("Drilling Machine", 45.00),
# # # # # # #             ("Hand Drilling Machine", 25.00),
# # # # # # #             ("Grinding Machine (BEME)", 8.75),
# # # # # # #             ("Monitor", 120.00),
# # # # # # #             ("Projector", 300.00),
# # # # # # #             ("Marker Pen", 1.00),
# # # # # # #             ("Extension Code", 20.00)
# # # # # # #         ]
# # # # # # #         cursor.executemany("INSERT INTO inventory (item_name, price) VALUES (?, ?)", sample_data)

# # # # # # #     conn.commit()
# # # # # # #     conn.close()

# # # # # # # # Load inventory data from the database
# # # # # # # def load_inventory_data():
# # # # # # #     global inventory_data
# # # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # # #     cursor = conn.cursor()

# # # # # # #     cursor.execute("SELECT item_name, price FROM inventory")
# # # # # # #     inventory_data = {item[0]: item[1] for item in cursor.fetchall()}
# # # # # # #     conn.close()

# # # # # # # # Clear the frame function
# # # # # # # def clear_frame():
# # # # # # #     for widget in root.winfo_children():
# # # # # # #         widget.destroy()

# # # # # # # # Admin Login Page
# # # # # # # def admin_login_page():
# # # # # # #     clear_frame()
# # # # # # #     history.append(admin_login_page)
# # # # # # #     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # #     tk.Label(root, text="Email").pack()
# # # # # # #     email_entry = tk.Entry(root)
# # # # # # #     email_entry.pack(pady=5)

# # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # #     password_entry.pack(pady=5)

# # # # # # #     def login():
# # # # # # #         global is_admin
# # # # # # #         if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
# # # # # # #             is_admin = True  # Set as admin
# # # # # # #             inventory_status_page()
# # # # # # #         else:
# # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # # User Login Page
# # # # # # # def user_login_page():
# # # # # # #     clear_frame()
# # # # # # #     history.append(user_login_page)
# # # # # # #     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # # #     tk.Label(root, text="Username").pack()
# # # # # # #     username_entry = tk.Entry(root)
# # # # # # #     username_entry.pack(pady=5)

# # # # # # #     tk.Label(root, text="Password").pack()
# # # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # # #     password_entry.pack(pady=5)

# # # # # # #     def login():
# # # # # # #         global is_admin
# # # # # # #         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
# # # # # # #             is_admin = False  # Set as user
# # # # # # #             user_view_department()
# # # # # # #         else:
# # # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # # User View - Departments Only
# # # # # # # def user_view_department():
# # # # # # #     clear_frame()
# # # # # # #     history.append(user_view_department)
# # # # # # #     tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # #     for dept in departments:
# # # # # # #         dept_frame = tk.Frame(root)
# # # # # # #         dept_frame.pack(pady=10)

# # # # # # #         tk.Label(dept_frame, text=dept, font=('Helvetica', 16)).pack(side=tk.LEFT)

# # # # # # #         tk.Button(dept_frame, text="Show Items", command=lambda d=dept: user_view_price(d)).pack(side=tk.LEFT, padx=10)

# # # # # # #         tk.Button(dept_frame, text="Show Price List", command=lambda d=dept: show_price_details(d)).pack(side=tk.LEFT)

# # # # # # #     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# # # # # # # # Show Price Details function in Tabular Format
# # # # # # # def show_price_details(department):
# # # # # # #     clear_frame()
# # # # # # #     tk.Label(root, text=f"Price Details for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # #     # Create a Treeview to display the prices in a tabular format
# # # # # # #     tree = ttk.Treeview(root, columns=("Item", "Price"), show='headings')
# # # # # # #     tree.heading("Item", text="Item")
# # # # # # #     tree.heading("Price", text="Price")

# # # # # # #     # Data for the different departments
# # # # # # #     items = []
# # # # # # #     if department == "BEPE":
# # # # # # #         items = [
# # # # # # #             ("M.s Pipe", "$10.99"),
# # # # # # #             ("Electrode", "$12.49"),
# # # # # # #             ("Grinding Machine", "$8.75"),
# # # # # # #             ("Welding Machine", "$15.00"),
# # # # # # #             ("Try Square", "$5.50"),
# # # # # # #             ("Thread", "$2.25"),
# # # # # # #             ("Power Saw", "$75.00"),
# # # # # # #             ("Sand Paper", "$1.50"),
# # # # # # #             ("Measuring Tape", "$6.00")
# # # # # # #         ]
# # # # # # #     elif department == "BEME":
# # # # # # #         items = [
# # # # # # #             ("Welding Machine", "$15.00"),
# # # # # # #             ("Oxy-Acetylene Sets", "$50.00"),
# # # # # # #             ("Power Saw", "$75.00"),
# # # # # # #             ("Drilling Machine", "$45.00"),
# # # # # # #             ("Hand Drilling Machine", "$25.00"),
# # # # # # #             ("Grinding Machine", "$8.75")
# # # # # # #         ]
# # # # # # #     else:  # CSN
# # # # # # #         items = [
# # # # # # #             ("Monitor", "$120.00"),
# # # # # # #             ("Projector", "$300.00"),
# # # # # # #             ("Marker Pen", "$1.00"),
# # # # # # #             ("Extension Code", "$20.00")
# # # # # # #         ]

# # # # # # #     # Insert items into the Treeview
# # # # # # #     for item in items:
# # # # # # #         tree.insert("", "end", values=item)

# # # # # # #     tree.pack(pady=10)

# # # # # # #     tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)

# # # # # # # # Inventory Status Page (Admin)
# # # # # # # def inventory_status_page():
# # # # # # #     clear_frame()
# # # # # # #     history.append(inventory_status_page)
# # # # # # #     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # #     tk.Button(root, text="Department", command=department_list_page).pack(pady=5)
# # # # # # #     tk.Button(root, text="Price", command=lambda: show_price_details("BEPE")).pack(pady=5)  # Specify a default department
# # # # # # #     tk.Button(root, text="Update", command=update_inventory_page).pack(pady=5)  # Update button
# # # # # # #     tk.Button(root, text="Report", command=report_page).pack(pady=5)
# # # # # # #     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# # # # # # # # Update Inventory Page (Admin)
# # # # # # # def update_inventory_page():
# # # # # # #     clear_frame()
# # # # # # #     history.append(update_inventory_page)
# # # # # # #     tk.Label(root, text="Update Inventory", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # #     item_name_label = tk.Label(root, text="Item Name")
# # # # # # #     item_name_label.pack(pady=5)
# # # # # # #     item_name_entry = tk.Entry(root)
# # # # # # #     item_name_entry.pack(pady=5)

# # # # # # #     price_label = tk.Label(root, text="New Price")
# # # # # # #     price_label.pack(pady=5)
# # # # # # #     price_entry = tk.Entry(root)
# # # # # # #     price_entry.pack(pady=5)

# # # # # # #     def update_item():
# # # # # # #         item_name = item_name_entry.get().strip()
# # # # # # #         new_price = price_entry.get().strip()

# # # # # # #         # Check if item exists in a case-insensitive way
# # # # # # #         normalized_inventory = {k.lower(): v for k, v in inventory_data.items()}
# # # # # # #         item_key = item_name.lower()

# # # # # # #         if item_key in normalized_inventory and new_price.replace('.', '', 1).isdigit():
# # # # # # #             new_price = float(new_price)
# # # # # # #             conn = sqlite3.connect('inventory.db')
# # # # # # #             cursor = conn.cursor()
# # # # # # #             cursor.execute("UPDATE inventory SET price = ? WHERE item_name = ?", (new_price, item_name))
# # # # # # #             conn.commit()
# # # # # # #             conn.close()
# # # # # # #             messagebox.showinfo("Success", f"Updated '{item_name}' to ${new_price:.2f}")
# # # # # # #             load_inventory_data()  # Reload inventory data
# # # # # # #         else:
# # # # # # #             if item_key not in normalized_inventory:
# # # # # # #                 messagebox.showerror("Error", "Item name does not exist.")
# # # # # # #             else:
# # # # # # #                 messagebox.showerror("Error", "Invalid price. Please enter a valid numeric value.")

# # # # # # #     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
# # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # # # # # Department List Page (Admin)
# # # # # # # def department_list_page():
# # # # # # #     clear_frame()
# # # # # # #     history.append(department_list_page)
# # # # # # #     tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # # #     for dept in departments:
# # # # # # #         tk.Button(root, text=dept, command=lambda d=dept: raw_materials_options_page(d)).pack(pady=10)

# # # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)  # Back button added

# # # # # # # # Raw Materials Options Page
# # # # # # # def raw_materials_options_page(department):
# # # # # # #     clear_frame()
# # # # # # #     history.append(raw_materials_options_page)
# # # # # # #     tk.Label(root, text=f"Raw Materials for {department}", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # # #     items = []
# # # # # # #     if department == "BEPE":
# # # # # # #         items = [
# # # # # # #             "1. M.s Pipe",
# # # # # # #             "2. Electrode",
# # # # # # #             "3. Grinding Machine",
# # # # # # #             "4. Welding Machine",
# # # # # # #             "5. Try Square",
# # # # # # #             "6. Thread",
# # # # # # #             "7. Power Saw",
# # # # # # #             "8. Sand Paper",
# # # # # # #             "9. Measuring Tape"
# # # # # # #         ]
# # # # # # #     elif department == "BEME":
# # # # # # #         items = [
# # # # # # #             "1. Welding Machine",
# # # # # # #             "2. Oxy-Acetylene Sets",
# # # # # # #             "3. Power Saw",
# # # # # # #             "4. Drilling Machine",
# # # # # # #             "5. Hand Drilling Machine",
# # # # # # #             "6. Grinding Machine"
# # # # # # #         ]
# # # # # # #     else:  # CSN
# # # # # # #         items = [
# # # # # # #             "1. Monitor",
# # # # # # #             "2. Projector",
# # # # # # #             "3. Marker Pen",
# # # # # # #             "4. Extension Code"
# # # # # # #         ]

# # # # # # #     for item in items:
# # # # # # #         tk.Label(root, text=item).pack(pady=5)

# # # # # # #     tk.Button(root, text="Back", command=department_list_page).pack(pady=20)

# # # # # # # # Start with Admin/User Login Options
# # # # # # # def get_started_page():
# # # # # # #     clear_frame()
# # # # # # #     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
# # # # # # #     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
# # # # # # #     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# # # # # # # # Call the init_db to create the database and load data
# # # # # # # init_db()
# # # # # # # load_inventory_data()

# # # # # # # # Call the get started page to initiate
# # # # # # # get_started_page()
# # # # # # # root.mainloop()

# # # # # # import tkinter as tk
# # # # # # from tkinter import messagebox
# # # # # # from tkinter import ttk
# # # # # # import sqlite3

# # # # # # # Initialize global variables
# # # # # # root = tk.Tk()
# # # # # # inventory_data = {}  # This will be populated from the database
# # # # # # history = []
# # # # # # is_admin = False

# # # # # # # Initialize the SQLite database
# # # # # # def init_db():
# # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # #     cursor = conn.cursor()

# # # # # #     # Create Inventory Table
# # # # # #     cursor.execute('''
# # # # # #     CREATE TABLE IF NOT EXISTS inventory (
# # # # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # # # #         item_name TEXT NOT NULL,
# # # # # #         price REAL NOT NULL
# # # # # #     )
# # # # # #     ''')

# # # # # #     # Insert sample inventory data if the table is empty
# # # # # #     cursor.execute("SELECT COUNT(*) FROM inventory")
# # # # # #     if cursor.fetchone()[0] == 0:  # If table is empty
# # # # # #         sample_data = [
# # # # # #             ("M.s Pipe", 10.99),
# # # # # #             ("Electrode", 12.49),
# # # # # #             ("Grinding Machine", 8.75),
# # # # # #             ("Welding Machine", 15.00),
# # # # # #             ("Try Square", 5.50),
# # # # # #             ("Thread", 2.25),
# # # # # #             ("Power Saw", 75.00),
# # # # # #             ("Sand Paper", 1.50),
# # # # # #             ("Measuring Tape", 6.00),
# # # # # #             ("Welding Machine (BEME)", 15.00),
# # # # # #             ("Oxy-Acetylene Sets", 50.00),
# # # # # #             ("Power Saw (BEME)", 75.00),
# # # # # #             ("Drilling Machine", 45.00),
# # # # # #             ("Hand Drilling Machine", 25.00),
# # # # # #             ("Grinding Machine (BEME)", 8.75),
# # # # # #             ("Monitor", 120.00),
# # # # # #             ("Projector", 300.00),
# # # # # #             ("Marker Pen", 1.00),
# # # # # #             ("Extension Code", 20.00)
# # # # # #         ]
# # # # # #         cursor.executemany("INSERT INTO inventory (item_name, price) VALUES (?, ?)", sample_data)

# # # # # #     conn.commit()
# # # # # #     conn.close()

# # # # # # # Load inventory data from the database
# # # # # # def load_inventory_data():
# # # # # #     global inventory_data
# # # # # #     conn = sqlite3.connect('inventory.db')
# # # # # #     cursor = conn.cursor()

# # # # # #     cursor.execute("SELECT item_name, price FROM inventory")
# # # # # #     inventory_data = {item[0]: item[1] for item in cursor.fetchall()}
# # # # # #     conn.close()

# # # # # # # Clear the frame function
# # # # # # def clear_frame():
# # # # # #     for widget in root.winfo_children():
# # # # # #         widget.destroy()

# # # # # # # Admin Login Page
# # # # # # def admin_login_page():
# # # # # #     clear_frame()
# # # # # #     history.append(admin_login_page)
# # # # # #     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # #     tk.Label(root, text="Email").pack()
# # # # # #     email_entry = tk.Entry(root)
# # # # # #     email_entry.pack(pady=5)

# # # # # #     tk.Label(root, text="Password").pack()
# # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # #     password_entry.pack(pady=5)

# # # # # #     def login():
# # # # # #         global is_admin
# # # # # #         if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
# # # # # #             is_admin = True  # Set as admin
# # # # # #             inventory_status_page()
# # # # # #         else:
# # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # User Login Page
# # # # # # def user_login_page():
# # # # # #     clear_frame()
# # # # # #     history.append(user_login_page)
# # # # # #     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # # #     tk.Label(root, text="Username").pack()
# # # # # #     username_entry = tk.Entry(root)
# # # # # #     username_entry.pack(pady=5)

# # # # # #     tk.Label(root, text="Password").pack()
# # # # # #     password_entry = tk.Entry(root, show="*")
# # # # # #     password_entry.pack(pady=5)

# # # # # #     def login():
# # # # # #         global is_admin
# # # # # #         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
# # # # # #             is_admin = False  # Set as user
# # # # # #             user_view_department()
# # # # # #         else:
# # # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # # User View - Departments Only
# # # # # # def user_view_department():
# # # # # #     clear_frame()
# # # # # #     history.append(user_view_department)
# # # # # #     tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # #     for dept in departments:
# # # # # #         tk.Button(root, text=dept, command=lambda d=dept: show_prices_in_tabular(d)).pack(pady=5)

# # # # # #     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# # # # # # # Show Prices in Tabular Form
# # # # # # def show_prices_in_tabular(department):
# # # # # #     clear_frame()
# # # # # #     tk.Label(root, text=f"Price List for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # #     # Create a Treeview to display the prices in a tabular format
# # # # # #     tree = ttk.Treeview(root, columns=("Item", "Price"), show='headings')
# # # # # #     tree.heading("Item", text="Item")
# # # # # #     tree.heading("Price", text="Price")

# # # # # #     # Data for the different departments
# # # # # #     items = []
# # # # # #     if department == "BEPE":
# # # # # #         items = [
# # # # # #             ("M.s Pipe", "$10.99"),
# # # # # #             ("Electrode", "$12.49"),
# # # # # #             ("Grinding Machine", "$8.75"),
# # # # # #             ("Welding Machine", "$15.00"),
# # # # # #             ("Try Square", "$5.50"),
# # # # # #             ("Thread", "$2.25"),
# # # # # #             ("Power Saw", "$75.00"),
# # # # # #             ("Sand Paper", "$1.50"),
# # # # # #             ("Measuring Tape", "$6.00")
# # # # # #         ]
# # # # # #     elif department == "BEME":
# # # # # #         items = [
# # # # # #             ("Welding Machine", "$15.00"),
# # # # # #             ("Oxy-Acetylene Sets", "$50.00"),
# # # # # #             ("Power Saw", "$75.00"),
# # # # # #             ("Drilling Machine", "$45.00"),
# # # # # #             ("Hand Drilling Machine", "$25.00"),
# # # # # #             ("Grinding Machine", "$8.75")
# # # # # #         ]
# # # # # #     else:  # CSN
# # # # # #         items = [
# # # # # #             ("Monitor", "$120.00"),
# # # # # #             ("Projector", "$300.00"),
# # # # # #             ("Marker Pen", "$1.00"),
# # # # # #             ("Extension Code", "$20.00")
# # # # # #         ]

# # # # # #     # Insert items into the Treeview
# # # # # #     for item in items:
# # # # # #         tree.insert("", "end", values=item)

# # # # # #     tree.pack(pady=10)

# # # # # #     # Add a back button to return to the departments list
# # # # # #     tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)

# # # # # # # Inventory Status Page (Admin)
# # # # # # def inventory_status_page():
# # # # # #     clear_frame()
# # # # # #     history.append(inventory_status_page)
# # # # # #     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # #     tk.Button(root, text="Department", command=department_list_page).pack(pady=5)
# # # # # #     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# # # # # # # Update Inventory Page (Admin)
# # # # # # def update_inventory_page():
# # # # # #     clear_frame()
# # # # # #     history.append(update_inventory_page)
# # # # # #     tk.Label(root, text="Update Inventory", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # #     item_name_label = tk.Label(root, text="Item Name")
# # # # # #     item_name_label.pack(pady=5)
# # # # # #     item_name_entry = tk.Entry(root)
# # # # # #     item_name_entry.pack(pady=5)

# # # # # #     price_label = tk.Label(root, text="New Price")
# # # # # #     price_label.pack(pady=5)
# # # # # #     price_entry = tk.Entry(root)
# # # # # #     price_entry.pack(pady=5)

# # # # # #     def update_item():
# # # # # #         item_name = item_name_entry.get().strip()
# # # # # #         new_price = price_entry.get().strip()

# # # # # #         # Check if item exists in a case-insensitive way
# # # # # #         normalized_inventory = {k.lower(): v for k, v in inventory_data.items()}
# # # # # #         item_key = item_name.lower()

# # # # # #         if item_key in normalized_inventory and new_price.replace('.', '', 1).isdigit():
# # # # # #             new_price = float(new_price)
# # # # # #             conn = sqlite3.connect('inventory.db')
# # # # # #             cursor = conn.cursor()
# # # # # #             cursor.execute("UPDATE inventory SET price = ? WHERE item_name = ?", (new_price, item_name))
# # # # # #             conn.commit()
# # # # # #             conn.close()
# # # # # #             messagebox.showinfo("Success", f"Updated '{item_name}' to ${new_price:.2f}")
# # # # # #             load_inventory_data()  # Reload inventory data
# # # # # #         else:
# # # # # #             if item_key not in normalized_inventory:
# # # # # #                 messagebox.showerror("Error", "Item name does not exist.")
# # # # # #             else:
# # # # # #                 messagebox.showerror("Error", "Invalid price. Please enter a valid numeric value.")

# # # # # #     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
# # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # # # # Department List Page (Admin)
# # # # # # def department_list_page():
# # # # # #     clear_frame()
# # # # # #     history.append(department_list_page)
# # # # # #     tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # # #     # Example departments
# # # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # # #     for dept in departments:
# # # # # #         tk.Button(root, text=dept, command=lambda d=dept: show_prices_in_tabular(d)).pack(pady=10)

# # # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # # # # Start with Admin/User Login Options
# # # # # # def get_started_page():
# # # # # #     clear_frame()
# # # # # #     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
# # # # # #     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
# # # # # #     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# # # # # # # Call the init_db to create the database and load data
# # # # # # init_db()
# # # # # # load_inventory_data()

# # # # # # # Call the get started page to initiate
# # # # # # get_started_page()
# # # # # # root.mainloop()

# # # # # import tkinter as tk
# # # # # from tkinter import messagebox
# # # # # from tkinter import ttk
# # # # # import sqlite3

# # # # # # Initialize global variables
# # # # # root = tk.Tk()
# # # # # inventory_data = {}  # This will be populated from the database
# # # # # history = []
# # # # # is_admin = False

# # # # # # Initialize the SQLite database
# # # # # def init_db():
# # # # #     conn = sqlite3.connect('inventory.db')
# # # # #     cursor = conn.cursor()

# # # # #     # Create Inventory Table
# # # # #     cursor.execute('''
# # # # #     CREATE TABLE IF NOT EXISTS inventory (
# # # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # # #         item_name TEXT NOT NULL,
# # # # #         price REAL NOT NULL
# # # # #     )
# # # # #     ''')

# # # # #     # Insert sample inventory data if the table is empty
# # # # #     cursor.execute("SELECT COUNT(*) FROM inventory")
# # # # #     if cursor.fetchone()[0] == 0:  # If table is empty
# # # # #         sample_data = [
# # # # #             ("M.s Pipe", 10.99),
# # # # #             ("Electrode", 12.49),
# # # # #             ("Grinding Machine", 8.75),
# # # # #             ("Welding Machine", 15.00),
# # # # #             ("Try Square", 5.50),
# # # # #             ("Thread", 2.25),
# # # # #             ("Power Saw", 75.00),
# # # # #             ("Sand Paper", 1.50),
# # # # #             ("Measuring Tape", 6.00),
# # # # #             ("Welding Machine (BEME)", 15.00),
# # # # #             ("Oxy-Acetylene Sets", 50.00),
# # # # #             ("Power Saw (BEME)", 75.00),
# # # # #             ("Drilling Machine", 45.00),
# # # # #             ("Hand Drilling Machine", 25.00),
# # # # #             ("Grinding Machine (BEME)", 8.75),
# # # # #             ("Monitor", 120.00),
# # # # #             ("Projector", 300.00),
# # # # #             ("Marker Pen", 1.00),
# # # # #             ("Extension Code", 20.00)
# # # # #         ]
# # # # #         cursor.executemany("INSERT INTO inventory (item_name, price) VALUES (?, ?)", sample_data)

# # # # #     conn.commit()
# # # # #     conn.close()

# # # # # # Load inventory data from the database
# # # # # def load_inventory_data():
# # # # #     global inventory_data
# # # # #     conn = sqlite3.connect('inventory.db')
# # # # #     cursor = conn.cursor()

# # # # #     cursor.execute("SELECT item_name, price FROM inventory")
# # # # #     inventory_data = {item[0]: item[1] for item in cursor.fetchall()}
# # # # #     conn.close()

# # # # # # Clear the frame function
# # # # # def clear_frame():
# # # # #     for widget in root.winfo_children():
# # # # #         widget.destroy()

# # # # # # Admin Login Page
# # # # # def admin_login_page():
# # # # #     clear_frame()
# # # # #     history.append(admin_login_page)
# # # # #     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # #     tk.Label(root, text="Email").pack()
# # # # #     email_entry = tk.Entry(root)
# # # # #     email_entry.pack(pady=5)

# # # # #     tk.Label(root, text="Password").pack()
# # # # #     password_entry = tk.Entry(root, show="*")
# # # # #     password_entry.pack(pady=5)

# # # # #     def login():
# # # # #         global is_admin
# # # # #         if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
# # # # #             is_admin = True  # Set as admin
# # # # #             inventory_status_page()
# # # # #         else:
# # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # User Login Page
# # # # # def user_login_page():
# # # # #     clear_frame()
# # # # #     history.append(user_login_page)
# # # # #     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # #     tk.Label(root, text="Username").pack()
# # # # #     username_entry = tk.Entry(root)
# # # # #     username_entry.pack(pady=5)

# # # # #     tk.Label(root, text="Password").pack()
# # # # #     password_entry = tk.Entry(root, show="*")
# # # # #     password_entry.pack(pady=5)

# # # # #     def login():
# # # # #         global is_admin
# # # # #         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
# # # # #             is_admin = False  # Set as user
# # # # #             user_view_department()
# # # # #         else:
# # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # User View - Departments Only
# # # # # def user_view_department():
# # # # #     clear_frame()
# # # # #     history.append(user_view_department)
# # # # #     tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # #     for dept in departments:
# # # # #         tk.Button(root, text=dept, command=lambda d=dept: show_prices_in_tabular(d)).pack(pady=5)

# # # # #     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# # # # # # Show Prices in Tabular Form
# # # # # def show_prices_in_tabular(department):
# # # # #     clear_frame()
# # # # #     tk.Label(root, text=f"Price List for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # #     # Create a Treeview to display the prices in a tabular format
# # # # #     tree = ttk.Treeview(root, columns=("Item", "Price"), show='headings')
# # # # #     tree.heading("Item", text="Item")
# # # # #     tree.heading("Price", text="Price")

# # # # #     # Data for the different departments
# # # # #     items = []
# # # # #     if department == "BEPE":
# # # # #         items = [
# # # # #             ("M.s Pipe", "$10.99"),
# # # # #             ("Electrode", "$12.49"),
# # # # #             ("Grinding Machine", "$8.75"),
# # # # #             ("Welding Machine", "$15.00"),
# # # # #             ("Try Square", "$5.50"),
# # # # #             ("Thread", "$2.25"),
# # # # #             ("Power Saw", "$75.00"),
# # # # #             ("Sand Paper", "$1.50"),
# # # # #             ("Measuring Tape", "$6.00")
# # # # #         ]
# # # # #     elif department == "BEME":
# # # # #         items = [
# # # # #             ("Welding Machine", "$15.00"),
# # # # #             ("Oxy-Acetylene Sets", "$50.00"),
# # # # #             ("Power Saw", "$75.00"),
# # # # #             ("Drilling Machine", "$45.00"),
# # # # #             ("Hand Drilling Machine", "$25.00"),
# # # # #             ("Grinding Machine", "$8.75")
# # # # #         ]
# # # # #     else:  # CSN
# # # # #         items = [
# # # # #             ("Monitor", "$120.00"),
# # # # #             ("Projector", "$300.00"),
# # # # #             ("Marker Pen", "$1.00"),
# # # # #             ("Extension Code", "$20.00")
# # # # #         ]

# # # # #     # Insert items into the Treeview
# # # # #     for item in items:
# # # # #         tree.insert("", "end", values=item)

# # # # #     tree.pack(pady=10)

# # # # #     # Add a back button to return to the departments list
# # # # #     tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)

# # # # # # Inventory Status Page (Admin)
# # # # # def inventory_status_page():
# # # # #     clear_frame()
# # # # #     history.append(inventory_status_page)
# # # # #     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # #     tk.Button(root, text="Update Inventory", command=update_inventory_page).pack(pady=5)
# # # # #     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# # # # # # Update Inventory Page (Admin)
# # # # # def update_inventory_page():
# # # # #     clear_frame()
# # # # #     history.append(update_inventory_page)
# # # # #     tk.Label(root, text="Update Item Price", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # #     tk.Label(root, text="Select Item").pack(pady=5)
    
# # # # #     item_name_var = tk.StringVar()
    
# # # # #     item_combobox = ttk.Combobox(root, textvariable=item_name_var)
# # # # #     item_combobox['values'] = list(inventory_data.keys())  # Populate with item names
# # # # #     item_combobox.pack(pady=5)
    
# # # # #     tk.Label(root, text="New Price").pack(pady=5)
# # # # #     price_entry = tk.Entry(root)
# # # # #     price_entry.pack(pady=5)

# # # # #     def update_item():
# # # # #         item_name = item_name_var.get().strip()
# # # # #         new_price = price_entry.get().strip()

# # # # #         if item_name in inventory_data and new_price.replace('.', '', 1).isdigit():
# # # # #             new_price = float(new_price)
# # # # #             conn = sqlite3.connect('inventory.db')
# # # # #             cursor = conn.cursor()
# # # # #             cursor.execute("UPDATE inventory SET price = ? WHERE item_name = ?", (new_price, item_name))
# # # # #             conn.commit()
# # # # #             conn.close()
# # # # #             messagebox.showinfo("Success", f"Updated '{item_name}' to ${new_price:.2f}")
# # # # #             load_inventory_data()  # Reload inventory data
# # # # #         else:
# # # # #             if item_name not in inventory_data:
# # # # #                 messagebox.showerror("Error", "Item name does not exist.")
# # # # #             else:
# # # # #                 messagebox.showerror("Error", "Invalid price. Please enter a valid numeric value.")

# # # # #     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
# # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # # # Start with Admin/User Login Options
# # # # # def get_started_page():
# # # # #     clear_frame()
# # # # #     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
# # # # #     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
# # # # #     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# # # # # # Call the init_db to create the database and load data
# # # # # init_db()
# # # # # load_inventory_data()

# # # # # # Call the get started page to initiate
# # # # # get_started_page()
# # # # # root.mainloop()

# # # # # import tkinter as tk
# # # # # from tkinter import messagebox
# # # # # from tkinter import ttk
# # # # # import sqlite3

# # # # # # Initialize global variables
# # # # # root = tk.Tk()
# # # # # inventory_data = {}  # This will be populated from the database
# # # # # history = []
# # # # # is_admin = False

# # # # # # Initialize the SQLite database
# # # # # def init_db():
# # # # #     conn = sqlite3.connect('inventory.db')
# # # # #     cursor = conn.cursor()

# # # # #     # Create Inventory Table
# # # # #     cursor.execute('''
# # # # #     CREATE TABLE IF NOT EXISTS inventory (
# # # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # # #         item_name TEXT NOT NULL,
# # # # #         price REAL NOT NULL
# # # # #     )
# # # # #     ''')

# # # # #     # Insert sample inventory data if the table is empty
# # # # #     cursor.execute("SELECT COUNT(*) FROM inventory")
# # # # #     if cursor.fetchone()[0] == 0:  # If table is empty
# # # # #         sample_data = [
# # # # #             ("M.s Pipe", 10.99),
# # # # #             ("Electrode", 12.49),
# # # # #             ("Grinding Machine", 8.75),
# # # # #             ("Welding Machine", 15.00),
# # # # #             ("Try Square", 5.50),
# # # # #             ("Thread", 2.25),
# # # # #             ("Power Saw", 75.00),
# # # # #             ("Sand Paper", 1.50),
# # # # #             ("Measuring Tape", 6.00),
# # # # #             ("Welding Machine (BEME)", 15.00),
# # # # #             ("Oxy-Acetylene Sets", 50.00),
# # # # #             ("Power Saw (BEME)", 75.00),
# # # # #             ("Drilling Machine", 45.00),
# # # # #             ("Hand Drilling Machine", 25.00),
# # # # #             ("Grinding Machine (BEME)", 8.75),
# # # # #             ("Monitor", 120.00),
# # # # #             ("Projector", 300.00),
# # # # #             ("Marker Pen", 1.00),
# # # # #             ("Extension Code", 20.00)
# # # # #         ]
# # # # #         cursor.executemany("INSERT INTO inventory (item_name, price) VALUES (?, ?)", sample_data)

# # # # #     conn.commit()
# # # # #     conn.close()

# # # # # # Load inventory data from the database
# # # # # def load_inventory_data():
# # # # #     global inventory_data
# # # # #     conn = sqlite3.connect('inventory.db')
# # # # #     cursor = conn.cursor()

# # # # #     cursor.execute("SELECT item_name, price FROM inventory")
# # # # #     inventory_data = {item[0]: item[1] for item in cursor.fetchall()}
# # # # #     conn.close()

# # # # # # Clear the frame function
# # # # # def clear_frame():
# # # # #     for widget in root.winfo_children():
# # # # #         widget.destroy()

# # # # # # Admin Login Page
# # # # # def admin_login_page():
# # # # #     clear_frame()
# # # # #     history.append(admin_login_page)
# # # # #     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # #     tk.Label(root, text="Email").pack()
# # # # #     email_entry = tk.Entry(root)
# # # # #     email_entry.pack(pady=5)

# # # # #     tk.Label(root, text="Password").pack()
# # # # #     password_entry = tk.Entry(root, show="*")
# # # # #     password_entry.pack(pady=5)

# # # # #     def login():
# # # # #         global is_admin
# # # # #         if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
# # # # #             is_admin = True  # Set as admin
# # # # #             inventory_status_page()
# # # # #         else:
# # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # User Login Page
# # # # # def user_login_page():
# # # # #     clear_frame()
# # # # #     history.append(user_login_page)
# # # # #     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # # # #     tk.Label(root, text="Username").pack()
# # # # #     username_entry = tk.Entry(root)
# # # # #     username_entry.pack(pady=5)

# # # # #     tk.Label(root, text="Password").pack()
# # # # #     password_entry = tk.Entry(root, show="*")
# # # # #     password_entry.pack(pady=5)

# # # # #     def login():
# # # # #         global is_admin
# # # # #         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
# # # # #             is_admin = False  # Set as user
# # # # #             user_view_department()
# # # # #         else:
# # # # #             messagebox.showerror("Error", "Invalid credentials")

# # # # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # # # Admin Inventory Status Page
# # # # # def inventory_status_page():
# # # # #     clear_frame()
# # # # #     history.append(inventory_status_page)
# # # # #     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # #     tk.Button(root, text="Department List", command=department_list_page).pack(pady=5)
# # # # #     tk.Button(root, text="Update Inventory", command=update_inventory_page).pack(pady=5)
# # # # #     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# # # # # # User View - Departments Only
# # # # # def user_view_department():
# # # # #     clear_frame()
# # # # #     history.append(user_view_department)
# # # # #     tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # #     for dept in departments:
# # # # #         tk.Button(root, text=dept, command=lambda d=dept: show_prices_in_tabular(d)).pack(pady=5)

# # # # #     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# # # # # # Show Prices in Tabular Form
# # # # # def show_prices_in_tabular(department):
# # # # #     clear_frame()
# # # # #     tk.Label(root, text=f"Price List for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # #     # Create a Treeview to display the prices in a tabular format
# # # # #     tree = ttk.Treeview(root, columns=("Item", "Price"), show='headings')
# # # # #     tree.heading("Item", text="Item")
# # # # #     tree.heading("Price", text="Price")

# # # # #     # Data for the different departments
# # # # #     items = []
# # # # #     if department == "BEPE":
# # # # #         items = [
# # # # #             ("M.s Pipe", "$10.99"),
# # # # #             ("Electrode", "$12.49"),
# # # # #             ("Grinding Machine", "$8.75"),
# # # # #             ("Welding Machine", "$15.00"),
# # # # #             ("Try Square", "$5.50"),
# # # # #             ("Thread", "$2.25"),
# # # # #             ("Power Saw", "$75.00"),
# # # # #             ("Sand Paper", "$1.50"),
# # # # #             ("Measuring Tape", "$6.00")
# # # # #         ]
# # # # #     elif department == "BEME":
# # # # #         items = [
# # # # #             ("Welding Machine", "$15.00"),
# # # # #             ("Oxy-Acetylene Sets", "$50.00"),
# # # # #             ("Power Saw", "$75.00"),
# # # # #             ("Drilling Machine", "$45.00"),
# # # # #             ("Hand Drilling Machine", "$25.00"),
# # # # #             ("Grinding Machine", "$8.75")
# # # # #         ]
# # # # #     else:  # CSN
# # # # #         items = [
# # # # #             ("Monitor", "$120.00"),
# # # # #             ("Projector", "$300.00"),
# # # # #             ("Marker Pen", "$1.00"),
# # # # #             ("Extension Code", "$20.00")
# # # # #         ]

# # # # #     # Insert items into the Treeview
# # # # #     for item in items:
# # # # #         tree.insert("", "end", values=item)

# # # # #     tree.pack(pady=10)

# # # # #     # Add a back button to return to the departments list
# # # # #     tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)

# # # # # # Update Inventory Page (Admin)
# # # # # def update_inventory_page():
# # # # #     clear_frame()
# # # # #     history.append(update_inventory_page)
# # # # #     tk.Label(root, text="Update Item Price", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # #     tk.Label(root, text="Select Item").pack(pady=5)
    
# # # # #     item_name_var = tk.StringVar()
    
# # # # #     item_combobox = ttk.Combobox(root, textvariable=item_name_var)
# # # # #     item_combobox['values'] = list(inventory_data.keys())  # Populate with item names
# # # # #     item_combobox.pack(pady=5)
    
# # # # #     tk.Label(root, text="New Price").pack(pady=5)
# # # # #     price_entry = tk.Entry(root)
# # # # #     price_entry.pack(pady=5)

# # # # #     def update_item():
# # # # #         item_name = item_name_var.get().strip()
# # # # #         new_price = price_entry.get().strip()

# # # # #         if item_name in inventory_data and new_price.replace('.', '', 1).isdigit():
# # # # #             new_price = float(new_price)
# # # # #             conn = sqlite3.connect('inventory.db')
# # # # #             cursor = conn.cursor()
# # # # #             cursor.execute("UPDATE inventory SET price = ? WHERE item_name = ?", (new_price, item_name))
# # # # #             conn.commit()
# # # # #             conn.close()
# # # # #             messagebox.showinfo("Success", f"Updated '{item_name}' to ${new_price:.2f}")
# # # # #             load_inventory_data()  # Reload inventory data
# # # # #         else:
# # # # #             if item_name not in inventory_data:
# # # # #                 messagebox.showerror("Error", "Item name does not exist.")
# # # # #             else:
# # # # #                 messagebox.showerror("Error", "Invalid price. Please enter a valid numeric value.")

# # # # #     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
# # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # # # Department List Page (Admin)
# # # # # def department_list_page():
# # # # #     clear_frame()
# # # # #     history.append(department_list_page)
# # # # #     tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # # # #     departments = ["BEPE", "BEME", "CSN"]
# # # # #     for dept in departments:
# # # # #         tk.Button(root, text=dept, command=lambda d=dept: show_prices_in_tabular(d)).pack(pady=10)

# # # # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # # # Start with Admin/User Login Options
# # # # # def get_started_page():
# # # # #     clear_frame()
# # # # #     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
# # # # #     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
# # # # #     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# # # # # # Call the init_db to create the database and load data
# # # # # init_db()
# # # # # load_inventory_data()

# # # # # # Call the get started page to initiate
# # # # # get_started_page()
# # # # # root.mainloop()

# # # import tkinter as tk
# # # from tkinter import messagebox
# # # from tkinter import ttk
# # # import sqlite3

# # # # Initialize global variables
# # # root = tk.Tk()
# # # inventory_data = {}  # This will be populated from the database
# # # history = []
# # # is_admin = False

# # # # Initialize the SQLite database
# # # def init_db():
# # #     conn = sqlite3.connect('inventory.db')
# # #     cursor = conn.cursor()

# # #     # Create Inventory Table
# # #     cursor.execute('''
# # #     CREATE TABLE IF NOT EXISTS inventory (
# # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #         item_name TEXT NOT NULL,
# # #         price REAL NOT NULL
# # #     )
# # #     ''')

# # #     # Insert sample inventory data if the table is empty
# # #     cursor.execute("SELECT COUNT(*) FROM inventory")
# # #     if cursor.fetchone()[0] == 0:  # If table is empty
# # #         sample_data = [
# # #             ("M.s Pipe", 10.99),
# # #             ("Electrode", 12.49),
# # #             ("Grinding Machine", 8.75),
# # #             ("Welding Machine", 15.00),
# # #             ("Try Square", 5.50),
# # #             ("Thread", 2.25),
# # #             ("Power Saw", 75.00),
# # #             ("Sand Paper", 1.50),
# # #             ("Measuring Tape", 6.00),
# # #             ("Welding Machine (BEME)", 15.00),
# # #             ("Oxy-Acetylene Sets", 50.00),
# # #             ("Power Saw (BEME)", 75.00),
# # #             ("Drilling Machine", 45.00),
# # #             ("Hand Drilling Machine", 25.00),
# # #             ("Grinding Machine (BEME)", 8.75),
# # #             ("Monitor", 120.00),
# # #             ("Projector", 300.00),
# # #             ("Marker Pen", 1.00),
# # #             ("Extension Code", 20.00)
# # #         ]
# # #         cursor.executemany("INSERT INTO inventory (item_name, price) VALUES (?, ?)", sample_data)

# # #     conn.commit()
# # #     conn.close()

# # # # Load inventory data from the database
# # # def load_inventory_data():
# # #     global inventory_data
# # #     conn = sqlite3.connect('inventory.db')
# # #     cursor = conn.cursor()

# # #     cursor.execute("SELECT item_name, price FROM inventory")
# # #     inventory_data = {item[0]: item[1] for item in cursor.fetchall()}
# # #     conn.close()

# # # # Clear the frame function
# # # def clear_frame():
# # #     for widget in root.winfo_children():
# # #         widget.destroy()

# # # # Admin Login Page
# # # def admin_login_page():
# # #     clear_frame()
# # #     history.append(admin_login_page)
# # #     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # #     tk.Label(root, text="Email").pack()
# # #     email_entry = tk.Entry(root)
# # #     email_entry.pack(pady=5)

# # #     tk.Label(root, text="Password").pack()
# # #     password_entry = tk.Entry(root, show="*")
# # #     password_entry.pack(pady=5)

# # #     def login():
# # #         global is_admin
# # #         if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
# # #             is_admin = True  # Set as admin
# # #             inventory_status_page()
# # #         else:
# # #             messagebox.showerror("Error", "Invalid credentials")

# # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # User Login Page
# # # def user_login_page():
# # #     clear_frame()
# # #     history.append(user_login_page)
# # #     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# # #     tk.Label(root, text="Username").pack()
# # #     username_entry = tk.Entry(root)
# # #     username_entry.pack(pady=5)

# # #     tk.Label(root, text="Password").pack()
# # #     password_entry = tk.Entry(root, show="*")
# # #     password_entry.pack(pady=5)

# # #     def login():
# # #         global is_admin
# # #         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
# # #             is_admin = False  # Set as user
# # #             user_view_department()
# # #         else:
# # #             messagebox.showerror("Error", "Invalid credentials")

# # #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # # Admin Inventory Status Page
# # # def inventory_status_page():
# # #     clear_frame()
# # #     history.append(inventory_status_page)
# # #     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # #     tk.Button(root, text="Department List", command=department_list_page).pack(pady=5)
# # #     tk.Button(root, text="Update Inventory", command=update_inventory_page).pack(pady=5)
# # #     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# # # # User View - Departments Only
# # # def user_view_department():
# # #     clear_frame()
# # #     history.append(user_view_department)
# # #     tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # #     departments = ["BEPE", "BEME", "CSN"]
# # #     for dept in departments:
# # #         tk.Button(root, text=dept, command=lambda d=dept: show_prices_in_tabular(d)).pack(pady=5)

# # #     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# # # # Show Prices in Tabular Form
# # # def show_prices_in_tabular(department):
# # #     clear_frame()
# # #     tk.Label(root, text=f"Price List for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # #     # Create a Treeview to display the prices in a tabular format
# # #     tree = ttk.Treeview(root, columns=("Item", "Price"), show='headings')
# # #     tree.heading("Item", text="Item")
# # #     tree.heading("Price", text="Price")

# # #     # Data for the different departments
# # #     items = []
# # #     if department == "BEPE":
# # #         items = [
# # #             ("M.s Pipe", "$10.99"),
# # #             ("Electrode", "$12.49"),
# # #             ("Grinding Machine", "$8.75"),
# # #             ("Welding Machine", "$15.00"),
# # #             ("Try Square", "$5.50"),
# # #             ("Thread", "$2.25"),
# # #             ("Power Saw", "$75.00"),
# # #             ("Sand Paper", "$1.50"),
# # #             ("Measuring Tape", "$6.00")
# # #         ]
# # #     elif department == "BEME":
# # #         items = [
# # #             ("Welding Machine", "$15.00"),
# # #             ("Oxy-Acetylene Sets", "$50.00"),
# # #             ("Power Saw", "$75.00"),
# # #             ("Drilling Machine", "$45.00"),
# # #             ("Hand Drilling Machine", "$25.00"),
# # #             ("Grinding Machine", "$8.75")
# # #         ]
# # #     else:  # CSN
# # #         items = [
# # #             ("Monitor", "$120.00"),
# # #             ("Projector", "$300.00"),
# # #             ("Marker Pen", "$1.00"),
# # #             ("Extension Code", "$20.00")
# # #         ]

# # #     # Insert items into the Treeview
# # #     for item in items:
# # #         tree.insert("", "end", values=item)

# # #     tree.pack(pady=10)

# # #     # Add a back button to return to the departments list
# # #     tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)

# # # # Update Inventory Page (Admin)
# # # def update_inventory_page():
# # #     clear_frame()
# # #     history.append(update_inventory_page)
# # #     tk.Label(root, text="Update Item Price", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # #     tk.Label(root, text="Select Item").pack(pady=5)
    
# # #     item_name_var = tk.StringVar()
    
# # #     item_combobox = ttk.Combobox(root, textvariable=item_name_var)
# # #     item_combobox['values'] = list(inventory_data.keys())  # Populate with item names
# # #     item_combobox.pack(pady=5)
    
# # #     tk.Label(root, text="New Price").pack(pady=5)
# # #     price_entry = tk.Entry(root)
# # #     price_entry.pack(pady=5)

# # #     def update_item():
# # #         item_name = item_name_var.get().strip()
# # #         new_price = price_entry.get().strip()

# # #         if item_name in inventory_data and new_price.replace('.', '', 1).isdigit():
# # #             new_price = float(new_price)
# # #             conn = sqlite3.connect('inventory.db')
# # #             cursor = conn.cursor()
# # #             cursor.execute("UPDATE inventory SET price = ? WHERE item_name = ?", (new_price, item_name))
# # #             conn.commit()
# # #             conn.close()
# # #             messagebox.showinfo("Success", f"Updated '{item_name}' to ${new_price:.2f}")
# # #             load_inventory_data()  # Reload inventory data
# # #         else:
# # #             if item_name not in inventory_data:
# # #                 messagebox.showerror("Error", "Item name does not exist.")
# # #             else:
# # #                 messagebox.showerror("Error", "Invalid price. Please enter a valid numeric value.")

# # #     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
# # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # Department List Page (Admin)
# # # def department_list_page():
# # #     clear_frame()
# # #     history.append(department_list_page)
# # #     tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

# # #     departments = ["BEPE", "BEME", "CSN"]
# # #     for dept in departments:
# # #         tk.Button(root, text=dept, command=lambda d=dept: show_prices_in_tabular(d)).pack(pady=10)

# # #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # # Start with Admin/User Login Options
# # # def get_started_page():
# # #     clear_frame()
# # #     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
# # #     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
# # #     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# # # # Call the init_db to create the database and load data
# # # init_db()
# # # load_inventory_data()

# # # # Call the get started page to initiate
# # # get_started_page()
# # # root.mainloop()

# # import tkinter as tk
# # from tkinter import messagebox
# # from tkinter import ttk
# # import sqlite3

# # # Initialize global variables
# # root = tk.Tk()
# # inventory_data = {}  # This will be populated from the database
# # history = []
# # is_admin = False

# # # Initialize the SQLite database
# # def init_db():
# #     conn = sqlite3.connect('inventory.db')
# #     cursor = conn.cursor()

# #     # Create Inventory Table with Quantity
# #     cursor.execute('''
# #     CREATE TABLE IF NOT EXISTS inventory (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         item_name TEXT NOT NULL,
# #         price REAL NOT NULL,
# #         quantity INTEGER NOT NULL DEFAULT 0
# #     )
# #     ''')

# #     # Insert sample inventory data if the table is empty
# #     cursor.execute("SELECT COUNT(*) FROM inventory")
# #     if cursor.fetchone()[0] == 0:  # If table is empty
# #         sample_data = [
# #             ("M.s Pipe", 10.99, 100),
# #             ("Electrode", 12.49, 200),
# #             ("Grinding Machine", 8.75, 50),
# #             ("Welding Machine", 15.00, 60),
# #             ("Try Square", 5.50, 150),
# #             ("Thread", 2.25, 300),
# #             ("Power Saw", 75.00, 25),
# #             ("Sand Paper", 1.50, 200),
# #             ("Measuring Tape", 6.00, 80),
# #             ("Welding Machine (BEME)", 15.00, 20),
# #             ("Oxy-Acetylene Sets", 50.00, 15),
# #             ("Power Saw (BEME)", 75.00, 10),
# #             ("Drilling Machine", 45.00, 40),
# #             ("Hand Drilling Machine", 25.00, 50),
# #             ("Grinding Machine (BEME)", 8.75, 30),
# #             ("Monitor", 120.00, 5),
# #             ("Projector", 300.00, 2),
# #             ("Marker Pen", 1.00, 500),
# #             ("Extension Code", 20.00, 100)
# #         ]
# #         cursor.executemany("INSERT INTO inventory (item_name, price, quantity) VALUES (?, ?, ?)", sample_data)

# #     conn.commit()
# #     conn.close()

# # # Load inventory data from the database
# # def load_inventory_data():
# #     global inventory_data
# #     conn = sqlite3.connect('inventory.db')
# #     cursor = conn.cursor()

# #     cursor.execute("SELECT item_name, price, quantity FROM inventory")
# #     inventory_data = {item[0]: {'price': item[1], 'quantity': item[2]} for item in cursor.fetchall()}
# #     conn.close()

# # # Clear the frame function
# # def clear_frame():
# #     for widget in root.winfo_children():
# #         widget.destroy()

# # # Admin Login Page
# # def admin_login_page():
# #     clear_frame()
# #     history.append(admin_login_page)
# #     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# #     tk.Label(root, text="Email").pack()
# #     email_entry = tk.Entry(root)
# #     email_entry.pack(pady=5)

# #     tk.Label(root, text="Password").pack()
# #     password_entry = tk.Entry(root, show="*")
# #     password_entry.pack(pady=5)

# #     def login():
# #         global is_admin
# #         if email_entry.get() == "Kinzang@gmail.com" and password_entry.get() == "kinzang123":
# #             is_admin = True  # Set as admin
# #             inventory_status_page()
# #         else:
# #             messagebox.showerror("Error", "Invalid credentials")

# #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # User Login Page
# # def user_login_page():
# #     clear_frame()
# #     history.append(user_login_page)
# #     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

# #     tk.Label(root, text="Username").pack()
# #     username_entry = tk.Entry(root)
# #     username_entry.pack(pady=5)

# #     tk.Label(root, text="Password").pack()
# #     password_entry = tk.Entry(root, show="*")
# #     password_entry.pack(pady=5)

# #     def login():
# #         global is_admin
# #         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
# #             is_admin = False  # Set as user
# #             user_view_department()
# #         else:
# #             messagebox.showerror("Error", "Invalid credentials")

# #     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # # Admin Inventory Status Page
# # def inventory_status_page():
# #     clear_frame()
# #     history.append(inventory_status_page)
# #     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

# #     tk.Button(root, text="Department List", command=department_list_page).pack(pady=5)
# #     tk.Button(root, text="Update Inventory", command=update_inventory_page).pack(pady=5)
# #     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# # # User View - Departments Only
# # def user_view_department():
# #     clear_frame()
# #     history.append(user_view_department)
# #     tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

# #     departments = ["BEPE", "BEME", "CSN"]
# #     for dept in departments:
# #         tk.Button(root, text=dept, command=lambda d=dept: show_prices_in_tabular(d)).pack(pady=5)

# #     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# # # Show Prices in Tabular Form
# # def show_prices_in_tabular(department):
# #     clear_frame()
# #     tk.Label(root, text=f"Price List for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

# #     # Create a Treeview to display the prices in a tabular format
# #     tree = ttk.Treeview(root, columns=("Item", "Price", "Quantity"), show='headings')
# #     tree.heading("Item", text="Item")
# #     tree.heading("Price", text="Price")
# #     tree.heading("Quantity", text="Quantity")

# #     # Data for the different departments
# #     items = []
# #     if department == "BEPE":
# #         items = [
# #             ("M.s Pipe", "$10.99", inventory_data["M.s Pipe"]['quantity']),
# #             ("Electrode", "$12.49", inventory_data["Electrode"]['quantity']),
# #             ("Grinding Machine", "$8.75", inventory_data["Grinding Machine"]['quantity']),
# #             ("Welding Machine", "$15.00", inventory_data["Welding Machine"]['quantity']),
# #             ("Try Square", "$5.50", inventory_data["Try Square"]['quantity']),
# #             ("Thread", "$2.25", inventory_data["Thread"]['quantity']),
# #             ("Power Saw", "$75.00", inventory_data["Power Saw"]['quantity']),
# #             ("Sand Paper", "$1.50", inventory_data["Sand Paper"]['quantity']),
# #             ("Measuring Tape", "$6.00", inventory_data["Measuring Tape"]['quantity'])
# #         ]
# #     elif department == "BEME":
# #         items = [
# #             ("Welding Machine", "$15.00", inventory_data["Welding Machine"]['quantity']),
# #             ("Oxy-Acetylene Sets", "$50.00", inventory_data["Oxy-Acetylene Sets"]['quantity']),
# #             ("Power Saw", "$75.00", inventory_data["Power Saw"]['quantity']),
# #             ("Drilling Machine", "$45.00", inventory_data["Drilling Machine"]['quantity']),
# #             ("Hand Drilling Machine", "$25.00", inventory_data["Hand Drilling Machine"]['quantity']),
# #             ("Grinding Machine", "$8.75", inventory_data["Grinding Machine"]['quantity'])
# #         ]
# #     else:  # CSN
# #         items = [
# #             ("Monitor", "$120.00", inventory_data["Monitor"]['quantity']),
# #             ("Projector", "$300.00", inventory_data["Projector"]['quantity']),
# #             ("Marker Pen", "$1.00", inventory_data["Marker Pen"]['quantity']),
# #             ("Extension Code", "$20.00", inventory_data["Extension Code"]['quantity'])
# #         ]

# #     # Insert items into the Treeview
# #     for item in items:
# #         tree.insert("", "end", values=item)

# #     tree.pack(pady=10)

# #     # Add a back button to return to the departments list
# #     tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)

# # # Update Inventory Page (Admin)
# # def update_inventory_page():
# #     clear_frame()
# #     history.append(update_inventory_page)
# #     tk.Label(root, text="Update Item Price and Quantity", font=('Helvetica', 18, 'bold')).pack(pady=20)

# #     tk.Label(root, text="Select Item").pack(pady=5)
    
# #     item_name_var = tk.StringVar()
    
# #     item_combobox = ttk.Combobox(root, textvariable=item_name_var)
# #     item_combobox['values'] = list(inventory_data.keys())  # Populate with item names
# #     item_combobox.pack(pady=5)
    
# #     tk.Label(root, text="New Price").pack(pady=5)
# #     price_entry = tk.Entry(root)
# #     price_entry.pack(pady=5)

# #     tk.Label(root, text="New Quantity").pack(pady=5)
# #     quantity_entry = tk.Entry(root)
# #     quantity_entry.pack(pady=5)

# #     def update_item():
# #         item_name = item_name_var.get().strip()
# #         new_price = price_entry.get().strip()
# #         new_quantity = quantity_entry.get().strip()

# #         if item_name in inventory_data and new_price.replace('.', '', 1).isdigit() and new_quantity.isdigit():
# #             new_price = float(new_price)
# #             new_quantity = int(new_quantity)
# #             conn = sqlite3.connect('inventory.db')
# #             cursor = conn.cursor()
# #             cursor.execute("UPDATE inventory SET price = ?, quantity = ? WHERE item_name = ?", (new_price, new_quantity, item_name))
# #             conn.commit()
# #             conn.close()
# #             messagebox.showinfo("Success", f"Updated '{item_name}' to ${new_price:.2f} with quantity {new_quantity}")
# #             load_inventory_data()  # Reload inventory data
# #         else:
# #             if item_name not in inventory_data:
# #                 messagebox.showerror("Error", "Item name does not exist.")
# #             else:
# #                 messagebox.showerror("Error", "Invalid inputs. Please enter valid numeric values.")

# #     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
# #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # Department List Page (Admin)
# # def department_list_page():
# #     clear_frame()
# #     history.append(department_list_page)
# #     tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

# #     departments = ["BEPE", "BEME", "CSN"]
# #     for dept in departments:
# #         tk.Button(root, text=dept, command=lambda d=dept: show_prices_in_tabular(d)).pack(pady=10)

# #     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # # Start with Admin/User Login Options
# # def get_started_page():
# #     clear_frame()
# #     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
# #     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
# #     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# # # Call the init_db to create the database and load data
# # init_db()
# # load_inventory_data()

# # # Call the get started page to initiate
# # get_started_page()
# # root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
# import sqlite3

# # Initialize global variables
# root = tk.Tk()
# inventory_data = {}  # This will be populated from the database
# history = []
# is_admin = False

# # Initialize the SQLite database
# def init_db():
#     conn = sqlite3.connect('inventory.db')
#     cursor = conn.cursor()

#     # Create Inventory Table with Quantity
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS inventory (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         item_name TEXT NOT NULL,
#         price REAL NOT NULL,
#         quantity INTEGER NOT NULL DEFAULT 0
#     )
#     ''')

#     # Insert sample inventory data if the table is empty
#     cursor.execute("SELECT COUNT(*) FROM inventory")
#     if cursor.fetchone()[0] == 0:  # If table is empty
#         sample_data = [
#             ("M.s Pipe", 10.99, 100),
#             ("Electrode", 12.49, 200),
#             ("Grinding Machine", 8.75, 50),
#             ("Welding Machine", 15.00, 60),
#             ("Try Square", 5.50, 150),
#             ("Thread", 2.25, 300),
#             ("Power Saw", 75.00, 25),
#             ("Sand Paper", 1.50, 200),
#             ("Measuring Tape", 6.00, 80),
#             ("Monitor", 120.00, 5),
#             ("Projector", 300.00, 2),
#             ("Marker Pen", 1.00, 500),
#             ("Extension Code", 20.00, 100)
#         ]
#         cursor.executemany("INSERT INTO inventory (item_name, price, quantity) VALUES (?, ?, ?)", sample_data)

#     conn.commit()
#     conn.close()

# # Load inventory data from the database
# def load_inventory_data():
#     global inventory_data
#     conn = sqlite3.connect('inventory.db')
#     cursor = conn.cursor()

#     cursor.execute("SELECT item_name, price, quantity FROM inventory")
#     inventory_data = {item[0]: {'price': item[1], 'quantity': item[2]} for item in cursor.fetchall()}
#     conn.close()

# # Clear the frame function
# def clear_frame():
#     for widget in root.winfo_children():
#         widget.destroy()

# # Admin Login Page
# def admin_login_page():
#     clear_frame()
#     history.append(admin_login_page)
#     tk.Label(root, text="Admin Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

#     tk.Label(root, text="Email").pack()
#     email_entry = tk.Entry(root)
#     email_entry.pack(pady=5)

#     tk.Label(root, text="Password").pack()
#     password_entry = tk.Entry(root, show="*")
#     password_entry.pack(pady=5)

#     def login():
#         global is_admin
#         if email_entry.get() == "admin@example.com" and password_entry.get() == "password123":
#             is_admin = True  # Set as admin
#             inventory_status_page()
#         else:
#             messagebox.showerror("Error", "Invalid credentials")

#     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # User Login Page
# def user_login_page():
#     clear_frame()
#     history.append(user_login_page)
#     tk.Label(root, text="User Login", font=('Helvetica', 18, 'bold')).pack(pady=50)

#     tk.Label(root, text="Username").pack()
#     username_entry = tk.Entry(root)
#     username_entry.pack(pady=5)

#     tk.Label(root, text="Password").pack()
#     password_entry = tk.Entry(root, show="*")
#     password_entry.pack(pady=5)

#     def login():
#         global is_admin
#         if username_entry.get() and password_entry.get():  # Simple check, modify as needed
#             is_admin = False  # Set as user
#             user_view_department()
#         else:
#             messagebox.showerror("Error", "Invalid credentials")

#     tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# # Admin Inventory Status Page
# def inventory_status_page():
#     clear_frame()
#     history.append(inventory_status_page)
#     tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

#     tk.Button(root, text="Update Inventory", command=update_inventory_page).pack(pady=5)
#     tk.Button(root, text="View Inventory", command=view_inventory_page).pack(pady=5)
#     tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# # View Inventory Page (Admin)
# def view_inventory_page():
#     clear_frame()
#     tk.Label(root, text="Current Inventory", font=('Helvetica', 18, 'bold')).pack(pady=20)

#     # Create a Treeview to display the inventory
#     tree = ttk.Treeview(root, columns=("Item", "Price", "Quantity"), show='headings')
#     tree.heading("Item", text="Item")
#     tree.heading("Price", text="Price")
#     tree.heading("Quantity", text="Quantity")

#     # Populate the Treeview with data from the inventory
#     for item_name, item_details in inventory_data.items():
#         tree.insert("", "end", values=(item_name, f"${item_details['price']:.2f}", item_details['quantity']))

#     tree.pack(pady=10)

#     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # User View - Show Inventory
# def user_view_department():
#     clear_frame()
#     tk.Label(root, text="Available Items", font=('Helvetica', 18, 'bold')).pack(pady=20)

#     # Create a Treeview to display the inventory
#     tree = ttk.Treeview(root, columns=("Item", "Price", "Quantity"), show='headings')
#     tree.heading("Item", text="Item")
#     tree.heading("Price", text="Price")
#     tree.heading("Quantity", text="Quantity")

#     # Populate the Treeview with data from the inventory
#     for item_name, item_details in inventory_data.items():
#         tree.insert("", "end", values=(item_name, f"${item_details['price']:.2f}", item_details['quantity']))

#     tree.pack(pady=10)

#     tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# # Update Inventory Page (Admin)
# def update_inventory_page():
#     clear_frame()
#     history.append(update_inventory_page)
#     tk.Label(root, text="Update Item Price and Quantity", font=('Helvetica', 18, 'bold')).pack(pady=20)

#     tk.Label(root, text="Select Item").pack(pady=5)
    
#     item_name_var = tk.StringVar()
    
#     item_combobox = ttk.Combobox(root, textvariable=item_name_var)
#     item_combobox['values'] = list(inventory_data.keys())  # Populate with item names
#     item_combobox.pack(pady=5)

#     tk.Label(root, text="New Price").pack(pady=5)
#     price_entry = tk.Entry(root)
#     price_entry.pack(pady=5)

#     tk.Label(root, text="New Quantity").pack(pady=5)
#     quantity_entry = tk.Entry(root)
#     quantity_entry.pack(pady=5)

#     def update_item():
#         item_name = item_name_var.get().strip()
#         new_price = price_entry.get().strip()
#         new_quantity = quantity_entry.get().strip()

#         if item_name in inventory_data and new_price.replace('.', '', 1).isdigit() and new_quantity.isdigit():
#             new_price = float(new_price)
#             new_quantity = int(new_quantity)
#             conn = sqlite3.connect('inventory.db')
#             cursor = conn.cursor()
#             cursor.execute("UPDATE inventory SET price = ?, quantity = ? WHERE item_name = ?", (new_price, new_quantity, item_name))
#             conn.commit()
#             conn.close()
#             messagebox.showinfo("Success", f"Updated '{item_name}' to ${new_price:.2f} with quantity {new_quantity}")
#             load_inventory_data()  # Reload inventory data
#         else:
#             messagebox.showerror("Error", "Invalid inputs. Please enter valid numeric values.")

#     tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
#     tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# # Start with Admin/User Login Options
# def get_started_page():
#     clear_frame()
#     tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
#     tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
#     tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# # Call the init_db to create the database and load data
# init_db()
# load_inventory_data()

# # Call the get started page to initiate
# get_started_page()
# root.mainloop()

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Initialize global variables
root = tk.Tk()
inventory_data = {}  # This will be populated from the database
history = []
is_admin = False

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Create Inventory Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        price REAL NOT NULL
    )
    ''')

    # Insert sample inventory data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM inventory")
    if cursor.fetchone()[0] == 0:  # If table is empty
        sample_data = [
            ("M.s Pipe", 10.99),
            ("Electrode", 12.49),
            ("Grinding Machine", 8.75),
            ("Welding Machine", 15.00),
            ("Try Square", 5.50),
            ("Thread", 2.25),
            ("Power Saw", 75.00),
            ("Sand Paper", 1.50),
            ("Measuring Tape", 6.00),
            ("Welding Machine (BEME)", 15.00),
            ("Oxy-Acetylene Sets", 50.00),
            ("Power Saw (BEME)", 75.00),
            ("Drilling Machine", 45.00),
            ("Hand Drilling Machine", 25.00),
            ("Grinding Machine (BEME)", 8.75),
            ("Monitor", 120.00),
            ("Projector", 300.00),
            ("Marker Pen", 1.00),
            ("Extension Code", 20.00)
        ]
        cursor.executemany("INSERT INTO inventory (item_name, price) VALUES (?, ?)", sample_data)

    conn.commit()
    conn.close()

# Load inventory data from the database
def load_inventory_data():
    global inventory_data
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    cursor.execute("SELECT item_name, price FROM inventory")
    inventory_data = {item[0]: item[1] for item in cursor.fetchall()}
    conn.close()

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
            user_view_department()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# Admin Inventory Status Page
def inventory_status_page():
    clear_frame()
    history.append(inventory_status_page)
    tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

    tk.Button(root, text="Department List", command=department_list_page).pack(pady=5)
    tk.Button(root, text="Update Inventory", command=update_inventory_page).pack(pady=5)
    tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# User View - Departments Only
def user_view_department():
    clear_frame()
    history.append(user_view_department)
    tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

    departments = ["BEPE", "BEME", "CSN"]
    for dept in departments:
        tk.Button(root, text=dept, command=lambda d=dept: show_prices_in_tabular(d)).pack(pady=5)

    tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# Show Prices in Tabular Form
def show_prices_in_tabular(department):
    clear_frame()
    tk.Label(root, text=f"Price List for {department} Raw Materials", font=('Helvetica', 18, 'bold')).pack(pady=20)

    # Create a Treeview to display the prices in a tabular format
    tree = ttk.Treeview(root, columns=("Item", "Price"), show='headings')
    tree.heading("Item", text="Item")
    tree.heading("Price", text="Price")

    # Data for the different departments
    items = []
    if department == "BEPE":
        items = [
            ("M.s Pipe", "$10.99"),
            ("Electrode", "$12.49"),
            ("Grinding Machine", "$8.75"),
            ("Welding Machine", "$15.00"),
            ("Try Square", "$5.50"),
            ("Thread", "$2.25"),
            ("Power Saw", "$75.00"),
            ("Sand Paper", "$1.50"),
            ("Measuring Tape", "$6.00")
        ]
    elif department == "BEME":
        items = [
            ("Welding Machine", "$15.00"),
            ("Oxy-Acetylene Sets", "$50.00"),
            ("Power Saw", "$75.00"),
            ("Drilling Machine", "$45.00"),
            ("Hand Drilling Machine", "$25.00"),
            ("Grinding Machine", "$8.75")
        ]
    else:  # CSN
        items = [
            ("Monitor", "$120.00"),
            ("Projector", "$300.00"),
            ("Marker Pen", "$1.00"),
            ("Extension Code", "$20.00")
        ]

    # Insert items into the Treeview
    for item in items:
        tree.insert("", "end", values=item)

    tree.pack(pady=10)

    # Add a back button to return to the departments list
    tk.Button(root, text="Back to Departments", command=user_view_department).pack(pady=20)

# Update Inventory Page (Admin)
def update_inventory_page():
    clear_frame()
    history.append(update_inventory_page)
    tk.Label(root, text="Update Item Price", font=('Helvetica', 18, 'bold')).pack(pady=20)

    tk.Label(root, text="Select Item").pack(pady=5)
    
    item_name_var = tk.StringVar()
    
    item_combobox = ttk.Combobox(root, textvariable=item_name_var)
    item_combobox['values'] = list(inventory_data.keys())  # Populate with item names
    item_combobox.pack(pady=5)
    
    tk.Label(root, text="New Price").pack(pady=5)
    price_entry = tk.Entry(root)
    price_entry.pack(pady=5)

    def update_item():
        item_name = item_name_var.get().strip()
        new_price = price_entry.get().strip()

        if item_name in inventory_data and new_price.replace('.', '', 1).isdigit():
            new_price = float(new_price)
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE inventory SET price = ? WHERE item_name = ?", (new_price, item_name))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Updated '{item_name}' to ${new_price:.2f}")
            load_inventory_data()  # Reload inventory data
        else:
            if item_name not in inventory_data:
                messagebox.showerror("Error", "Item name does not exist.")
            else:
                messagebox.showerror("Error", "Invalid price. Please enter a valid numeric value.")

    tk.Button(root, text="Update Item", command=update_item, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)
    tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# Department List Page (Admin)
def department_list_page():
    clear_frame()
    history.append(department_list_page)
    tk.Label(root, text="Department List", font=('Helvetica', 18, 'bold')).pack(pady=20)

    departments = ["BEPE", "BEME", "CSN"]
    for dept in departments:
        tk.Button(root, text=dept, command=lambda d=dept: show_prices_in_tabular(d)).pack(pady=10)

    tk.Button(root, text="Back", command=inventory_status_page).pack(pady=20)

# Start with Admin/User Login Options
def get_started_page():
    clear_frame()
    tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
    tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
    tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)

# Call the init_db to create the database and load data
init_db()
load_inventory_data()

# Call the get started page to initiate
get_started_page()
root.mainloop()

