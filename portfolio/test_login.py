import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_login_fail_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("")

    elemPassword.send_keys(Keys.RETURN)
    #assert "Django" in driver.title
    assert driver.find_element_by_css_selector("input:invalid")

def test_login_fail():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("benny")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("Password123A")

    elemPassword.send_keys(Keys.RETURN)


def test_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("Iwanttoeat50burger")

    elemPassword.send_keys(Keys.RETURN)

def test_comment_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("Projects done").click()

    elemName = driver.find_element_by_name("author")
    #elemName.send_keys("JJ")

    #elemComment = driver.find_element_by_name("body")
    #elemComment.send_keys("Hi!")

    #elem.clear()
    elemName.send_keys(Keys.RETURN)

def test_comment_name_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("Projects done").click()

    elemName = driver.find_element_by_name("author")
    elemName.send_keys("JJ")

    #elemComment = driver.find_element_by_name("body")
    #elemComment.send_keys("Hi!")

    #elem.clear()
    elemName.send_keys(Keys.RETURN)

def test_comment():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("Projects done").click()

    elemName = driver.find_element_by_name("author")
    elemName.send_keys("JJ")

    elemComment = driver.find_element_by_name("body")
    elemComment.send_keys("Hi!")

    #elem.clear()
    elemName.send_keys(Keys.RETURN)
