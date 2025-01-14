# this is a task from automation class by Aria Suseno - session 6.
# with selenium, automate the process to click each button and handle each alert.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep


def main():
    # variables init
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    # start test
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://demoqa.com/alerts")

    # first alert
    driver.find_element(By.ID, "alertButton").click()
    sleep(0.5)
    driver.switch_to.alert.accept()

    # second alert
    driver.find_element(By.ID, "timerAlertButton").click()
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        sleep(0.5)
        driver.switch_to.alert.accept()
    except TimeoutException:
        print("Alert not found")
        pass

    # third alert
    # scroll down to make the 'confirmButton' element visible
    confirmButton = driver.find_element(By.ID, "confirmButton")
    actions = ActionChains(driver)
    actions.scroll_to_element(confirmButton)
    actions.click(confirmButton)
    actions.perform()
    sleep(2)
    driver.switch_to.alert.accept()

    # fourth alert
    promptButton = driver.find_element(By.ID, "promtButton").click()
    actions = ActionChains(driver)
    actions.scroll_to_element(promptButton)
    actions.click(promptButton)
    actions.perform()
    sleep(2)
    driver.switch_to.alert.send_keys("Jesky")
    sleep(2)
    driver.switch_to.alert.accept()

    sleep(1)
    driver.quit()


main()
