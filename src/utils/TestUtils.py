import sys, os
from selenium import webdriver

from utils.Utils import Utils
from utils.LoginUtils import LoginUtils
from utils.DataRequestsUtils import DataRequestsUtils
from utils.ManagePoliciesUtils import ManagePoliciesUtils


TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"


class TestUtils:
    @staticmethod
    def makeSource(inputList, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        for line in inputList:
            file.write(str(line) + "\n")
        file.close()


class TestDataRequests:
    @staticmethod
    def test(inputList, expect, num):
        # inputList = (browser, url, username, password, filter, (requestId), action)
        TestUtils.makeSource(inputList, num)
        TestDataRequests.check(SOL_DIR, inputList, num)
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputList, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        try:
            Utils.getDriver(inputList[0], inputList[1])
            LoginUtils.login(inputList[2], inputList[3])
            try:
                DataRequestsUtils.getDataRequestsPage()
                if inputList[4] != "":
                    DataRequestsUtils.addFilter(inputList[4])
                result = DataRequestsUtils.action(inputList[5], inputList[6])
                dest.write(result)
            except Exception as e:
                dest.write(str(e))
            finally:
                LoginUtils.logout()
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
            Utils.driver.implicitly_wait(10)
            Utils.driver.close()


class TestManagePolicies:
    @staticmethod
    def test(inputList, expect, num):
        # inputList = (browser, url, username, password, filter, (requestId), action)
        TestUtils.makeSource(inputList, num)
        TestDataRequests.check(SOL_DIR, inputList, num)
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputList, num):
        # inputList = (browser, url, username, password, policyName, filter, (userId), action)
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        try:
            Utils.getDriver(inputList[0], inputList[1])
            LoginUtils.login(inputList[2], inputList[3])
            try:
                ManagePoliciesUtils.getManagePoliciesPage()
                ManagePoliciesUtils.choosePolicy(inputList[4])
                if inputList[5] != "":
                    ManagePoliciesUtils.addFilter(inputList[5])
                result = ManagePoliciesUtils.action(inputList[6], inputList[7])
                dest.write(result)
            except Exception as e:
                dest.write(str(e))
            finally:
                LoginUtils.logout()
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
            Utils.driver.implicitly_wait(10)
            Utils.driver.close()