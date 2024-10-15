import os
import string
import random
from datetime import datetime
from selenium.webdriver.support.ui import Select
from Screen.login_page.xPath import *
from Settings.CommonStep import *
import pyautogui
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


def navigate_login_page(driver):
    navigation(url=login_page_url, driver=driver)
    return [None, True]


def input_first_name(driver):
    cr_date = str(datetime.now().strftime('%Y_%m_%d'))
    return input_value(item_xpath=first_name_field, value=f"Executing at {cr_date}", driver=driver)


def input_last_name(driver):
    cr_time = str(datetime.now().strftime('%H_%M'))
    return input_value(item_xpath=last_name_field, value=f"Executing at {cr_time}", driver=driver)


def input_email_field(driver):
    length = random.randint(2, 5)
    letters = string.ascii_letters
    input_email = f"aAzZ{str(datetime.now().strftime('%Y_%m_%d-%H-%M..'))}@aAzZ{str(datetime.now().strftime('%Y_%m_%d-%H-%M.'))}" + (
        ''.join(random.choice(letters) for _ in range(length)))
    return input_value(item_xpath=email_field, value=input_email, driver=driver)


def select_gender(driver, option=None):
    try:
        if option and option.lower() == 'male':
            return ['Male', click_item(item_xpath=male_option, driver=driver)[1]]
        elif option and option.lower() == 'female':
            return ['Female', click_item(item_xpath=female_option, driver=driver)[1]]
        elif option and option.lower() == 'other':
            return ['Other', click_item(item_xpath=other_option, driver=driver)[1]]
        else:
            selected_option = random.choice([male_option, female_option, other_option])
            selected_text = 'Male' if selected_option == male_option else 'Female' if selected_option == female_option else 'Other'
            return [selected_text, click_item(item_xpath=selected_option, driver=driver)[1]]
    except Exception as e:
        print(f"An error occurred: {e}")
        return [None, False]


def input_mobile_num(driver, numb=None, length=10):
    return input_value(item_xpath=mobile_field, driver=driver,
                       value=numb if numb is not None else ''.join(random.choice(string.digits) for _ in range(length)))


def check_validation_error(driver, item_xpath):
    try:
        input_field = driver.find_element(by=By.XPATH, value=item_xpath)
        border_color = driver.execute_script(
            "return window.getComputedStyle(arguments[0], null).getPropertyValue('border-color');", input_field)
        border_color = border_color.split('(')[-1][:-1].split(", ")
        if int(border_color[0]) > 200:
            print(f'Successfully checked error border in {item_xpath}')
            return ['red', True]
        else:
            print("No validation error detected")
            return [None, False]
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [e, False]


def select_date_of_birth(driver):
    try:
        click_item(item_xpath=date_of_birth, driver=driver)
        time.sleep(0.5)
        click_item(item_xpath=year_select, driver=driver)
        time.sleep(0.5)
        select = Select(driver.find_element(by=By.XPATH, value=year_select))
        year_selected = random.choice(select.options)
        y = year_selected.text
        year_selected.click()
        click_item(item_xpath=month_select, driver=driver)
        time.sleep(0.5)
        select = Select(driver.find_element(by=By.XPATH, value=month_select))
        month_selected = random.choice(select.options)
        m = month_selected.text
        month_selected.click()
        time.sleep(0.5)
        week_idx = random.randint(2, 5)
        col_idx = random.randint(1, 7)
        date_e = driver.find_element(by=By.XPATH, value=date_box + f"/div[{week_idx}]/div[{col_idx}]")
        d = date_e.text.zfill(2)
        date_e.click()
        time.sleep(1)
        if driver.find_element(by=By.XPATH, value=date_of_birth).get_attribute('value') == f"{d} {m[:3]} {y}":
            return [f"{d} {m},{y}", True]
        else:
            print(f"Actual: {driver.find_element(by=By.XPATH, value=date_of_birth).get_attribute('value')}")
            print(f'Expect: {d} {m[:3]} {y}')
            return [None, False]
    except TimeoutException:
        return [None, False]


def input_subject(driver, subject_list=None):
    try:
        if subject_list is None:
            return ['', True]
        else:
            pyautogui.press('tab')
            for subject in subject_list:
                # Input the subject
                pyautogui.typewrite(subject, interval=0.1)
                pyautogui.press('tab')
            return [', '.join(subject_list), True]
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [None, False]


