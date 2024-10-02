# Add global variable for LRC user state
is_lrc_user = False

# User Login Page (with LRC user option)
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
        global is_admin, is_lrc_user
        username = username_entry.get()
        password = password_entry.get()

        # Here you can implement specific checks for LRC user credentials.
        # For example, if username is "lrc_user" and password is "lrc_password"
        if username == "lrc_user" and password == "lrc_password":
            is_lrc_user = True  # Set as LRC user
            user_view_department()
        elif username and password:  # Simple check for regular users
            is_admin = False  # Set as regular user
            user_view_department()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# Modify how user permissions are handled
def user_view_department():
    clear_frame()
    history.append(user_view_department)
    tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

    departments = ["BEPE", "BEME", "CSN"]

    for dept in departments:
        tk.Button(root, text=dept, command=lambda d=dept: user_view_price(d)).pack(pady=10)

    tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# If you wish to restrict LRC users from certain functionalities, you can modify the access to the options
def inventory_status_page():
    clear_frame()
    history.append(inventory_status_page)
    tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

    # If the user is not an admin, hide or restrict access to certain features
    if is_admin:
        tk.Button(root, text="Department", command=department_list_page).pack(pady=5)
        tk.Button(root, text="Price", command=lambda: show_price_details("All")).pack(pady=5)
        tk.Button(root, text="Update", command=update_inventory_page).pack(pady=5)
        tk.Button(root, text="Report", command=report_page).pack(pady=5)
    elif is_lrc_user:
        tk.Button(root, text="Department", command=user_view_department).pack(pady=5)
        tk.Button(root, text="Price", command=lambda: show_price_details("All")).pack(pady=5)

    tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# Start with Admin/User Login Options
def get_started_page():
    clear_frame()
    tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
    tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
    tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
    tk.Button(root, text="LRC User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)  # Added LRC user option# Add global variable for LRC user state
is_lrc_user = False

# User Login Page (with LRC user option)
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
        global is_admin, is_lrc_user
        username = username_entry.get()
        password = password_entry.get()

        # Here you can implement specific checks for LRC user credentials.
        # For example, if username is "lrc_user" and password is "lrc_password"
        if username == "lrc_user" and password == "lrc_password":
            is_lrc_user = True  # Set as LRC user
            user_view_department()
        elif username and password:  # Simple check for regular users
            is_admin = False  # Set as regular user
            user_view_department()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(root, text="Login", command=login, font=('Helvetica', 14), bg="green", fg="white").pack(pady=20)

# Modify how user permissions are handled
def user_view_department():
    clear_frame()
    history.append(user_view_department)
    tk.Label(root, text="Departments", font=('Helvetica', 18, 'bold')).pack(pady=20)

    departments = ["BEPE", "BEME", "CSN"]

    for dept in departments:
        tk.Button(root, text=dept, command=lambda d=dept: user_view_price(d)).pack(pady=10)

    tk.Button(root, text="Back", command=get_started_page).pack(pady=20)

# If you wish to restrict LRC users from certain functionalities, you can modify the access to the options
def inventory_status_page():
    clear_frame()
    history.append(inventory_status_page)
    tk.Label(root, text="Inventory Status", font=('Helvetica', 18, 'bold')).pack(pady=20)

    # If the user is not an admin, hide or restrict access to certain features
    if is_admin:
        tk.Button(root, text="Department", command=department_list_page).pack(pady=5)
        tk.Button(root, text="Price", command=lambda: show_price_details("All")).pack(pady=5)
        tk.Button(root, text="Update", command=update_inventory_page).pack(pady=5)
        tk.Button(root, text="Report", command=report_page).pack(pady=5)
    elif is_lrc_user:
        tk.Button(root, text="Department", command=user_view_department).pack(pady=5)
        tk.Button(root, text="Price", command=lambda: show_price_details("All")).pack(pady=5)

    tk.Button(root, text="Back", command=get_started_page, font=('Helvetica', 14), bg="red", fg="white").pack(pady=20)

# Start with Admin/User Login Options
def get_started_page():
    clear_frame()
    tk.Label(root, text="Welcome to Inventory System", font=('Helvetica', 24, 'bold')).pack(pady=50)
    tk.Button(root, text="Admin Login", command=admin_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
    tk.Button(root, text="User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)
    tk.Button(root, text="LRC User Login", command=user_login_page, font=('Helvetica', 14), bg="blue", fg="white").pack(pady=20)  # Added LRC user option