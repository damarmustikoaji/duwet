from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
from dotenv import load_dotenv
import platform
from behave.log_capture import capture
import time

load_dotenv()

def before_all(context):
    if os.getenv("BROWSER") == "chrome":
        if platform.system() == "Darwin":
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications" : 2}
            options.add_experimental_option("prefs",prefs)
            context.browser = webdriver.Chrome(options=options, executable_path="driver/chrome/Darwin/chromedriver")
        elif platform.system() == "Windows":
            context.browser = webdriver.Chrome(executable_path="driver/chrome/Windows/chromedriver")
        elif platform.system() == "Linux":
            context.browser = webdriver.Chrome(executable_path="driver/chrome/Linux/chromedriver")
    elif os.getenv("BROWSER") == "firefox":
        if platform.system() == "Darwin":
            options = Options()
            options.set_preference('dom.webnotifications.enabled', False)
            options.set_preference("geo.prompt.testing", True)
            options.set_preference("geo.prompt.testing.allow", True)
            context.browser = webdriver.Firefox(options=options, executable_path="driver/firefox/Darwin/geckodriver")   
        elif platform.system() == "Windows":
            context.browser = webdriver.Chrome(executable_path="driver/firefox/Windows/geckodriver")
        elif platform.system() == "Linux":
            context.browser = webdriver.Chrome(executable_path="driver/firefox/Linux/geckodriver")

def after_all(context):
    # cleanup after tests run
    # time.sleep(360)
    context.browser.quit()