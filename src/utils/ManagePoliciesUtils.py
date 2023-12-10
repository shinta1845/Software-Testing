from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from utils.Utils import Utils
import time


class ManagePoliciesUtils(Utils):
    @classmethod
    def getDataRequestsPage(cls):
        # get Site administration page
        siteAdministration = cls.driver.find_element(By.XPATH, """/html/body/div[2]/nav/div[1]/nav/ul/li[4]/a""")
        if siteAdministration.is_displayed():
            cls.driver.implicitly_wait(10)
            siteAdministration.click()
        else:
            menu = cls.driver.find_element(By.ID, "/html/body/div[2]/nav/button")
            if menu.is_displayed():
                cls.driver.implicitly_wait(10)
                menu.click()
                time.sleep(1)
                cls.driver.implicitly_wait(10)
                cls.driver.find_element(By.XPATH, """/html/body/div[2]/div[2]/div[2]/div/a[4]""").click()
            else:
                more = cls.driver.find_element(By.XPATH, """/html/body/div[2]/nav/div[1]/nav/ul/li[3]/a""")
                if more.is_displayed():
                    cls.driver.implicitly_wait(10)
                    more.click()
                    time.sleep(1)
                    cls.driver.implicitly_wait(10)
                    cls.driver.find_element(By.XPATH, """/html/body/div[2]/nav/div[1]/nav/ul/li[3]/ul/li[2]/a""").click()
                else:
                    raise Exception("Cannot find Site administration menu")
        time.sleep(1)

        # get Users tab
        cls.driver.implicitly_wait(10)
        cls.driver.find_element(By.XPATH, """/html/body/div[2]/div[3]/div/div[2]/nav/ul/li[2]/a""").click()

        # get Data requests tab
        cls.driver.implicitly_wait(10)
        cls.driver.find_element(By.XPATH, """/html/body/div[2]/div[3]/div/div[3]/div/section/div/div[2]/div[2]/div/div[2]/div[2]/ul/li[5]/a""").click()
        time.sleep(1)

    @classmethod
    def choosePolicy(cls, policyName):
        policy = cls.driver.find_element(By.CSS_SELECTOR, "tr[data-policy-name='" + str(policyName) + "']")
        try:
            aggreements = policy.find_elements(By.XPATH, "td[4]/a").click()
        except Exception as e:
            raise Exception("Agreements: N/A")

    @classmethod
    def action(cls, userId, action):
        if len(userId) == 1:
            userId = userId[0]
            try:
                user = cls.driver.find_element(By.XPATH, "//*[@id='tool_policy_user_acceptances_r'" + str(userId) + "']")
                response = user.find_element(By.XPATH, "td[3]")
                try:
                    cls.driver.implicitly_wait(10)
                    response.find_element(By.LINK_TEXT, action).click()
                    time.sleep(1)
                    if action == "Accept":
                        cls.driver.implicitly_wait(10)
                        cls.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[3]/button[2]").click()
                    elif action == "Withdraw":
                        cls.driver.implicitly_wait(10)
                        cls.driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div[3]/button[2]").click()
                    elif action == "Decline":
                        pass
                    else:
                        raise Exception("Can not complete action")
                    time.sleep(1)
                    return "successful"
                except Exception as e:
                    raise Exception("Invalid action " + str(action))
            except Exception as e:
                raise Exception("Invalid user ID " + str(userId))
        else: # bulk action
            # select users checkbox
            for user in userId:
                # checkbox
                try:
                    cls.driver.implicitly_wait(10)
                    select = cls.driver.find_element(By.XPATH, "//*[@id='tool_policy_user_acceptances_r" + str(user) + "']/td[1]/input").click()
                except Exception as e:
                    raise Exception("Invalid user ID " + str(user))
            # bulk action
            try:
                cls.driver.implicitly_wait(10)
                cls.driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[3]/div/section/div/form[3]/input[5]").click()
                time.sleep(1)
                cls.driver.implicitly_wait(10)
                cls.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[3]/button[2]").click()
                time.sleep(1)
                return "successful"
            except Exception as e:
                raise Exception("Can not complete bulk action")

    @classmethod
    def addFilter(cls, filter):
        filter = cls.driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[3]/div/section/div/form[1]/div[2]/input")
        filter.clear()
        cls.driver.implicitly_wait(10)
        filter.send_keys(filter)
        time.sleep(1)
        try:
            filterList = cls.driver.find_elements(By.XPATH, "/html/body/div[2]/div[4]/div/div[3]/div/section/div/form[1]/ul/li")
            for f in filterList:
                if f.is_displayed():
                    cls.driver.implicitly_wait(10)
                    f.click()
                    break
        except Exception as e:
            raise Exception("Invalid filter")
        time.sleep(1)