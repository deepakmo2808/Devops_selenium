from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SeleniumTestCase(TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chromeOptions.add_argument("--remote-debugging-port=9222")
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)


    def test_LoginAndRegistrationForm(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_xpath('/html/body/header/nav/div/div/div[2]/a[2]').click()
        self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/fieldset/div[1]/div/input').send_keys(
            'sanjayrohra45')
        self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/fieldset/div[2]/div/input').send_keys(
            'rohra470@gmail.com')
        self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/fieldset/div[3]/div/input').send_keys(
            'HelloWorld@123')
        self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/fieldset/div[4]/div/input').send_keys(
            'HelloWorld@123')
        self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/div/button').click()

        self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/fieldset/div[1]/div/input').send_keys(
            'sanjayrohra45')
        self.driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/fieldset/div[2]/div/input').send_keys(
            'HelloWorld@123')
