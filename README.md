**Project Overview**
The Student Management System is a web application developed using Django that allows users to manage student records effectively. Users can perform operations such as adding, editing, deleting, and searching for student details.

**Features**
- User Authentication: Secure login/logout functionality.
- Student Management:
   - List all students with pagination (5 students per page).
   - View details of a single student.
   - Add new student records.
   -Edit existing student information.
- Search Functionality: Search for students by first or last name.
- Responsive Design: User-friendly interface with styled components.

**Installation**
To set up the project on your local machine, follow these steps:
- Clone the Repository:
    git clone <repository_url>
    cd student_management
- Set Up Virtual Environment (optional but recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
- Install Dependencies: Make sure you have Django installed. If not, install it using:
    pip install django
- Run Migrations:
    python manage.py migrate
- Create a Superuser (for admin access):
    python manage.py createsuperuser
- Run the Development Server:
    python manage.py runserver
- Access the Application: Open your web browser and go to http://127.0.0.1:8000.

**Login Credentials**
Use the following credentials to log in:
    Username: test
    Password: test123

**File Structure**

student_management/
│
├── student/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   │       ├── student_list.html
│   │       ├── student_detail.html
│   │       ├── student_form.html
│   │       └── student_confirm_delete.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── student_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── db.sqlite3

**Usage**
- Adding a Student: Click on the "Add a new student" button on the student list page, fill in the required fields, and submit the form.
-Editing a Student: Click on the "Edit" button next to a student's name to modify their information.
- Deleting a Student: Click on the "Delete" button to remove a student record.
- Searching for Students: Use the search bar to filter students by their first or last names.
- Pagination: Navigate through the list of students using the pagination controls at the bottom of the student list page.
  
**Conclusion**
- The Student Management System is designed to provide a straightforward and efficient way to manage student records. With features like user authentication, search functionality, and pagination, it enhances the user experience and ensures effective management of student data.
