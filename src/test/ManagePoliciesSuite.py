import unittest
from utils.ManagePoliciesUtils import ManagePoliciesUtils


class ManagePoliciesSuite(unittest.TestCase):
    def setUp(self):
        self.url = "https://school.moodledemo.net/"
        self.username = "privacyofficer"
        self.password = "moodle"

    def tearDown(self):
        pass

    def test_600_sample(self):
        browser = "firefox"
        policyName = "Privacy policy"
        filter = ""
        userId = ('0')
        action = "Accept"
        expect = "successful"
        num = 600
        self.assertTrue(ManagePoliciesUtils.test((browser, self.url, self.username, self.password, policyName, filter, userId, action), expect, num))

    def test_601_basic_flow(self):
        browser = "firefox"
        policyName = "Privacy policy"
        filter = ""
        userId = ('0')
        action = "Accept"
        expect = "successful"
        num = 601
        self.assertTrue(ManagePoliciesUtils.test((browser, self.url, self.username, self.password, policyName, filter, userId, action), expect, num))

    def test_602_alternative_flow_withdraw(self):
        browser = "firefox"
        policyName = "Privacy policy"
        filter = ""
        userId = ('0')
        action = "Withdraw"
        expect = "successful"
        num = 602
        self.assertTrue(ManagePoliciesUtils.test((browser, self.url, self.username, self.password, policyName, filter, userId, action), expect, num))

    def test_603_exception_decline(self):
        browser = "firefox"
        policyName = "Privacy policy"
        filter = ""
        userId = ('0')
        action = "Decline"
        expect = "Compulsory policies cannot be declined!"
        num = 603
        self.assertTrue(ManagePoliciesUtils.test((browser, self.url, self.username, self.password, policyName, filter, userId, action), expect, num))

    def test_604_alternative_flow_bulk_action(self):
        browser = "firefox"
        policyName = "Privacy policy"
        filter = ""
        userId = ('0', '1')
        action = "Accept"
        expect = "successful"
        num = 604
        self.assertTrue(ManagePoliciesUtils.test((browser, self.url, self.username, self.password, policyName, filter, userId, action), expect, num))