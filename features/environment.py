from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import os
from dotenv import load_dotenv
import platform
from behave.log_capture import capture
import time

load_dotenv()

params = {
    "latitude": float(os.getenv("LATITUDE")),
    "longitude":float(os.getenv("LONGITUDE")),
    "accuracy": 100
    }
    
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
        context.browser.execute_cdp_cmd("Page.setGeolocationOverride", params)
    elif os.getenv("BROWSER") == "firefox":
        options = Options()
        options.set_preference('dom.webnotifications.enabled', False)
        options.set_preference("geo.prompt.testing", True)
        options.set_preference("geo.prompt.testing.allow", True)
        options.set_preference("geo.wifi.uri", 'data:application/json,{"location": {"lat": '+os.getenv("LATITUDE")+', "lng":'+os.getenv("LONGITUDE")+'}, "accuracy": 20.0}')
        if platform.system() == "Darwin":
            context.browser = webdriver.Firefox(options=options, executable_path="driver/firefox/Darwin/geckodriver")   
        elif platform.system() == "Windows":
            context.browser = webdriver.Chrome(executable_path="driver/firefox/Windows/geckodriver")
        elif platform.system() == "Linux":
            context.browser = webdriver.Chrome(executable_path="driver/firefox/Linux/geckodriver")
        # context.browser.execute_cdp_cmd("Page.setGeolocationOverride", params)

def after_all(context):
    # cleanup after tests run
    if os.getenv("PAUSE_ERROR") is True:
        time.sleep(360)
    context.browser.quit()