def select_hobbies(driver, hobbies_list=None):
    try:
        if hobbies_list is None:
            full_list = ['Sports', 'Reading', 'Music']
            for h in full_list:
                if random.randint(0, 1) == 0:
                    full_list.remove(h)
            hobbies_list = full_list
        for h in hobbies_list:
            if h == 'Sports':
                click_item(item_xpath=sports_checkbox, driver=driver)
            if h == 'Reading':
                click_item(item_xpath=reading_checkbox, driver=driver)
            if h == 'Music':
                click_item(item_xpath=music_checkbox, driver=driver)
        return [', '.join(hobbies_list), True]
    except TimeoutException:
        return [None, False]


def choose_picture_file(driver, picture_path=None):
    try:
        import pyperclip
        if picture_path is None:
            picture_path = os.path.join(os.getcwd(), 'Screen\\login_page\\temp_screenshot.png')
            driver.save_screenshot(picture_path)
            pyperclip.copy(picture_path)
        elif picture_path == '':
            return [None, True]

        driver.find_element(by=By.XPATH, value=picture_select).click()
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        file_name = str(picture_path).split('\\')[-1]
        return [file_name, True]
    except Exception as e:
        print(f"An error occurred: {e}")
        return [None, False]

def input_address(driver, address=None):
    try:
        if address is None:
            address = f"Executing at {str(datetime.now().strftime('%Y_%m_%d'))}"
        elif address == '':
            return [None, True]
        input_value(driver=driver, item_xpath=address_field, value=address)
        return [address, True]
    except TimeoutException:
        print('Can not find address text box.')
        return [None, False]


def select_state_and_city(driver, state=None, city=None):
    state_dic = {'NCR': ['Delhi', 'Gurgaon', 'Noida'],
                 'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
                 'Haryana': ['Karnal', 'Panipat'],
                 'Rajasthan': ['Jaipur', 'Jaiselmer']}
    try:
        if state == '':
            return [None, True]
        if state is None or state not in state_dic:
            if state is not None:
                print(f'State not found {state}')
            state = random.choice([*state_dic])
            city = random.choice(state_dic[state])
        if state in state_dic:
            if city != '' and (city is None or city not in state_dic[state]):
                if city is not None:
                    print(f"City not found {city}")
                city = random.choice(state_dic[state])
        input_value(item_xpath=state_field, value=state, driver=driver)
        pyautogui.press('enter')
        input_value(item_xpath=city_field, value=city, driver=driver)
        pyautogui.press('enter')
        return [' '.join([state, city]), True]
    except TimeoutException:
        return [None, False]


def click_submit_button(driver):
    return click_item(item_xpath=submit_button, driver=driver)


def verify_form(driver, results):
    try:
        fail_list = []
        if not verify_item_attribute(driver=driver, item_xpath=f"{form_table}/tr[1]/td[2]", attribute='text', value=f"{results[1][0]} {results[2][0]}")[1]:
            fail_list.append('Student Name')
        if not verify_item_attribute(driver=driver, item_xpath=f"{form_table}/tr[2]/td[2]", attribute='text', value=results[3][0])[1]:
            fail_list.append('Student Email')
        if not verify_item_attribute(driver=driver, item_xpath=f"{form_table}/tr[3]/td[2]", attribute='text', value=results[4][0])[1]:
            fail_list.append('Gender')
        if not verify_item_attribute(driver=driver, item_xpath=f"{form_table}/tr[4]/td[2]", attribute='text', value=results[5][0])[1]:
            fail_list.append('Mobile')
        if not verify_item_attribute(driver=driver, item_xpath=f"{form_table}/tr[5]/td[2]", attribute='text', value=results[6][0])[1]:
            fail_list.append('Date of Birth')
        if not verify_item_attribute(driver=driver, item_xpath=f"{form_table}/tr[6]/td[2]", attribute='text', value=results[7][0])[1]:
            fail_list.append('Subjects')
        if not verify_item_attribute(driver=driver, item_xpath=f"{form_table}/tr[7]/td[2]", attribute='text', value=results[8][0])[1]:
            fail_list.append('Hobbies')
        if not verify_item_attribute(driver=driver, item_xpath=f"{form_table}/tr[8]/td[2]", attribute='text', value=results[9][0])[1]:
            fail_list.append('Picture')
        if not verify_item_attribute(driver=driver, item_xpath=f"{form_table}/tr[9]/td[2]", attribute='text', value=results[10][0])[1]:
            fail_list.append('Address')
        if not verify_item_attribute(driver=driver, item_xpath=f"{form_table}/tr[10]/td[2]", attribute='text', value=results[11][0])[1]:
            fail_list.append('State and City')
        if fail_list:
            print(f"Form failed at fields: {', '.join(fail_list)}")
            return [fail_list, False]
        else:
            return [None, True]
    except Exception as e:
        print(e)
        return [None, False]


