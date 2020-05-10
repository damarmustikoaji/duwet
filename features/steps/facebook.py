from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os
from features.object import facebook

load_dotenv()

obj         = facebook.object_repository

@given('I go to facebook')
def step_impl(context):
    context.browser.get(os.getenv('FACEBOOK_URL'))

@then('It should have a title Facebook')
def step_impl(context):
    title = context.browser.title
    if 'Facebook' in title:
        assert context.browser.title == 'Facebook - Masuk atau Daftar'
    elif 'Facebook' in title:
        assert context.browser.title == 'Facebook – log in or sign up'

@when('I fill in facebook email field with "{input}"')
def step_impl(context, input):
    emailField = WebDriverWait(context.browser, 5).until(EC.visibility_of_element_located((By.ID, obj.emailField)))
    emailField.clear()
    emailField.send_keys(input)

@when('I fill in facebook password field with "{input}"')
def step_impl(context, input):
    passwordField = WebDriverWait(context.browser, 5).until(EC.visibility_of_element_located((By.ID, obj.passwordField)))
    passwordField.clear()
    passwordField.send_keys(input)

@when('I click the button login facebook')
def step_impl(context):
    buttonLogin = WebDriverWait(context.browser, 5).until(EC.visibility_of_element_located((By.ID, obj.loginbutton)))
    buttonLogin.click()

@then('It should have element "{element}" dengan nama "{string}"')
def step_impl(context, element, string):
    myProfile = WebDriverWait(context.browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//a[@data-testid="'+element+string+'"]')))
    print(myProfile.text)
    assert myProfile.text in context.browser.page_source