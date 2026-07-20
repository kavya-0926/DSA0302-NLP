import re

reg_no = input("Enter Register Number: ")
email = input("Enter College Email: ")
course = input("Enter Course Code: ")
semester = input("Enter Semester: ")
mobile = input("Enter Mobile Number: ")

status = True

# Register Number Validation
if re.fullmatch(r'\d{2}[A-Z]{3}\d{4}', reg_no):
    print("Register Number : Valid")
else:
    print("Register Number : Invalid")
    status = False

# Email Validation
if re.fullmatch(r'[\w\.-]+@saveetha\.com', email):
    print("Email : Valid")
else:
    print("Email : Invalid")
    status = False

# Course Code Validation
if re.fullmatch(r'[A-Z]{2,4}\d{3}', course):
    print("Course Code : Valid")
else:
    print("Course Code : Invalid")
    status = False

# Semester Validation
if re.fullmatch(r'[1-8]', semester):
    print("Semester : Valid")
else:
    print("Semester : Invalid")
    status = False

# Mobile Validation
if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Mobile Number : Valid")
else:
    print("Mobile Number : Invalid")
    status = False

# Final Report
print("\nRegistration Status")

if status:
    print("Registration Successful")
else:
    print("Registration Failed")
