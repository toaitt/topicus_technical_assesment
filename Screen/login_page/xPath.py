login_page_url = 'https://demoqa.com/automation-practice-form'

# Practice form
first_name_field = "//input[@id='firstName']"
last_name_field = "//input[@id='lastName']"
email_field = "//input[@id='userEmail']"

gender_option = "//input[@type='radio' and @value='"
male_option = gender_option + "Male']/following-sibling::label"
female_option = gender_option + "Female']/following-sibling::label"
other_option = gender_option + "Other']/following-sibling::label"

mobile_field = "//input[@id='userNumber']"

date_of_birth = "//input[@id='dateOfBirthInput']"
year_select = "//select[contains(@class, 'year-select')]"
month_select = "//select[contains(@class, 'month-select')]"
date_box = "//div[contains(@class, 'datepicker__month') and @role='listbox']"

subjects_field = "//div[contains(@class, 'subjects-auto-complete__value-container')]"
sports_checkbox = "//input[contains(@id, 'hobbies-checkbox') and @value=1]/following-sibling::label"
reading_checkbox = "//input[contains(@id, 'hobbies-checkbox') and @value=2]/following-sibling::label"
music_checkbox = "//input[contains(@id, 'hobbies-checkbox') and @value=3]/following-sibling::label"

picture_select = "//label[@for='uploadPicture']"
address_field = "//textarea[@id='currentAddress']"
state_field = "//div[@id='state']//input"
city_field = "//div[@id='city']//input"

submit_button = "//button[@id='submit']"
form_table = "//div[@class='table-responsive']//tbody"
