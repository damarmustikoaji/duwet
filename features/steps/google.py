from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os
from features.object import google

load_dotenv()

obj         = google.object_repository

@given('I go to google')
def step_impl(context):
    context.browser.get(os.getenv('GOOGLE_URL'))

@then('It should have a title Google')
def step_impl(context):
    title = context.browser.title
    print(title)
    if 'Google Accounts' in title:
        assert context.browser.title == 'Sign in - Google Accounts'
    elif 'Akun Google' in title:
        assert context.browser.title == 'Masuk - Akun Google'

@when('I fill in email field with "{input}"')
def step_impl(context, input):
    emailField = WebDriverWait(context.browser, 5).until(EC.visibility_of_element_located((By.ID, obj.identifierIdField)))
    emailField.clear()
    emailField.send_keys(input)
    emailField.send_keys(Keys.RETURN)

@when('I fill in password field with "{input}"')
def step_impl(context, input):
    passwordField = WebDriverWait(context.browser, 5).until(EC.visibility_of_element_located((By.NAME, obj.passwordField)))
    passwordField.clear()
    passwordField.send_keys(input)
    passwordField.send_keys(Keys.RETURN)