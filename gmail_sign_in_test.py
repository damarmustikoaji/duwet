from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

load_dotenv()

# for firefox
options = Options()
options.set_preference('dom.webnotifications.enabled', False)
options.set_preference("geo.prompt.testing", True)
options.set_preference("geo.prompt.testing.allow", True)
# comment or uncomment if want to use
# driver = webdriver.Firefox(options=options, executable_path="driver/firefox/Darwin/geckodriver")  

# for chrome
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
# comment or uncomment if want to use
driver = webdriver.Chrome(options=options, executable_path="driver/chrome/Darwin/chromedriver")

buttonAccept = '//span[@class="Pos(r) Z(1)" and contains(text(), "I Accept")]'
buttonGoogle = '//button[@class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Pos(r) Cur(p) Tt(u) Bdrs(100px) Px(48px) Px(40px)--s Py(0) Mih(54px) button--outline Bdw(2px) Bds(s) Trsdu($fast) Bdc($c-secondary) C($c-secondary) Bdc($c-base):h C($c-base):h Bdc($c-base):f C($c-base):f Bdc($c-base):a C($c-base):a Fw($semibold) focus-button-style Mb(20px)--ml W(100%)--ml W(100%)--s Fz(4vw)--s"]'
identifierIdField = 'identifierId'
passwordField = 'password'
buttonAllowNotif = '//span[contains(text(), "Allow")]'
buttonEnableNotif = '//span[contains(text(), "Enable")]'
keepSwiping = '//span[@class="StretchedBox Pe(n) noBg+D(n) Z(-1) Bgc(#000.8) Bdf($overlay-blur)"]'
buttonLike = '//button[@type="button" and @aria-label="Like"]'

driver.delete_all_cookies()
browser = driver.desired_capabilities['browserName']
driver.get(os.getenv("TINDER_URL"))
assert "Tinder | Match. Chat. Date." in driver.title
time.sleep(3)
driver.find_element_by_xpath(buttonAccept).click()
time.sleep(2)
google = driver.find_element_by_xpath(buttonGoogle)
googleText = google.text
if "LOG IN WITH GOOGLE" in googleText:
    google.click()
    time.sleep(2)
    window_before = driver.current_window_handle
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    identifierId = driver.find_element_by_id(identifierIdField)
    identifierId.clear()
    identifierId.send_keys(os.getenv("EMAIL_GMAIL"))
    identifierId.send_keys(Keys.RETURN)
    time.sleep(3)
    password = driver.find_element_by_name(passwordField)
    password.clear()
    password.send_keys(os.getenv("PASSWORD_GMAIL"))
    password.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.switch_to_window(window_before)
    time.sleep(10)
    driver.find_element_by_xpath(buttonAllowNotif).click()
    time.sleep(3)
    if(browser=='chrome'):
        driver.find_element_by_xpath(buttonEnableNotif).click()
    time.sleep(3)
    keepGoing = True
    while keepGoing:
        time.sleep(3)
        try:
            driver.find_element_by_xpath(keepSwiping)
            driver.refresh()
            time.sleep(5)
            keepGoing = True
        except NoSuchElementException:
            try:
                driver.find_element_by_xpath(buttonLike).click()
                keepGoing = True
            except NoSuchElementException:
                driver.refresh()
                time.sleep(5)
                keepGoing = True
else:
    print ("LOG IN WITH GOOGLE not available")
driver.quit()