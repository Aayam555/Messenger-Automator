def login(driver, email, password):
    email_input = driver.find_element_by_css_selector("#email").send_keys(email)
    password_input = driver.find_element_by_css_selector("#pass").send_keys(password)
    button = driver.find_element_by_css_selector("#loginbutton").click()
