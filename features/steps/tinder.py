from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os
from features.object import tinder
from features.object import google
from features.object import facebook

load_dotenv()

obj         = tinder.object_repository
objGoogle   = google.object_repository
objFacebook = facebook.object_repository

@given('I go to tinder')
def step_impl(context):
    context.browser.get(os.getenv("TINDER_URL"))
    time.sleep(3)

@then('It should have a title Tinder')
def step_impl(context):
   assert context.browser.title == "Tinder | Match. Chat. Date."

@then('I click the Accept cookies')
def step_impl(context):
    buttonAccept = WebDriverWait(context.browser, 10).until(EC.visibility_of_element_located((By.XPATH, obj.buttonAccept)))
    buttonAccept.click()
    time.sleep(1)

@when('I click the sign in with google')
def step_impl(context):
    google = context.browser.find_element_by_xpath(obj.buttonGoogle)
    googleText = google.text
    if "LOG IN WITH GOOGLE" in googleText:
        google.click()
        time.sleep(10)
    else:
        print ("LOG IN WITH GOOGLE not available")

@when('I click More Options')
def step_impl(context):
    buttonMore = context.browser.find_element_by_xpath(obj.buttonMoreOption)
    if context.browser.find_element_by_xpath(obj.buttonMoreOption).is_displayed():
        buttonMore.click()

@then('I see the More Options Sign In')
def step_impl(context):
    buttonFacebook = context.browser.find_element_by_xpath(obj.buttonFacebook2)
    if buttonFacebook.is_displayed():
        time.sleep(3)

@when('I click the LOG IN WITH FACEBOOK')
def step_impl(context):
    fb = True
    while fb:
        try:
            facebook = context.browser.find_element_by_xpath(obj.buttonFacebook2)
            facebookText = facebook.text
            if "LOG IN WITH FACEBOOK" in facebookText:
                facebook.click()
                time.sleep(2)
                window_before = context.browser.current_window_handle
                window_after = context.browser.window_handles[1]
                context.browser.switch_to_window(window_after)
                email = context.browser.find_element_by_id(objFacebook.emailField)
                email.send_keys(os.getenv("EMAIL_FACEBOOK"))
                password = context.browser.find_element_by_name(objFacebook.passwordField)
                password.send_keys(os.getenv("PASSWORD_FACEBOOK"))
                buttonLogin = WebDriverWait(context.browser, 5).until(EC.visibility_of_element_located((By.ID, objFacebook.loginbutton)))
                buttonLogin.click()
                time.sleep(3)
                context.browser.switch_to_window(window_before)
                time.sleep(7)
            else:
                print ("LOG IN WITH FACEBOOK not available")
            fb = False
        except NoSuchElementException:
            buttonMore = context.browser.find_element_by_xpath(obj.buttonMoreOption)
            buttonMore.click()

@when('I click the LOG IN WITH GOOGLE')
def step_impl(context):
    google = WebDriverWait(context.browser, 5).until(EC.visibility_of_element_located((By.XPATH, obj.buttonGoogle)))
    #google = context.browser.find_element_by_xpath(obj.buttonGoogle)
    googleText = google.text
    if "LOG IN WITH GOOGLE" in googleText:
        google.click()
        time.sleep(3)
        window_before = context.browser.current_window_handle
        window_after = context.browser.window_handles[1]
        context.browser.switch_to_window(window_after)
        identifierId = context.browser.find_element_by_id(objGoogle.identifierIdField)
        identifierId.clear()
        identifierId.send_keys(os.getenv("EMAIL_GMAIL"))
        identifierId.send_keys(Keys.RETURN)
        time.sleep(3)
        password = context.browser.find_element_by_name(objGoogle.passwordField)
        password.clear()
        password.send_keys(os.getenv("PASSWORD_GMAIL"))
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        context.browser.switch_to_window(window_before)
        time.sleep(10)
    else:
        print ("LOG IN WITH GOOGLE not available")

@when('I click the Allow notification')
def step_impl(context):
    buttonAllowNotif = WebDriverWait(context.browser, 5).until(EC.visibility_of_element_located((By.XPATH, obj.buttonAllowNotif)))
    buttonAllowNotif.click()

@when('I click the Enable notification')
def step_impl(context):
    browser = context.browser.desired_capabilities['browserName']
    if(browser=='chrome'):
        buttonEnableNotif = WebDriverWait(context.browser, 5).until(EC.visibility_of_element_located((By.XPATH, obj.buttonEnableNotif)))
        buttonEnableNotif.click()

@then('I see My Profile')
def step_impl(context):
    myProfile = WebDriverWait(context.browser, 10).until(EC.visibility_of_element_located((By.XPATH, obj.myProfile)))

@when('I click the Like button')
def step_impl(context):
    keepGoing = True
    limit = True
    swipe = 0
    while keepGoing:
        time.sleep(1)
        try:
            keepSwiping = WebDriverWait(context.browser, 3).until(EC.visibility_of_element_located((By.XPATH, obj.keepSwiping)))
            #keepSwiping = context.browser.find_element_by_xpath(obj.keepSwiping)
            context.browser.refresh()
            keepGoing = True
        except TimeoutException:
            try:
                buttonLike = WebDriverWait(context.browser, 3).until(EC.element_to_be_clickable((By.XPATH, obj.buttonLike)))
                #context.browser.find_element_by_xpath(obj.buttonLike).click()
                try:
                    ciwik = context.browser.find_element_by_xpath(obj.profileName).text
                    buttonLike.click()
                    swipe = swipe + 1
                    if (limit is True):
                        print(ciwik+" | "+str(swipe))
                    keepGoing = True
                except ElementClickInterceptedException:
                    if context.browser.find_element_by_xpath(obj.ModalUnlimited).is_displayed():
                        webdriver.ActionChains(context.browser).send_keys(Keys.ESCAPE).perform()
                        print("you're out of like")
                        limit = False
                        keepGoing = True
            except TimeoutException:
                context.browser.refresh()
                keepGoing = True
        except NoSuchElementException:
            context.browser.refresh()
            keepGoing = True

@given('I time sleep "{input}" s')
def step_impl(context, input):
    print(int(input))
    time.sleep(int(input))