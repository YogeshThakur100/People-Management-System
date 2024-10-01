# People Management System

This is a **People Management System** built using Django, a high-level Python web framework. The application allows administrators to manage employees, including adding, removing, viewing, and filtering employee details.

## Features

- **View All Employees**: A complete list of all employees can be viewed on the dashboard.
- **Add an Employee**: Administrators can add new employees by filling out a form with the necessary details.
- **Remove an Employee**: Employees can be removed from the system with a simple action.
- **Filter Employees**: Employees can be filtered based on different criteria (e.g., department, role, name).

## Technologies Used

### Frontend:
- **HTML5/CSS3**: For creating the user interface and styling.
  
### Backend:
- **Django**: A Python web framework used for developing the application.
- **SQLite**: A lightweight database used to store employee data.

### Additional Tools:
- **Django REST Framework**: For handling API endpoints and data serialization (if APIs are involved).
- **Bootstrap**: A CSS framework used to enhance the responsiveness and design of the web application.

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/people-management-system.git
2. **Navigate to the project directory**:
   ```bash
   cd people-management-system
3. **Create a virtual environment (optional but recommended)**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
5. **Apply database migrations**:
   ```bash
   python manage.py migrate
6. **Run the development server:**:
   ```bash
   python manage.py runserver
7. **Access the application: Open your browser and navigate to**:
   ```bash
   http://127.0.0.1:8000.

### Video Overview
https://github.com/user-attachments/assets/b489b331-1e27-4971-bd55-09ffd983b132






