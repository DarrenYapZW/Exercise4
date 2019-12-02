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
    assert driver.find_element_by_css_selector("input:invalid")

def test_login_username_only():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("")

    elemPassword.send_keys(Keys.RETURN)
    assert driver.find_element_by_css_selector("input:invalid")

def test_login_password_only():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("Iwanttoeat50burger")

    elemPassword.send_keys(Keys.RETURN)
    assert driver.find_element_by_css_selector("input:invalid")

def test_login_fail():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("Benny")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("Password123A")

    elemPassword.send_keys(Keys.RETURN)
    assert driver.find_element_by_class_name("errornote")

def test_login_pass():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("JunYoung")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("Iwanttoeat50burger")

    elemPassword.send_keys(Keys.RETURN)
    assert "Site administration" in driver.title
    

def test_comment_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("Projects done").click()

    elemName = driver.find_element_by_name("author")
    elemName.send_keys("")

    elemComment = driver.find_element_by_name("body")
    elemComment.send_keys("")

    #elem.clear()
    elemName.send_keys(Keys.RETURN)
    assert driver.find_element_by_css_selector("input:invalid")
    

def test_comment_name_only():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("Projects done").click()

    elemName = driver.find_element_by_name("author")
    elemName.send_keys("JJ")

    elemComment = driver.find_element_by_name("body")
    elemComment.send_keys("")

    #elem.clear()
    elemName.send_keys(Keys.RETURN)
    assert driver.find_element_by_css_selector("textarea:invalid")

def test_comment_comment_only():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("Projects done").click()

    elemName = driver.find_element_by_name("author")
    elemName.send_keys("")

    elemComment = driver.find_element_by_name("body")
    elemComment.send_keys("Hi!")

    #elem.clear()
    elemName.send_keys(Keys.RETURN)
    assert driver.find_element_by_css_selector("input:invalid")

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
    

def test_accessible():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("Projects done").click()
    assert "Projects done" in driver.title
    
#yeah boy
