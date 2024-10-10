from flask import Flask, render_template_string

app = Flask(__name__)

# Your HTML code (put your entire HTML code here as a string)
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inventory Management</title>
    <link rel="stylesheet" href="/static/inventory.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    <!-- Login Page -->
    <div class="login-container" id="loginPage">
        <div class="image-overlay">
            <h1>WELCOME</h1>
            <div class="login-form">
                <form id="loginForm">
                    <input type="email" id="email" placeholder="email@domain.com" required>
                    <input type="password" id="password" placeholder="Password" required>
                    <a href="#" class="forgot-password">Forgot Password?</a>
                    <button type="submit" class="login-btn">LOGIN</button>
                </form>
            </div>
        </div>
    </div>

    <!-- Dashboard Page -->
    <div class="dashboard-container" id="dashboardPage">
        <header>
            <h1>INVENTORY STATUS</h1>
        </header>
        <div class="banner">
            <p>Check the stock level!</p>
        </div>
        <div class="container">
            <div class="dashboard-item" id="departmentItem" class="card">
                <i class="fas fa-building"></i>
                <p>Department</p>
            </div>
            <div class="dashboard-item" class="card">
                <i class="fas fa-tag"></i>
                <p>Price</p>
            </div>
            <div class="dashboard-item" class="card">
                <i class="fas fa-box"></i>
                <p>Order</p>
            </div>
            <div class="dashboard-item" class="card">
                <i class="fas fa-user"></i>
                <p>User</p>
            </div>
            <div class="dashboard-item" class="card">
                <i class="fas fa-tasks"></i>
                <p>Status</p>
            </div>
            <div class="dashboard-item" class="card">
                <i class="fas fa-cog"></i>
                <p>Management</p>
            </div>
            <div class="dashboard-item" class="card">
                <i class="fas fa-desktop"></i>
                <p>Interface</p>
            </div>
            <div class="dashboard-item" class="card">
                <i class="fas fa-file-alt"></i>
                <p>Report</p>
            </div>
        </div>
    </div>

    <!-- Department Selection Page -->
    <div class="department-container" id="departmentPage">
        <h1>Select a Department</h1>
        <div class="department-form">
            <select id="departmentDropdown">
                <option value="department">Select department</option>
                <option value="Power">B.E. in Power Engineering</option>
                <option value="Mechanical">B.E. Mechanical Engineering</option>
                <!-- Add other departments here -->
            </select>
            <button class="department-login-btn" id="goToLoginBtn">Go to Department Login</button>
        </div>
    </div>

    <!-- Department Login Page -->
    <div class="department-login-container" id="departmentLoginPage">
        <h1>DEPARTMENT LOGIN</h1>
        <p>Please enter your department code</p>
        <div class="department-login-form">
            <form id="departmentLoginForm">
                <input type="text" id="departmentCode" placeholder="Enter Department Code" required>
                <button type="submit" class="login-btn">LOGIN</button>
            </form>
        </div>
    </div>

    <!-- Admin Dashboard Page -->
    <div class="admin-dashboard-container" id="adminDashboardPage">
        <h1>Admin Dashboard</h1>
        <button class="admin-dashboard-btn" id="addItemBtn">Add Item</button>
        <button class="admin-dashboard-btn" id="deleteItemBtn">Delete Item</button>
        <button class="admin-dashboard-btn" id="viewInventoryBtn">View Inventory</button>
        <button class="admin-dashboard-btn" id="monthlyReportBtn">Report</button>
        <button class="admin-dashboard-btn" id="viewOrdersBtn">View Orders</button>
    </div>

    <footer>
        <p>© 2024 Inventory Management System</p>
    </footer>

    <script>
        // Login form submission
        document.getElementById("loginForm").addEventListener("submit", function(event) {
            event.preventDefault();

            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;

            if (email && password) {
                // Simulate login
                document.getElementById("loginPage").style.display = "none";
                document.getElementById("dashboardPage").style.display = "block";
            } else {
                alert("Please fill in all fields");
            }
        });

        // Show department selection page when Department is clicked
        document.getElementById("departmentItem").addEventListener("click", function() {
            document.getElementById("dashboardPage").style.display = "none";
            document.getElementById("departmentPage").style.display = "block";
        });

        // Handle department selection and go to department login page
        document.getElementById("goToLoginBtn").addEventListener("click", function() {
            const selectedDepartment = document.getElementById("departmentDropdown").value;

            if (selectedDepartment) {
                document.getElementById("departmentPage").style.display = "none";
                document.getElementById("departmentLoginPage").style.display = "block";
            } else {
                alert("Please select a department");
            }
        });

        // Handle department login form submission
        document.getElementById("departmentLoginForm").addEventListener("submit", function(event) {
            event.preventDefault();

            const departmentCode = document.getElementById("departmentCode").value;

            if (departmentCode) {
                document.getElementById("departmentLoginPage").style.display = "none";
                document.getElementById("adminDashboardPage").style.display = "block";
            } else {
                alert("Please enter the department code");
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)