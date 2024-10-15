import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import sys

def open_browser(detach=False, browser='Chrome'):
    if browser == 'Chrome':
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        driver_path = "WebDriver\\chromedriver-win64\\chromedriver.exe"
    elif browser == 'Edge':
        from selenium.webdriver.edge.options import Options
        from selenium.webdriver.edge.service import Service
        driver_path = "..\\WebDriver\\edgedriver_win64\\msedgedriver.exe"
    else:
        print("Wrong input browser type (Chrome or Edge only)")
        sys.exit()
    driver_options = Options()
    driver_options.add_argument('--lang=en')
    driver_options.use_chromium = True
    driver_options.add_argument("--start-maximized")
    driver_options.add_experimental_option('detach', detach)
    driver_options.add_argument('--guest')
    service = Service(executable_path=driver_path)
    if browser == 'Chrome':
        driver = webdriver.Chrome(options=driver_options, service=service)
    else:
        driver = webdriver.Edge(options=driver_options, service=service)
    return driver


def navigation(url, driver, wait_time=1, wait_item=None):
    driver.get(url)
    if not wait_item:
        time.sleep(wait_time)
    else:
        try:
            WebDriverWait(driver=driver, timeout=wait_time).until(ec.presence_of_element_located((By.XPATH, wait_item)))
        except TimeoutException:
            print(f"Time out waiting item {wait_item}")


def input_value(item_xpath, value, driver, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(ec.element_to_be_clickable((By.XPATH, item_xpath)))
        element = driver.find_element(by=By.XPATH, value=item_xpath)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].focus();", element)
        element.send_keys(value)
        time.sleep(0.5)
        return [value, True]
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [None, False]


def verify_item_available(item_xpath, driver, timeout=10, require=True):
    try:
        if require:
            WebDriverWait(driver=driver, timeout=timeout).until(ec.presence_of_element_located((By.XPATH, item_xpath)))
        else:
            WebDriverWait(driver=driver, timeout=timeout).until(ec.invisibility_of_element_located((By.XPATH, item_xpath)))
        success = True
    except TimeoutException:
        print(f"Item not appear: {item_xpath}" if require else f"Item still appear: {item_xpath}")
        success = False
    return [None, success]


def verify_item_attribute(item_xpath, attribute, driver, value=None, timeout=10, require=True):
    try:
        WebDriverWait(driver=driver, timeout=timeout).until(ec.presence_of_element_located((By.XPATH, item_xpath)))
        if value is not None:
            if attribute == 'text':
                return_value = True if driver.find_element(by=By.XPATH, value=item_xpath).text == value else False
                if not return_value:
                    print(f"Fail\n"
                          f"Actual: {driver.find_element(by=By.XPATH, value=item_xpath).text}\n"
                          f"Expect: {value}")
            else:
                return_value = True if driver.find_element(by=By.XPATH, value=item_xpath).get_attribute(attribute) == value else False
                if not return_value:
                    print(f"Fail\n"
                          f"Actual: {driver.find_element(by=By.XPATH, value=item_xpath).get_attribute(attribute)}"
                          f"Expect: {value}")
        else:
            return_value = driver.execute_script("return arguments[0].hasAttribute(arguments[1]);",
                                                 driver.find_element(by=By.XPATH, value=item_xpath), attribute)
            if not return_value and require:
                print(f"Fail: Can not find required attribute.")
                print(item_xpath)
    except TimeoutException:
        return_value = False
    return [None, return_value if require else not return_value]


def click_item(item_xpath, driver, timeout=10):
    try:
        if isinstance(item_xpath, str):
            WebDriverWait(driver=driver, timeout=timeout).until(ec.presence_of_element_located((By.XPATH, item_xpath)))
            driver.find_element(by=By.XPATH, value=item_xpath).click()
            return [None, True]
        elif isinstance(item_xpath, WebElement):
            item_xpath.click()
            return [None, True]
        else:
            print("Can only click on web element or xpath of an element")
            return [None, False]
    except TimeoutException:
        print(f"Item can not be found {item_xpath}")
        return [None, False]
