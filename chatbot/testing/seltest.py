import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_login_fail(self):
        self.driver.get("http://localhost:5000/login")

        username = self.driver.find_element(
            by=By.CSS_SELECTOR, value="#login-form input[name='username']")
        username.send_keys(random.randint(1, 10000))

        password = self.driver.find_element(
            by=By.CSS_SELECTOR, value="#login-form input[name='password']")
        password.send_keys(random.randint(1, 10000))

        self.driver.find_element(
            by=By.XPATH, value="//form[@id='login-form']//button[@type='submit']").click()

        self.driver.find_element(
            by=By.CLASS_NAME, value="alert-danger")

    def test_signup_fail(self):
        self.driver.get("http://localhost:5000/login")
        self.driver.find_element(
            by=By.CSS_SELECTOR, value='a.nav-link[data-bs-toggle="tab"][href="#signup-form"]').click()

        username = self.driver.find_element(
            by=By.CSS_SELECTOR, value="#signup-form input[name='username']")
        username.send_keys(random.randint(1, 10000))

        password = self.driver.find_element(
            by=By.CSS_SELECTOR, value="#signup-form input[name='password']")
        password.send_keys(random.randint(1, 10000))

        confirm_password = self.driver.find_element(
            by=By.CSS_SELECTOR, value="#signup-form input[name='confirm-password']")
        confirm_password.send_keys(random.randint(1, 10000))

        email = self.driver.find_element(
            by=By.CSS_SELECTOR, value="#signup-form input[name='email']")
        email.send_keys(str(random.randint(1, 10000)) + "@gmail.com")

        self.driver.find_element(
            by=By.XPATH, value="//div[@id='signup-form']//button[@type='submit']").click()

        self.driver.find_element(
            by=By.CLASS_NAME, value="alert-danger")

    def test_full_site(self):
        self.driver.get("http://localhost:5000/login")
        self.driver.find_element(
            by=By.CSS_SELECTOR, value='a.nav-link[data-bs-toggle="tab"][href="#signup-form"]').click()

        user = random.randint(1, 10000)
        username_box = self.driver.find_element(
            by=By.CSS_SELECTOR, value="#signup-form input[name='username']")
        username_box.send_keys(user)

        passw = random.randint(1, 10000)
        password_box = self.driver.find_element(
            by=By.CSS_SELECTOR, value="#signup-form input[name='password']")
        password_box.send_keys(passw)

        confirm_password = self.driver.find_element(
            by=By.CSS_SELECTOR, value="#signup-form input[name='confirm-password']")
        confirm_password.send_keys(passw)

        email_addr = str(random.randint(1, 10000)) + "@gmail.com"
        email_box = self.driver.find_element(
            by=By.CSS_SELECTOR, value="#signup-form input[name='email']")
        email_box.send_keys(email_addr)

        self.driver.find_element(
            by=By.XPATH, value="//div[@id='signup-form']//button[@type='submit']").click()

        username_box = self.driver.find_element(
            by=By.CSS_SELECTOR, value="#login-form input[name='username']")
        username_box.send_keys(user)

        password_box = self.driver.find_element(
            by=By.CSS_SELECTOR, value="#login-form input[name='password']")
        password_box.send_keys(passw)

        self.driver.find_element(
            by=By.XPATH, value="//form[@id='login-form']//button[@type='submit']").click()

        self.assertIn("http://localhost:5000/home", self.driver.current_url)
        self.assertIn("Home - Chatbot", self.driver.title)

        # Homepage area
        self.driver.find_element(
            by=By.CSS_SELECTOR, value='div.row div.col-md-8.text-start div.card.border-0.bg-light.rounded.position-relative.mb-5.mt-5.d-inline-block')

        time.sleep(2)
        textbox = self.driver.find_element(by=By.ID, value="chattextarea")
        textbox.send_keys("Hello there James, this is Selenium!")
        textbox.send_keys(Keys.ENTER)
        self.driver.find_element(
            by=By.CSS_SELECTOR, value='div.row:nth-of-type(3)')  # the reply from our message

        # History area
        self.driver.get("http://localhost:5000/history")
        self.assertIn("http://localhost:5000/history", self.driver.current_url)
        self.assertIn("History - Chatbot", self.driver.title)

        history_button = self.driver.find_element(
            by=By.XPATH, value="//button[contains(text(), 'Hello there James, this is Selenium!')]")
        history_button.click()

        self.driver.find_element(
            by=By.XPATH, value="//p[contains(text(), 'Hello there James, this is Selenium!')]")

    def test_redirection_unauthorized(self):
        self.driver.get("http://localhost:5000/abcdefgh/zxcvbnm")
        self.assertIn("Login", self.driver.title)
        self.assertIn("http://localhost:5000/login", self.driver.current_url)
        self.driver.get("http://localhost:5000/home")
        self.assertIn("Login", self.driver.title)
        self.assertIn("http://localhost:5000/login", self.driver.current_url)
        self.driver.get("http://localhost:5000/history")
        self.assertIn("Login", self.driver.title)
        self.assertIn("http://localhost:5000/login", self.driver.current_url)
        self.driver.get("http://localhost:5000/")
        self.assertIn("Login", self.driver.title)
        self.assertIn("http://localhost:5000/login", self.driver.current_url)


if __name__ == '__main__':
    unittest.main()
