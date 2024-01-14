from orange_hrm_live import OrangeHrmLive

orange = OrangeHrmLive()

orange.login("Admin", "admin123")

emp_data = {
    "first_name": "Josenayahasas",
    "last_name": "Konan",
    "username": "kpkpkpkkkkkkkkjklskkk",
    "password": "a1234567",
}

# orange.add_employee(emp_data)
# orange.add_employee_details()
# orange.add_supervisor()
orange.search_employee()
orange.edit_employee(emp_data.get("first_name"))

orange.quit_driver()
