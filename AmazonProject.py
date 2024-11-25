import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

# Empty list created to store productTitle and fresh product(only iphone 13)
productTitle =[]
freshList = []
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Chrome driver service connected--------------------------------------------------------------------------------------------------------------------

try:
    driver = webdriver.Chrome() # Trigger Chrome driver
    # implicitly wait for global timeout session
    driver.implicitly_wait(5)
    driver.get("https://www.amazon.in/") # After invoking the driver going to this url
    # Maximize the window
    driver.maximize_window()
    # Getting the search area
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    # Input the iphone 13 to the textbox
    search_box.send_keys("iphone 13")
    # Hitting the Enter Key
    search_box.send_keys(Keys.ENTER)
    # Getting the total number of results
    totalTitles = driver.find_elements(By.CSS_SELECTOR, ".s-title-instructions-style .a-text-normal")
    # Filling the fresh list and creating the product title list before printing
    for title in totalTitles:
        if "iPhone 13" in title.text:
            freshList.append(title)
            productTitle.append(title.text)

    # printing product titles and total results of iphone 13
    print("All Result Product Titles are -> ", productTitle)
    print("Total Results of iphone 13 in Amazon.in is -> ", len(freshList))
    # Getting the 4th Item from the list and clicking for a new tab
    if len(freshList) > 4:
        print("The 4th Item title is -> ", freshList[3].text)
        freshList[3].click()

    else:
        print("Less than 4 item available so can't show 4th result!!")
        driver.quit()
        exit()

    # Switching tab
    try:
        driver.switch_to.window(driver.window_handles[1])
    except IndexError:
            print("New tab did not open.")
            driver.quit()
            exit()
    # Clicking on Buy Now
    try:
        driver.find_element(By.ID, "buy-now-button").click()

    except Exception as e:
            print("Failed to find or click the 'Buy Now' button. Error:", str(e))
            driver.quit()
            exit()
    # Assigning login credential
    try:
        driver.find_element(By.ID, "ap_email").send_keys("8945864680")
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("Hello@123")
        driver.find_element(By.ID, "signInSubmit").click()
        textMsg = driver.find_element(By.CLASS_NAME,"a-list-item").text
    # Handling the assertion
    except AssertionError as ae:
        print("Assertion failed:", str(ae))
    except Exception as e:
        print("An error occurred during the login process:", str(e))

finally:
    print("Execution finished. Closing the browser.")
    time.sleep(15)
    driver.quit()
