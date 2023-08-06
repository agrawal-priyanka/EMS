# EMS
### EMS Project is multipage Streamlit App created using tools like Python, Streamlit and MySQL.

## AIM 
#### Aim of the project is to manage MySQL database using streamlit app as well as develop relationship between Employees as well as Admins.

## Users :
1) Employees - Employees can fetch thier details, no. of leaves and Final salaries after deduction of leaves, status of leave/WFH application as well as apply for Leave/AFH.
2) Admin - Admins can view as well as add, update, delete employees data. Admins can approve Leave Status and WFH status.

## Features:
### 1) Employees
Employees can perform the following actions
- View Personal details
- View Leave details
- View Final salaries after bonuses and deductions
- Apply for Leave and WFH
- Check Leave Status and WFH Status
- Fill Feedback Form
But all this is subject to login credentials of admins. Employee must enter correct login credentials to get access to all these features.

### 2) Admins
Admins need to first enter the credentials and if it matches with database then only they can perform the following functions.
- Add, Update, Delete and View Employee's Personal details
- Add, Update, Delete and View Leave details
- Add, Update, Delete and View Final Salaries
- Add, Update, Delete and View Job Roles
- Check AND Grant Leaves
- Check AND Grant WFH
- Add and View all Departments
  These changes will be directly reflected in MySQL database
 
