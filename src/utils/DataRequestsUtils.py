from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from utils.Utils import Utils
import time


class DataRequestsUtils(Utils):
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
        cls.driver.find_element(By.XPATH, """/html/body/div[2]/div[3]/div/div[3]/div/section/div/div[2]/div[2]/div/div[2]/div[2]/ul/li[1]/a""").click()
        time.sleep(1)

    @classmethod
    def action(cls, requestId, action):
        # /html/body/div[2]/div[4]/div/div[3]/div/section/div/div/div[2]/div[1]/table/tbody/tr[4]/td[8]/div/div/div/div/a
        if len(requestId) == 1:
            reqId = requestId[0]
            try:
                # find the request action button
                req = cls.driver.find_element(By.XPATH, "//*[@id='data-requests-table_r" + str(reqId) + "_c7']/div/div/div/div")
                if req.is_displayed():
                    cls.driver.implicitly_wait(10)
                    req.find_element(By.XPATH, "a").click()
                    time.sleep(1)
                    # select action
                    # return "//a[@data-action='" + str(action) + "']"
                    try:
                        cls.driver.implicitly_wait(10)
                        action = req.find_element(By.CSS_SELECTOR, "a[data-action='" + str(action) + "']").click()
                        time.sleep(1)
                        # //*[@id="page-admin-tool-dataprivacy-datarequests"]/div[4]/div[2]/div/div/div[3]/button[2]
                        # /html/body/div[4]/div[2]/div/div/div[3]/button[2]
                        if action == "approve":
                            cls.driver.implicitly_wait(10)
                            req.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[3]/button[2]").click()
                        elif action == "deny":
                            continue
                        else:
                            raise Exception("Can not complete action")
                        time.sleep(1)
                        return "successful"
                    except Exception as e:
                        raise Exception("Invalid action")
                        # return str(e)
            except Exception as e:
                raise Exception("Invalid request ID " + str(reqId))
        else: # Bulk action
            # checkbox, select requests
            for reqId in requestId:
                req = cls.driver.find_element(By.XPATH, "//*[@id='data-requests-table_r" + str(reqId) + "_c0']/input")
                if req.is_displayed():
                    cls.driver.implicitly_wait(10)
                    req.click()
                    time.sleep(1)
                else:
                    raise Exception("Invalid request id " + str(reqId))
            # select action
            select = Select(cls.driver.find_element(By.ID, "bulk-action"))
            cls.driver.implicitly_wait(10)
            if action == "approve":
                select.select_by_value("1")
            elif action == "deny":
                select.select_by_value("2")
            else:
                raise Exception("Invalid bulk action")
            cls.driver.implicitly_wait(10)
            cls.driver.find_element(By.ID, "confirm-bulk-action").click()
            time.sleep(1)
            cls.driver.implicitly_wait(10)
            cls.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[3]/button[2]").click()
            time.sleep(1)
            return "successful"
                
    @classmethod
    def addFilter(cls, filter):
        filter = cls.driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/div[1]/form/div[2]/input")
        filter.clear()
        cls.driver.implicitly_wait(10)
        filter.send_keys(filter)
        time.sleep(1)
        try:
            # cls.driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/div[1]/form/ul/li[1]").click()
            filterList = cls.driver.find_elements(By.XPATH, "/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/div[1]/form/ul/li")
            for f in filterList:
                if f.is_displayed():
                    cls.driver.implicitly_wait(10)
                    f.click()
                    break
        except Exception as e:
            raise Exception("Invalid filter")
            # return str(e)
        time.sleep(1)