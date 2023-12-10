from selenium.webdriver.common.by import By
from utils.Utils import Utils
import time


class LoginUtils(Utils):
    @classmethod
    def login(cls, username, password):
        cls.driver.get(cls.url)
        cls.driver.implicitly_wait(10)
        cls.driver.find_element(By.XPATH, """/html/body/div[2]/nav/div[2]/div[5]/div/span/a""").click()
        cls.driver.find_element(By.ID, "username").clear()
        cls.driver.find_element(By.ID, "username").send_keys(username)
        cls.driver.find_element(By.ID, "password").clear()
        cls.driver.find_element(By.ID, "password").send_keys(password)
        cls.driver.implicitly_wait(10)
        cls.driver.find_element(By.ID, "loginbtn").click()

    @classmethod
    def logout(cls):
        userMenu = cls.driver.find_element(By.ID, "user-menu-toggle")
        # userMenu = cls.driver.find_element(By.XPATH, """/html/body/div[2]/nav/div[2]/div[5]/div/div/a""")
        if userMenu.is_displayed():
            cls.driver.implicitly_wait(10)
            userMenu.click()
            time.sleep(1)
            cls.driver.implicitly_wait(10)
            # cls.driver.find_element(By.XPATH, """/html/body/div[2]/nav/div[2]/div[5]/div/div/div/div/div/div[1]/a[9]""").click()
            cls.driver.find_element(By.XPATH, """//*[@id="carousel-item-main"]/a[9]""").click()
            time.sleep(1)