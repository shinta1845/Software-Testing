import unittest
from utils.TestUtils import TestDataRequests
from utils.LoginUtils import LoginUtils


class DataRequestsSuite(unittest.TestCase):
    def setUp(self):
        self.url = "https://school.moodledemo.net/"
        self.username = "privacyofficer"
        self.password = "moodle"

    def tearDown(self):
        # LoginUtils.logout()
        # if LoginUtils.driver is not None:
            # LoginUtils.driver.close()
        pass

    # def test_500_sample(self):
    #     browser = "firefox"
    #     filter = "Type: Export"
    #     requestId = ('3')
    #     action = "approve"
    #     expect = "successful"
    #     num = 500
    #     self.assertTrue(TestDataRequests.test((browser, self.url, self.username, self.password, filter, requestId, action), expect, num))

    def test_501_basic_flow(self):
        browser = "firefox"
        filter = ""
        requestId = ('3')
        action = "approve"
        expect = "successful"
        num = 501
        self.assertTrue(TestDataRequests.test((browser, self.url, self.username, self.password, filter, requestId, action), expect, num))

    def test_502_alternative_flow_filter_type(self):
        browser = "firefox"
        filter = "Type: Export"
        requestId = ('0')
        action = "approve"
        expect = "successful"
        num = 502
        self.assertTrue(TestDataRequests.test((browser, self.url, self.username, self.password, filter, requestId, action), expect, num))

    def test_503_alternative_flow_deny_request(self):
        browser = "firefox"
        filter = ""
        requestId = ('2')
        action = "deny"
        expect = "successful"
        num = 503
        self.assertTrue(TestDataRequests.test((browser, self.url, self.username, self.password, filter, requestId, action), expect, num))

    def test_504_alternative_flow_bulk_action(self):
        browser = "firefox"
        filter = ""
        requestId = ('1')
        action = "approve"
        expect = "successful"
        num = 504
        self.assertTrue(TestDataRequests.test((browser, self.url, self.username, self.password, filter, requestId, action), expect, num))