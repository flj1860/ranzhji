#coding=utf-8
from time import sleep

from selenium.webdriver.support.select import Select

from base.automate_driver import AutomateDriver
from base.base_page_ranzhi import BasePage


class RanzhiMainPage():
    def __init__(self,driver:AutomateDriver):
        self.driver = driver

    def login(self,login_data):
        driver = self.driver
        sleep(2)
        #driver.find_element_by_css_selector('#account').send_keys('system')
        driver.type('s,#account',login_data['username'])
        #driver.find_element_by_name('password').send_keys('159753')
        driver.type('n,password',login_data['password'])
        #driver.find_element_by_css_selector('#submit').click()
        driver.click('s,#submit')


    def add_user(self,username,password):
        driver = self.driver
        sleep(2)
        driver.find_element_by_xpath('.//*[@id=\'s-menu-superadmin\']/button').click()
        #driver.click('x,.//*[@id=\'s-menu-superadmin\']/button')
        sleep(2)
        #driver.switch_to_frame('iframe-superadmin')
        driver.switch_frame('iframe-superadmin')
        driver.find_element_by_xpath('.//*[@id=\'shortcutBox\']/div/div[1]/div/a/h3').click()
        #driver.click('x,.//*[@id=\'shortcutBox\']/div/div[1]/div/a/h3')
        sleep(3)
        driver.find_element_by_id('account').send_keys('aaaa')
        #driver.type('account',username)
        driver.find_element_by_id('realname').send_keys('xiaoli')
        #driver.type('realname',"xiaoli")
        driver.find_element_by_id('gender2').click()
        #driver.click('gender2')
        driver.find_element_by_css_selector('#dept')
        sleep(2)
        #driver.type('s,#dept')
        Select(driver.find_element_by_css_selector('#dept')).select_by_value('820001')
        #driver.select_by_value('s,#dept',"820001")
        sleep(2)
        Select(driver.find_element_by_xpath('.//*[@id=\'role\']')).select_by_value('dev')
        #driver.select_by_value('x,.//*[@id=\'role\']',"dev")
        sleep(2)
        driver.find_element_by_id('password1').send_keys('123456')
        #driver.type('password1',password)
        sleep(2)
        driver.find_element_by_id('password2').send_keys('123456')
        #driver.type('password2',password)
        sleep(2)
        driver.find_element_by_id('email').send_keys('123@q.com')
        #driver.type('email',"123@q.com")
        sleep(2)
        driver.find_element_by_id('submit').click()
        #driver.click('submit')
        sleep(2)
        driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[3]').click()
        #driver.click('x,html/body/div[1]/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[3]')
        sleep(3)
        driver.accept_alert()
        sleep(2)

