from Screen.login_page.xPath import *
from Screen.login_page import stepList
from Settings import CommonStep
from Settings.Settings import TestCase, Step
import openpyxl
import sys

execute_type = sys.argv[1]
driver = CommonStep.open_browser(detach=True)

ts_login_page = openpyxl.Workbook()
condition1 = ts_login_page.active
condition1.title = execute_type
con1_result = []

Verify_Form_Can_Submit = {
    'Case': TestCase(test_suit=ts_login_page, test_condition=condition1, name='Form_Can_Submit'),
    'Smoke test': True,
    'Regression test': True,
    'Pre-condition': []}
Verify_Form_Can_Submit_Step_List = [
    Step(stepList.navigate_login_page, driver=driver),
    Step(stepList.input_first_name, driver=driver),
    Step(stepList.input_last_name, driver=driver),
    Step(stepList.input_email_field, driver=driver),
    Step(stepList.select_gender, driver=driver),
    Step(stepList.input_mobile_num, driver=driver),
    Step(stepList.select_date_of_birth, driver=driver),
    Step(stepList.input_subject, driver=driver, subject_list=['Maths', 'Biology']),
    Step(stepList.select_hobbies, driver=driver),
    Step(stepList.choose_picture_file, driver=driver),
    Step(stepList.input_address, driver=driver),
    Step(stepList.select_state_and_city, driver=driver),
    Step(stepList.click_submit_button, driver=driver),
    Step(stepList.verify_form, driver=driver, results=Verify_Form_Can_Submit['Case'].results)
]


Verify_Mobile_Require_Field = {
    'Case': TestCase(test_suit=ts_login_page, test_condition=condition1, name='Mobile_Require_Field'),
    'Smoke test': False,
    'Regression test': True,
    'Pre-condition': []}
Verify_Mobile_Require_Field_Step_List = [
    Step(stepList.navigate_login_page, driver=driver),
    Step(stepList.input_first_name, driver=driver),
    Step(stepList.input_last_name, driver=driver),
    Step(stepList.input_email_field, driver=driver),
    Step(stepList.select_gender, driver=driver),
    # Step(stepList.input_mobile_num, driver=driver),
    Step(stepList.select_date_of_birth, driver=driver),
    Step(stepList.input_subject, driver=driver, subject_list=['Maths', 'Biology']),
    Step(stepList.select_hobbies, driver=driver),
    Step(stepList.choose_picture_file, driver=driver),
    Step(stepList.input_address, driver=driver),
    Step(stepList.select_state_and_city, driver=driver),
    Step(stepList.click_submit_button, driver=driver),
    Step(stepList.check_validation_error, driver=driver, item_xpath=mobile_field)
]

mapping_table = [
    {'Case': Verify_Form_Can_Submit,
     'Step': Verify_Form_Can_Submit_Step_List},
    {'Case': Verify_Mobile_Require_Field,
     'Step': Verify_Mobile_Require_Field_Step_List}
]

for case in mapping_table:
    if execute_type in case['Case']:
        if case['Case'][execute_type]:
            case['Case']['Case'].execute_test_case(step_list=case['Step'], mapping_table=mapping_table)
driver.quit()
