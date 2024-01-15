from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class OrangeHrmLive:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.domain = "https://opensource-demo.orangehrmlive.com"

    def login(self, username: str, password: str) -> None:
        self.driver.get(self.domain + "/web/index.php/auth/login")
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
        login_button.click()

    def add_employee(self, emp_data: dict) -> None:
        self.driver.get(self.domain + "/web/index.php/pim/addEmployee")
        self.click_checkbox()
        self.add_first_name(emp_data.get("first_name"))
        self.add_last_name(emp_data.get("last_name"))
        self.add_username(emp_data.get("username"))
        self.add_password(emp_data.get("password"))
        self.press_save_button()

    def click_checkbox(self) -> None:
        checkbox_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "label[data-v-8e4757dc] input[type='checkbox']")
            )
        )
        self.driver.execute_script("arguments[0].click();", checkbox_element)

    def add_first_name(self, first_name: str) -> None:
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        )
        first_name_field.send_keys(first_name)

    def add_last_name(self, last_name: str) -> None:
        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "lastName"))
        )
        last_name_field.send_keys(last_name)

    def add_username(self, username: str) -> None:
        username_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[label[text()='Username']]/following-sibling::div//input[@data-v-1f99f73c]",
                )
            )
        )
        username_field.send_keys(username)

    def add_password(self, password: str) -> None:
        password_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[label[text()='Password']]/following-sibling::div//input[@type='password'][@data-v-1f99f73c]",
                )
            )
        )
        confirm_password_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[label[text()='Confirm Password']]/following-sibling::div//input[@type='password'][@data-v-1f99f73c]",
                )
            )
        )
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)

    def press_save_button(self):
        save_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-v-10d463b7][type='submit']")
            )
        )
        save_button.click()

    def add_employee_details(self) -> None:
        self.press_job_button()
        self.add_joined_date()
        self.add_job_title()
        self.add_job_category()
        self.add_location()
        self.add_emp_status()
        self.press_save_button()

    def press_job_button(self) -> None:
        job_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@role='tablist']/div/a[@class='orangehrm-tabs-item' and text()='Job']",
                )
            )
        )
        job_button.click()

    def add_joined_date(self) -> None:
        joined_date = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "div[data-v-4a95a2e0] input[placeholder='yyyy-mm-dd']",
                )
            )
        )
        joined_date.click()
        joined_date.send_keys("2022-10-12")

    def add_job_title(self) -> None:
        job_title = self.driver.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]',
        )
        job_title.click()

        job_title_options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]',
                )
            )
        )
        job_title_options[0].click()

    def add_job_category(self) -> None:
        job_category = self.driver.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[1]/div[2]',
        )
        job_category.click()

        job_category_options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]',
                )
            )
        )
        job_category_options[0].click()

    def add_location(self) -> None:
        location = self.driver.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]',
        )
        location.click()

        location_options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[2]',
                )
            )
        )
        location_options[0].click()

    def add_emp_status(self) -> None:
        emp_status = self.driver.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[2]',
        )
        emp_status.click()

        emp_status_options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//span[text()="Full-Time Permanent"]')
            )
        )
        emp_status_options.click()

    def add_supervisor(self) -> None:
        self.press_supervisor_button()
        self.press_add_button()
        self.add_supervisor_name()
        self.add_reporting_method()
        self.press_save_button()

    def press_supervisor_button(self) -> None:
        supervisor_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@role='tablist']/div/a[@class='orangehrm-tabs-item' and text()='Report-to']",
                )
            )
        )
        supervisor_button.click()

    def press_add_button(self) -> None:
        add_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'oxd-button--medium') and contains(@class, 'oxd-button--text') and contains(., 'Add')]",
                )
            )
        )
        add_button.click()

    def add_supervisor_name(self) -> None:
        supervisor_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "input[placeholder='Type for hints...']",
                )
            )
        )

        supervisor_name.send_keys("Odis Adalwin")
        time.sleep(3)

        supervisor_name_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div[2]',
                )
            )
        )
        supervisor_name_option[0].click()

    def add_reporting_method(self) -> None:
        reporting_method = self.driver.find_element(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]',
        )
        reporting_method.click()

        reporting_method_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]',
                )
            )
        )
        reporting_method_option[0].click()

    def search_employee(self) -> None:
        self.driver.get(self.domain + "/web/index.php/pim/viewEmployeeList")
        self.check_emp_status()
        self.check_supervisor()
        self.press_save_button()

    def check_emp_status(self) -> None:
        emp_status = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]',
                )
            )
        )
        emp_status.click()

        emp_status_options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//span[text()="Full-Time Permanent"]')
            )
        )
        emp_status_options.click()

    def check_supervisor(self) -> None:
        supervisor = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[5]/div/div[2]/div/div/input',
                )
            )
        )
        supervisor.send_keys("Odis Adalwin")
        time.sleep(3)
        supervisor_options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[5]/div/div[2]/div/div[2]',
                )
            )
        )
        supervisor_options[0].click()

    def edit_employee(self, name) -> None:
        self.open_employee_data(name)
        self.add_middle_name()
        self.add_nickname()
        self.add_other_id()
        self.add_drivers_license()
        self.add_license_exp_date()
        self.add_ssn_number()
        self.add_sin_number()
        self.add_nationality()
        self.add_martial_status()
        self.add_date_of_birth()
        self.add_gender()
        self.add_mil_service()
        self.add_blood_type()
        self.click_save()
        # self.add_attachment()

    def open_employee_data(self, name) -> None:
        table_body = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]',
                )
            )
        )
        rows = table_body.find_elements(By.CLASS_NAME, "oxd-table-card")
        for row in rows:
            if name in row.text:
                edit_button = row.find_element(
                    By.XPATH, ".//i[@class='oxd-icon bi-pencil-fill']"
                )
                self.driver.execute_script(
                    "arguments[0].scrollIntoView(true);", edit_button
                )
                edit_button.click()

    def add_middle_name(self) -> None:
        middle_name = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input',
                )
            )
        )
        middle_name.send_keys("PK")

    def add_nickname(self) -> None:
        nickname = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input',
                )
            )
        )
        nickname.send_keys("PK")

    def add_other_id(self) -> None:
        middle_name = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input',
                )
            )
        )
        middle_name.send_keys("696969")

    def add_drivers_license(self) -> None:
        drivers_license = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input',
                )
            )
        )
        drivers_license.send_keys("696969")

    def add_license_exp_date(self) -> None:
        license_exp = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input',
                )
            )
        )
        license_exp.click()
        license_exp.send_keys("2024-02-01")

    def add_ssn_number(self) -> None:
        ssn_number = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input',
                )
            )
        )
        ssn_number.send_keys("1234567890")

    def add_sin_number(self) -> None:
        sin_number = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input',
                )
            )
        )
        sin_number.send_keys("1234567890")

    def add_nationality(self) -> None:
        nationality = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]',
                )
            )
        )
        nationality.click()
        nationality_option = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[5]',
                )
            )
        )
        nationality_option.click()

    def add_martial_status(self) -> None:
        martial_status = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div',
                )
            )
        )
        martial_status.click()
        martial_status_option = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]',
                )
            )
        )
        martial_status_option.click()

    def add_date_of_birth(self) -> None:
        date_of_birth = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input',
                )
            )
        )
        date_of_birth.click()
        date_of_birth.send_keys("1999-02-01")

    def add_gender(self) -> None:
        gender = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span',
                )
            )
        )
        gender.click()

    def add_mil_service(self) -> None:
        mil_service = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input',
                )
            )
        )
        mil_service.send_keys("Gelezinis vilkas")

    def add_blood_type(self) -> None:
        blood_type = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div',
                )
            )
        )
        blood_type.click()
        blood_type_option = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div[2]/div[3]',
                )
            )
        )
        blood_type_option.click()

    def click_save(self) -> None:
        save = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button',
                )
            )
        )
        save.click()

    def add_attachment(self) -> None:
        self.click_add()
        self.click_browse()
        self.attach_file()

    def click_add(self) -> None:
        add_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div/button',
                )
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
        add_button.click()

    def click_browse(self) -> None:
        browse_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[1]/div/div/div/div[2]/div/div[1]',
                )
            )
        )
        browse_button.click()

    def attach_file(self) -> None:
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[1]/div/div/div/div[2]/div/div[2]',
                )
            )
        )

        file_path = "C:/Users/cante/Desktop/a.txt"
        file_input.send_keys(file_path)

    def quit_driver(self) -> None:
        input("Press Enter to close the browser...")
        self.driver.quit()
